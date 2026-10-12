/**
 * Lily Corp Operator Takeover Companion — Frontend Application Logic
 * Built specifically for Jack Fay's Day 1-90 Industrial Acquisition
 */

// Global Reactive State
const state = {
  currentTab: 'primer',
  status: null,
  frontier: [],
  plans: [],
  selectedPlan: null,
  selectedPlanContent: '',
  generatedPages: [],
  frontierFilter: 'ALL',
  frontierSearch: ''
};

// Safe Markdown Parser Helper
function renderMarkdown(md) {
  if (!md) return '';
  if (typeof marked !== 'undefined' && marked.parse) {
    return marked.parse(md);
  }
  return md
    .replace(/^### (.*$)/gim, '<h3>$1</h3>')
    .replace(/^## (.*$)/gim, '<h2>$1</h2>')
    .replace(/^# (.*$)/gim, '<h1>$1</h1>')
    .replace(/\*\*(.*)\*\*/gim, '<strong>$1</strong>')
    .replace(/\*(.*)\*/gim, '<em>$1</em>')
    .replace(/`([^`]+)`/gim, '<code>$1</code>')
    .replace(/\n\n/gim, '<br><br>');
}

function escapeHtml(str) {
  if (!str) return '';
  return String(str)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#039;');
}

// App Initialization
document.addEventListener('DOMContentLoaded', () => {
  initApp();
});

async function initApp() {
  await Promise.all([
    loadStatus(),
    loadPlansList(),
    loadFrontierData(),
    loadGeneratedPages()
  ]);

  // Periodic background check
  setInterval(() => {
    loadStatus();
  }, 45000);
}

// ============================================================================
// Navigation & Tab Switching
// ============================================================================

function switchTab(tabId) {
  state.currentTab = tabId;

  // Nav buttons
  document.querySelectorAll('.tab-btn').forEach(btn => {
    if (btn.getAttribute('data-tab') === tabId) {
      btn.classList.add('active');
    } else {
      btn.classList.remove('active');
    }
  });

  // Tab content panes
  document.querySelectorAll('.tab-content').forEach(pane => {
    if (pane.id === `tab-${tabId}`) {
      pane.classList.add('active');
    } else {
      pane.classList.remove('active');
    }
  });

  // Default selection when entering plans
  if (tabId === 'plans' && !state.selectedPlan && state.plans.length > 0) {
    // Look for operator guide first
    const guidePlan = state.plans.find(p => p.filename.includes('operator_guide'));
    selectPlan(guidePlan ? guidePlan.filename : state.plans[0].filename);
  }

  // Scroll to top smoothly
  window.scrollTo({ top: 0, behavior: 'smooth' });
}

// ============================================================================
// Status & Header Metrics
// ============================================================================

async function loadStatus() {
  try {
    const res = await fetch('/api/status');
    if (!res.ok) return;
    const data = await res.json();
    state.status = data;

    const cycleText = document.getElementById('activeCycleText');
    if (cycleText && data.active_cycle) {
      cycleText.textContent = `Engine Cycle #${data.active_cycle}`;
    }
  } catch (err) {
    console.warn('Could not fetch status:', err);
  }
}

// ============================================================================
// Jargon Decoder Filter
// ============================================================================

function filterJargon() {
  const query = (document.getElementById('jargonSearchInput')?.value || '').toLowerCase().trim();
  const cards = document.querySelectorAll('.jargon-card');
  cards.forEach(card => {
    const text = card.textContent.toLowerCase();
    card.style.display = (!query || text.includes(query)) ? 'flex' : 'none';
  });
}

// ============================================================================
// Operator AI Advisor Q&A
// ============================================================================

function askQuickPrompt(promptText) {
  const input = document.getElementById('advisorQuestionInput');
  if (input) {
    input.value = promptText;
    submitAdvisorQuestion();
  }
}

async function submitAdvisorQuestion() {
  const input = document.getElementById('advisorQuestionInput');
  const question = input ? input.value.trim() : '';
  if (!question) return;

  const btn = document.getElementById('advisorSubmitBtn');
  const responseArea = document.getElementById('advisorResponseArea');
  const responseContent = document.getElementById('advisorResponseContent');
  const timestampEl = document.getElementById('advisorTimestamp');

  if (btn) {
    btn.disabled = true;
    btn.innerHTML = '⏳ Consulting Verified Records...';
  }

  responseArea.style.display = 'block';
  responseContent.innerHTML = `
    <div class="loading-state">
      <div class="pulse-dot" style="margin: 0 auto 1rem; width: 12px; height: 12px;"></div>
      <p>Analyzing Lily Corp verified shop records, operator playbook, and capital constraints...</p>
    </div>
  `;

  try {
    const res = await fetch('/api/ask-advisor', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ question: question })
    });

    if (!res.ok) {
      throw new Error(`Advisor query failed (${res.status})`);
    }

    const data = await res.json();
    if (data.answer) {
      responseContent.innerHTML = renderMarkdown(data.answer);
      if (timestampEl) {
        timestampEl.textContent = new Date().toLocaleTimeString();
      }
      // Scroll into view
      responseArea.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    } else {
      responseContent.innerHTML = '<p class="text-rose">No response received from advisor.</p>';
    }
  } catch (err) {
    responseContent.innerHTML = `<p class="text-rose">Error consulting advisor: ${escapeHtml(err.message)}</p>`;
  } finally {
    if (btn) {
      btn.disabled = false;
      btn.innerHTML = '<span class="icon">✨</span> Get Operator Guidance';
    }
  }
}

// ============================================================================
// Business Plans Viewer
// ============================================================================

async function loadPlansList() {
  const listEl = document.getElementById('planListContainer');
  try {
    const res = await fetch('/api/plans');
    if (!res.ok) throw new Error('Failed to load plans');
    const data = await res.json();
    state.plans = data.plans || [];
    renderPlanList();
  } catch (err) {
    console.error('Error loading plans:', err);
    if (listEl) {
      listEl.innerHTML = `<div class="empty-state">Failed to load plan modules: ${err.message}</div>`;
    }
  }
}

function renderPlanList() {
  const listEl = document.getElementById('planListContainer');
  if (!listEl) return;

  listEl.innerHTML = state.plans.map(p => {
    const isSelected = state.selectedPlan === p.filename;
    const isGrave = p.is_graveyard;
    const icon = isGrave ? '🪦' : '📄';
    const isGuide = p.filename.includes('operator_guide');

    return `
      <div class="plan-sidebar-item ${isSelected ? 'active' : ''} ${isGrave ? 'graveyard-item' : ''}" onclick="selectPlan('${escapeHtml(p.filename)}')">
        <span class="plan-item-icon">${icon}</span>
        <div class="plan-item-info">
          <div class="plan-item-name">${escapeHtml(p.filename)} ${isGuide ? '⭐' : ''}</div>
          <div class="plan-item-sub">${p.lines} lines • ${Math.round(p.size_bytes / 1024)} KB</div>
        </div>
      </div>
    `;
  }).join('');
}

async function selectPlan(filename) {
  state.selectedPlan = filename;
  renderPlanList();

  const titleEl = document.getElementById('activePlanTitle');
  const bodyEl = document.getElementById('planViewerContent');

  if (titleEl) titleEl.textContent = filename;
  if (bodyEl) bodyEl.innerHTML = '<div class="loading-state">Loading plan content...</div>';

  try {
    const res = await fetch(`/api/plans/${encodeURIComponent(filename)}`);
    if (!res.ok) throw new Error('Failed to load plan module');
    const data = await res.json();
    state.selectedPlanContent = data.content || '';
    if (bodyEl) {
      bodyEl.innerHTML = renderMarkdown(state.selectedPlanContent);
    }
  } catch (err) {
    console.error('Error loading plan file:', err);
    if (bodyEl) {
      bodyEl.innerHTML = `<div class="empty-state">Failed to load content: ${err.message}</div>`;
    }
  }
}

function copyCurrentPlan() {
  if (!state.selectedPlanContent) return;
  navigator.clipboard.writeText(state.selectedPlanContent).then(() => {
    alert('Plan markdown copied to clipboard!');
  }).catch(() => {
    alert('Could not copy to clipboard.');
  });
}

// ============================================================================
// Frontier & Diligence Initiatives (Tab 8)
// ============================================================================

async function loadFrontierData() {
  const container = document.getElementById('frontierCardsContainer');
  try {
    const res = await fetch('/api/frontier');
    if (!res.ok) throw new Error('Failed to load frontier');
    const data = await res.json();
    state.frontier = data.items || [];
    renderFrontierCards();
    populateModalDropdown();
  } catch (err) {
    console.error('Error loading frontier:', err);
    if (container) {
      container.innerHTML = `<div class="empty-state">Failed to load diligence items: ${err.message}</div>`;
    }
  }
}

function setFrontierFilter(filter) {
  state.frontierFilter = filter;
  document.querySelectorAll('.filter-pill').forEach(pill => {
    pill.classList.toggle('active', pill.textContent.toUpperCase() === filter);
  });
  renderFrontierCards();
}

function filterFrontierCards() {
  state.frontierSearch = (document.getElementById('frontierSearchInput')?.value || '').toLowerCase().trim();
  renderFrontierCards();
}

function renderFrontierCards() {
  const container = document.getElementById('frontierCardsContainer');
  if (!container) return;

  let items = state.frontier;

  // Filter by category/status
  if (state.frontierFilter === 'CRITICAL') {
    items = items.filter(x => x.priority === 'CRITICAL');
  } else if (state.frontierFilter === 'RESOLVED') {
    items = items.filter(x => x.status === 'RESOLVED');
  } else if (state.frontierFilter === 'REFINED') {
    items = items.filter(x => x.status === 'REFINED');
  }

  // Filter by search text
  if (state.frontierSearch) {
    items = items.filter(x => {
      const txt = `${x.id} ${x.title || ''} ${x.question || ''} ${x.category || ''}`.toLowerCase();
      return txt.includes(state.frontierSearch);
    });
  }

  if (items.length === 0) {
    container.innerHTML = '<div class="empty-state" style="grid-column: 1/-1;">No initiatives match your filter.</div>';
    return;
  }

  // Render top 40 for responsiveness
  const displayItems = items.slice(0, 40);

  container.innerHTML = displayItems.map(item => {
    const score = item.confidence_score !== undefined ? `${item.confidence_score}/10` : 'N/A';
    const statusColor = item.status === 'RESOLVED' ? 'status-resolved' : (item.status === 'REFINED' ? 'status-refined' : 'status-open');

    return `
      <div class="frontier-card card">
        <div class="frontier-header">
          <span class="frontier-id">${escapeHtml(item.id)}</span>
          <span class="frontier-badge ${statusColor}">${escapeHtml(item.status || 'OPEN')}</span>
        </div>
        <h4 class="frontier-title">${escapeHtml(item.title || 'Initiative')}</h4>
        <p class="frontier-question">${escapeHtml(item.question || '')}</p>
        
        <div class="frontier-footer">
          <div class="frontier-meta">
            <span class="score-tag">Confidence: ${score}</span>
            ${item.github_pr ? `
              <a href="${escapeHtml(item.github_pr)}" target="_blank" class="github-pr-tag ${item.github_auto_merged ? 'merged' : 'pending'}">
                🐙 PR #${escapeHtml(String(item.github_pr_number || ''))} ${item.github_auto_merged ? 'Merged ✓' : 'Review ⏳'}
              </a>
            ` : ''}
          </div>
          <button class="btn btn-outline btn-sm" onclick="openGenerateModalWithItem('${item.id}')">
            ✨ Generate Brief
          </button>
        </div>
      </div>
    `;
  }).join('');
}

function populateModalDropdown() {
  const sel = document.getElementById('modalItemId');
  if (!sel) return;
  sel.innerHTML = '<option value="">-- General Diligence Review --</option>' +
    state.frontier.slice(0, 50).map(i => {
      return `<option value="${escapeHtml(i.id)}">${escapeHtml(i.id)}: ${escapeHtml(i.title || '')}</option>`;
    }).join('');
}

// ============================================================================
// Generated AI HTML Pages (Tab 8 Gallery)
// ============================================================================

async function loadGeneratedPages() {
  const container = document.getElementById('generatedPagesContainer');
  try {
    const res = await fetch('/api/generated-pages');
    if (!res.ok) return;
    const data = await res.json();
    state.generatedPages = data.pages || [];
    renderGeneratedPages();
  } catch (err) {
    console.error('Error loading generated pages:', err);
  }
}

function renderGeneratedPages() {
  const container = document.getElementById('generatedPagesContainer');
  if (!container) return;

  if (state.generatedPages.length === 0) {
    container.innerHTML = '<div class="empty-state" style="grid-column: 1/-1;">No AI review pages generated yet. Click "Generate AI Page" to create one.</div>';
    return;
  }

  container.innerHTML = state.generatedPages.map(p => {
    return `
      <div class="page-card card">
        <div class="page-card-header">
          <span class="template-pill">${escapeHtml(p.template_type || 'briefing')}</span>
          <span class="page-date">${new Date(p.created_at).toLocaleDateString()}</span>
        </div>
        <h4 class="page-title">${escapeHtml(p.title || 'Generated View')}</h4>
        <div class="page-card-footer">
          <a href="${escapeHtml(p.url)}" target="_blank" class="btn btn-primary btn-sm">
            🔗 Open Full Page
          </a>
        </div>
      </div>
    `;
  }).join('');
}

// ============================================================================
// AI Page Generator Modal
// ============================================================================

function openGenerateModal() {
  const modal = document.getElementById('generateModal');
  if (modal) modal.style.display = 'flex';
}

function openGenerateModalWithItem(itemId) {
  openGenerateModal();
  const sel = document.getElementById('modalItemId');
  if (sel) sel.value = itemId;
}

function closeModal(modalId) {
  const modal = document.getElementById(modalId);
  if (modal) modal.style.display = 'none';
}

function closeModalOnBackdrop(event, modalId) {
  if (event.target.id === modalId) {
    closeModal(modalId);
  }
}

async function submitGeneratePage() {
  const templateType = document.getElementById('modalTemplateType')?.value || 'briefing';
  const itemId = document.getElementById('modalItemId')?.value || null;
  const customPrompt = document.getElementById('modalCustomPrompt')?.value || null;
  const btn = document.getElementById('btnSubmitGenerate');

  if (btn) {
    btn.disabled = true;
    btn.textContent = 'Generating Page...';
  }

  try {
    const res = await fetch('/api/generate-page', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        template_type: templateType,
        item_id: itemId,
        custom_prompt: customPrompt
      })
    });

    if (!res.ok) throw new Error(`Generation failed (${res.status})`);
    const data = await res.json();

    closeModal('generateModal');
    await loadGeneratedPages();

    // Open generated page in new tab
    if (data.url) {
      window.open(data.url, '_blank');
    }
  } catch (err) {
    alert(`Error generating page: ${err.message}`);
  } finally {
    if (btn) {
      btn.disabled = false;
      btn.textContent = 'Generate Page';
    }
  }
}
