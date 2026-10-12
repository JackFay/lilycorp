/**
 * Lily Corp Autonomous Plan Cockpit & AI Page Generator
 * Frontend Logic & Reactive State Management
 */

// Global State
const state = {
  currentTab: 'frontier',
  status: null,
  frontier: [],
  plans: [],
  selectedPlan: null,
  generatedPages: [],
  graveyard: [],
  steering: null,
  selectedItemIdForGen: null
};

// Safe markdown renderer helper
function renderMarkdown(md) {
  if (!md) return '';
  if (typeof marked !== 'undefined' && marked.parse) {
    return marked.parse(md);
  }
  // Fallback simple renderer
  return md
    .replace(/^### (.*$)/gim, '<h3>$1</h3>')
    .replace(/^## (.*$)/gim, '<h2>$1</h2>')
    .replace(/^# (.*$)/gim, '<h1>$1</h1>')
    .replace(/\*\*(.*)\*\*/gim, '<strong>$1</strong>')
    .replace(/\*(.*)\*/gim, '<em>$1</em>')
    .replace(/`([^`]+)`/gim, '<code>$1</code>')
    .replace(/\n\n/gim, '<br><br>');
}

// Initial bootstrap on DOM ready
document.addEventListener('DOMContentLoaded', () => {
  initApp();
});

async function initApp() {
  await loadStatus();
  await loadFrontierData();
  await loadGeneratedPages();
  await loadPlansList();
  
  // Setup auto-refresh every 30 seconds for live background sync
  setInterval(() => {
    loadStatus(false);
  }, 30000);
}

// ============================================================================
// Navigation & Tabs
// ============================================================================

function switchTab(tabId) {
  state.currentTab = tabId;

  // Update nav buttons
  document.querySelectorAll('.tab-btn').forEach(btn => {
    if (btn.getAttribute('data-tab') === tabId) {
      btn.classList.add('active');
    } else {
      btn.classList.remove('active');
    }
  });

  // Update tab content panes
  document.querySelectorAll('.tab-content').forEach(pane => {
    if (pane.id === `tab-${tabId}`) {
      pane.classList.add('active');
    } else {
      pane.classList.remove('active');
    }
  });

  // Lazy-load data when switching
  if (tabId === 'plans' && state.plans.length > 0 && !state.selectedPlan) {
    // Select first plan by default
    selectPlan(state.plans[0].filename);
  } else if (tabId === 'graveyard' && state.graveyard.length === 0) {
    loadGraveyardData();
  } else if (tabId === 'auditor') {
    loadAuditorData();
  } else if (tabId === 'pages') {
    loadGeneratedPages();
  }
}

function filterFrontierByStatus(status) {
  switchTab('frontier');
  const sel = document.getElementById('statusFilter');
  if (sel) {
    sel.value = status;
    renderFrontierList();
  }
}

// ============================================================================
// API Calls: Status & KPI
// ============================================================================

async function loadStatus(showVisualFeedback = true) {
  try {
    const res = await fetch('/api/status');
    if (!res.ok) throw new Error('Status fetch failed');
    const data = await res.json();
    state.status = data;

    // Update Header Pill
    const cycleText = document.getElementById('activeCycleText');
    if (cycleText) {
      cycleText.textContent = `Cycle #${data.active_cycle || 0} Active`;
    }

    // Update KPI Banner
    const totalEl = document.getElementById('kpiTotalItems');
    if (totalEl) totalEl.textContent = data.total_frontier_items;

    const critEl = document.getElementById('kpiCriticalCount');
    if (critEl) {
      const critCount = data.priority_counts?.CRITICAL || 0;
      critEl.textContent = `${critCount} Critical Priorities`;
    }

    const resolvedEl = document.getElementById('kpiResolvedCount');
    if (resolvedEl) resolvedEl.textContent = data.status_counts?.RESOLVED || 0;

    const refinedEl = document.getElementById('kpiRefinedCount');
    if (refinedEl) refinedEl.textContent = data.status_counts?.REFINED || 0;

    const exploratoryEl = document.getElementById('kpiExploratoryCount');
    if (exploratoryEl) exploratoryEl.textContent = data.status_counts?.EXPLORATORY || 0;

    const graveyardEl = document.getElementById('kpiGraveyardCount');
    if (graveyardEl) graveyardEl.textContent = data.graveyard_count || 0;

    // Also update Auditor Tab digest if available
    const digestBadge = document.getElementById('digestCycleBadge');
    if (digestBadge) digestBadge.textContent = `Cycle #${data.active_cycle}`;

  } catch (err) {
    console.error('Error loading status:', err);
  }
}

// ============================================================================
// API Calls & Rendering: Frontier
// ============================================================================

async function loadFrontierData() {
  const grid = document.getElementById('frontierGrid');
  try {
    const res = await fetch('/api/frontier');
    if (!res.ok) throw new Error('Failed to load frontier');
    const data = await res.json();
    state.frontier = data.items || [];
    renderFrontierList();
    populateInitiativeDropdown();
  } catch (err) {
    console.error('Error loading frontier:', err);
    if (grid) {
      grid.innerHTML = `<div class="empty-state">Failed to load frontier: ${err.message}</div>`;
    }
  }
}

function renderFrontierList() {
  const grid = document.getElementById('frontierGrid');
  if (!grid) return;

  const searchQuery = (document.getElementById('frontierSearch')?.value || '').toLowerCase().trim();
  const statusFilter = (document.getElementById('statusFilter')?.value || '').toUpperCase();
  const priorityFilter = (document.getElementById('priorityFilter')?.value || '').toUpperCase();

  const filtered = state.frontier.filter(item => {
    // Status filter
    if (statusFilter && item.status?.toUpperCase() !== statusFilter) {
      return false;
    }
    // Priority filter
    if (priorityFilter && item.priority?.toUpperCase() !== priorityFilter) {
      return false;
    }
    // Search query
    if (searchQuery) {
      const corpus = `${item.id || ''} ${item.title || ''} ${item.question || ''} ${item.category || ''} ${item.known_facts || ''}`.toLowerCase();
      if (!corpus.includes(searchQuery)) {
        return false;
      }
    }
    return true;
  });

  if (filtered.length === 0) {
    grid.innerHTML = `
      <div class="empty-state">
        <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">🔍</div>
        <h3>No Strategic Initiatives Found</h3>
        <p>No frontier items match your active search or filter criteria.</p>
        <button class="btn btn-outline btn-sm" onclick="resetFrontierFilters()" style="margin-top: 1rem;">Reset Filters</button>
      </div>
    `;
    return;
  }

  grid.innerHTML = filtered.map(item => {
    // Score Badge Class
    const score = parseFloat(item.confidence_score) || 0;
    let scoreBadge = '';
    if (score >= 8.0) {
      scoreBadge = `<span class="score-pill score-high">★ ${score.toFixed(1)}/10 Grounded</span>`;
    } else if (score >= 5.0) {
      scoreBadge = `<span class="score-pill score-mid">● ${score.toFixed(1)}/10 Refined</span>`;
    } else {
      scoreBadge = `<span class="score-pill score-low">⚠ ${score.toFixed(1)}/10 Exploratory</span>`;
    }

    // Status Class
    let statusClass = 'badge-open';
    if (item.status === 'RESOLVED') statusClass = 'badge-resolved';
    else if (item.status === 'REFINED') statusClass = 'badge-refined';
    else if (item.status === 'EXPLORATORY') statusClass = 'badge-exploratory';

    // Priority Class
    let priorityClass = 'badge-med';
    if (item.priority === 'CRITICAL') priorityClass = 'badge-crit';
    else if (item.priority === 'HIGH') priorityClass = 'badge-high';
    else if (item.priority === 'LOW') priorityClass = 'badge-low';

    // Target plan basename
    const planName = item.target_plan_file ? item.target_plan_file.split('/').pop() : '';

    return `
      <div class="frontier-card card">
        <div class="frontier-card-header">
          <div class="frontier-id-wrap">
            <span class="frontier-id">${escapeHtml(item.id || 'ITEM')}</span>
            <span class="badge ${statusClass}">${escapeHtml(item.status || 'OPEN')}</span>
            <span class="badge ${priorityClass}">${escapeHtml(item.priority || 'MED')}</span>
          </div>
          <div>${scoreBadge}</div>
        </div>

        <h3 class="frontier-title">${escapeHtml(item.title || 'Untitled Strategic Initiative')}</h3>
        <p class="frontier-question">${escapeHtml(item.question || '')}</p>

        ${item.known_facts ? `
          <div class="frontier-facts">
            <div class="facts-label">Empirical Diligence Anchors:</div>
            <div class="facts-text">${escapeHtml(item.known_facts)}</div>
          </div>
        ` : ''}

        <div class="frontier-footer">
          <div class="frontier-meta">
            ${planName ? `<span class="plan-tag" onclick="selectPlanAndNavigate('${planName}')">📄 ${escapeHtml(planName)}</span>` : ''}
            <span class="cycle-tag">Cycle #${item.cycle_added || item.cycle_resolved || '0'}</span>
          </div>
          
          <div class="frontier-card-actions">
            <button class="btn btn-outline btn-sm" onclick="openGenerateModalWithItem('${item.id}', 'red_team')">
              🛡️ Red-Team
            </button>
            <button class="btn btn-primary btn-sm" onclick="openGenerateModalWithItem('${item.id}', 'briefing')">
              ✨ AI Briefing
            </button>
          </div>
        </div>
      </div>
    `;
  }).join('');
}

function resetFrontierFilters() {
  const s = document.getElementById('frontierSearch');
  if (s) s.value = '';
  const sf = document.getElementById('statusFilter');
  if (sf) sf.value = '';
  const pf = document.getElementById('priorityFilter');
  if (pf) pf.value = '';
  renderFrontierList();
}

function populateInitiativeDropdown() {
  const sel = document.getElementById('generateTargetItem');
  if (!sel) return;

  const currentVal = sel.value;
  sel.innerHTML = '<option value="">General Company Review</option>' + 
    state.frontier.map(item => {
      return `<option value="${escapeHtml(item.id)}">${escapeHtml(item.id)}: ${escapeHtml(item.title || '')}</option>`;
    }).join('');

  if (currentVal) {
    sel.value = currentVal;
  }
}

// ============================================================================
// API Calls & Rendering: Generated HTML Pages Gallery
// ============================================================================

async function loadGeneratedPages() {
  const grid = document.getElementById('generatedPagesGrid');
  try {
    const res = await fetch('/api/generated-pages');
    if (!res.ok) throw new Error('Failed to load generated pages');
    const data = await res.json();
    state.generatedPages = data.pages || [];

    // Update KPI count
    const kpiPages = document.getElementById('kpiPagesCount');
    if (kpiPages) kpiPages.textContent = state.generatedPages.length;

    renderGeneratedPagesGallery();
  } catch (err) {
    console.error('Error loading generated pages:', err);
    if (grid) {
      grid.innerHTML = `<div class="empty-state">Error loading gallery: ${err.message}</div>`;
    }
  }
}

function renderGeneratedPagesGallery() {
  const grid = document.getElementById('generatedPagesGrid');
  if (!grid) return;

  if (state.generatedPages.length === 0) {
    grid.innerHTML = `
      <div class="empty-state" style="grid-column: 1 / -1;">
        <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">⚡</div>
        <h3>No AI Pages Generated Yet</h3>
        <p>Click "Generate AI Page" or pick a template above to generate your first live on-the-fly review dashboard!</p>
        <button class="btn btn-primary" onclick="openGenerateModal()" style="margin-top: 1rem;">
          ✨ Generate First Page
        </button>
      </div>
    `;
    return;
  }

  grid.innerHTML = state.generatedPages.map(page => {
    // Template badge style
    let badgeClass = 'badge-briefing';
    let badgeLabel = 'Executive Briefing';
    if (page.template_type === 'red_team') {
      badgeClass = 'badge-red-team';
      badgeLabel = 'Red-Team Audit';
    } else if (page.template_type === 'operator_checklist') {
      badgeClass = 'badge-checklist';
      badgeLabel = 'Operator Checklist';
    } else if (page.template_type === 'custom') {
      badgeClass = 'badge-custom';
      badgeLabel = 'Custom Deep Dive';
    }

    // Relative or formatted date
    const dateFormatted = page.created_at ? new Date(page.created_at).toLocaleDateString(undefined, {
      month: 'short', day: 'numeric', hour: '2-digit', minute: '2-digit'
    }) : 'Recent';

    const kbSize = page.file_size ? `${Math.round(page.file_size / 1024)} KB` : 'Dynamic';

    return `
      <div class="page-card card">
        <div class="page-card-header">
          <span class="template-pill ${badgeClass}">${badgeLabel}</span>
          <span class="page-date">${dateFormatted}</span>
        </div>

        <h4 class="page-title">${escapeHtml(page.title || 'Untitled Page')}</h4>

        <div class="page-meta-row">
          ${page.item_id ? `<span class="page-item-tag">🎯 ${escapeHtml(page.item_id)}</span>` : ''}
          ${page.plan_file ? `<span class="page-plan-tag">📄 ${escapeHtml(page.plan_file.split('/').pop())}</span>` : ''}
          <span class="page-size-tag">${kbSize}</span>
        </div>

        <div class="page-card-footer">
          <button class="btn btn-primary btn-sm" onclick="previewPage('${page.page_id}', '${escapeHtml(page.title)}')">
            👁️ Open Preview
          </button>
          <a href="${page.url}" target="_blank" class="btn btn-outline btn-sm">
            🔗 Full Tab
          </a>
        </div>
      </div>
    `;
  }).join('');
}

// ============================================================================
// API Calls & Rendering: Live Business Plan Modules
// ============================================================================

async function loadPlansList() {
  const sidebar = document.getElementById('planSidebar');
  try {
    const res = await fetch('/api/plans');
    if (!res.ok) throw new Error('Failed to load plans');
    const data = await res.json();
    state.plans = data.plans || [];
    renderPlanSidebar();
  } catch (err) {
    console.error('Error loading plans list:', err);
    if (sidebar) {
      sidebar.innerHTML = `<div class="empty-state">Failed to load plans</div>`;
    }
  }
}

function renderPlanSidebar() {
  const sidebar = document.getElementById('planSidebar');
  if (!sidebar) return;

  sidebar.innerHTML = `
    <div class="sidebar-title">Plan Modules (${state.plans.length})</div>
    <div class="sidebar-list">
      ${state.plans.map(p => {
        const isSelected = state.selectedPlan === p.filename;
        const activeClass = isSelected ? 'active' : '';
        const isGrave = p.is_graveyard;
        const icon = isGrave ? '🪦' : '📄';

        return `
          <div class="plan-sidebar-item ${activeClass} ${isGrave ? 'graveyard-item' : ''}" onclick="selectPlan('${p.filename}')">
            <span class="plan-item-icon">${icon}</span>
            <div class="plan-item-info">
              <div class="plan-item-name">${escapeHtml(p.filename)}</div>
              <div class="plan-item-sub">${p.lines} lines • ${Math.round(p.size_bytes / 1024)} KB</div>
            </div>
          </div>
        `;
      }).join('')}
    </div>
  `;
}

async function selectPlan(filename) {
  state.selectedPlan = filename;
  renderPlanSidebar();

  const titleEl = document.getElementById('planViewerTitle');
  const metaEl = document.getElementById('planViewerMeta');
  const bodyEl = document.getElementById('planViewerBody');

  if (titleEl) titleEl.textContent = filename;
  if (bodyEl) bodyEl.innerHTML = '<div class="loading-state">Loading plan markdown...</div>';

  try {
    const res = await fetch(`/api/plans/${encodeURIComponent(filename)}`);
    if (!res.ok) throw new Error('Failed to load plan file');
    const data = await res.json();

    if (metaEl) {
      metaEl.innerHTML = `
        <span>${data.line_count} lines</span> • 
        <span>Modified: ${new Date(data.last_modified).toLocaleString()}</span>
        <button class="btn btn-outline btn-sm" style="margin-left: 1rem;" onclick="openGenerateModalWithPlan('${data.filename}')">
          ✨ Generate Review of this Module
        </button>
      `;
    }

    if (bodyEl) {
      bodyEl.innerHTML = renderMarkdown(data.content);
    }
  } catch (err) {
    console.error('Error loading plan file:', err);
    if (bodyEl) {
      bodyEl.innerHTML = `<div class="empty-state">Failed to load content: ${err.message}</div>`;
    }
  }
}

function selectPlanAndNavigate(filename) {
  switchTab('plans');
  selectPlan(filename);
}

// ============================================================================
// API Calls & Rendering: Auditor & Digestion Feed
// ============================================================================

async function loadAuditorData() {
  const digestEl = document.getElementById('digestContent');
  const archiveEl = document.getElementById('archiveContent');

  try {
    const res = await fetch('/api/steering');
    if (!res.ok) throw new Error('Failed to load steering & digest data');
    const data = await res.json();
    state.steering = data;

    if (digestEl) {
      digestEl.innerHTML = data.digest ? renderMarkdown(data.digest) : '<p class="text-muted">No cycle digest generated yet.</p>';
    }

    if (archiveEl) {
      archiveEl.innerHTML = data.archive_recent ? renderMarkdown(data.archive_recent) : '<p class="text-muted">No archived steering notes yet.</p>';
    }
  } catch (err) {
    console.error('Error loading auditor data:', err);
    if (digestEl) digestEl.innerHTML = `<div class="empty-state">Error: ${err.message}</div>`;
  }
}

// ============================================================================
// API Calls & Rendering: Graveyard Autopsies
// ============================================================================

async function loadGraveyardData() {
  const grid = document.getElementById('graveyardGrid');
  try {
    const res = await fetch('/api/graveyard');
    if (!res.ok) throw new Error('Failed to load graveyard');
    const data = await res.json();
    state.graveyard = data.concepts || [];

    if (grid) {
      if (state.graveyard.length === 0) {
        grid.innerHTML = `<div class="empty-state">The graveyard is currently empty. No ideas rejected yet.</div>`;
        return;
      }

      grid.innerHTML = state.graveyard.map(concept => {
        return `
          <div class="graveyard-card card">
            <div class="graveyard-card-header">
              <span class="grave-icon">🪦</span>
              <span class="grave-badge">${escapeHtml(concept.classification || 'REJECTED')}</span>
            </div>
            <h3 class="grave-title">${escapeHtml(concept.title || 'Untitled Rejected Idea')}</h3>
            <div class="grave-body markdown-body">
              ${renderMarkdown(concept.raw_text)}
            </div>
          </div>
        `;
      }).join('');
    }
  } catch (err) {
    console.error('Error loading graveyard:', err);
    if (grid) grid.innerHTML = `<div class="empty-state">Error: ${err.message}</div>`;
  }
}

// ============================================================================
// AI Page Generator Modal & Execution
// ============================================================================

function openGenerateModal(templateType = 'briefing') {
  const modal = document.getElementById('generateModal');
  if (!modal) return;

  // Set radio template
  const radios = document.querySelectorAll('input[name="tplType"]');
  radios.forEach(r => {
    if (r.value === templateType) {
      r.checked = true;
    }
  });

  toggleCustomPromptArea();
  modal.classList.add('open');
}

function openGenerateModalWithItem(itemId, templateType = 'briefing') {
  openGenerateModal(templateType);
  const sel = document.getElementById('generateTargetItem');
  if (sel) {
    sel.value = itemId;
  }
  // Try to pre-select corresponding plan if known
  const item = state.frontier.find(f => f.id === itemId);
  if (item && item.target_plan_file) {
    const pSel = document.getElementById('generateTargetPlan');
    if (pSel) pSel.value = item.target_plan_file;
  }
}

function openGenerateModalWithPlan(planFilename, templateType = 'briefing') {
  openGenerateModal(templateType);
  const pSel = document.getElementById('generateTargetPlan');
  if (pSel) {
    pSel.value = `plan/${planFilename}`;
  }
}

function toggleCustomPromptArea() {
  const selectedType = document.querySelector('input[name="tplType"]:checked')?.value;
  const area = document.getElementById('customPromptGroup');
  if (area) {
    if (selectedType === 'custom') {
      area.style.display = 'block';
    } else {
      area.style.display = 'none';
    }
  }
}

async function executeAIPageGeneration() {
  const btn = document.getElementById('btnExecuteGenerate');
  const tplType = document.querySelector('input[name="tplType"]:checked')?.value || 'briefing';
  const targetItem = document.getElementById('generateTargetItem')?.value || null;
  const targetPlan = document.getElementById('generateTargetPlan')?.value || null;
  const customPrompt = document.getElementById('generateCustomPrompt')?.value || null;

  if (tplType === 'custom' && (!customPrompt || !customPrompt.trim())) {
    alert('Please enter a custom prompt or question for the AI to analyze.');
    return;
  }

  // Visual loading feedback
  const originalText = btn.innerHTML;
  btn.disabled = true;
  btn.innerHTML = `<span class="spinner"></span> Synthesizing with Gemini...`;

  try {
    const payload = {
      template_type: tplType,
      item_id: targetItem,
      plan_file: targetPlan,
      custom_prompt: customPrompt
    };

    const res = await fetch('/api/generate-page', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    });

    if (!res.ok) {
      const errData = await res.json();
      throw new Error(errData.detail || 'Page generation failed');
    }

    const data = await res.json();

    // Success! Close generate modal
    closeModal('generateModal');

    // Reload generated pages gallery & status
    await loadGeneratedPages();
    await loadStatus(false);

    // Immediately open in preview modal
    previewPage(data.page_id, data.title);

  } catch (err) {
    console.error('Error generating AI page:', err);
    alert(`Failed to generate AI page: ${err.message}`);
  } finally {
    btn.disabled = false;
    btn.innerHTML = originalText;
  }
}

// ============================================================================
// Preview Modal
// ============================================================================

function previewPage(pageId, title) {
  const modal = document.getElementById('previewModal');
  const iframe = document.getElementById('previewIframe');
  const titleEl = document.getElementById('previewModalTitle');
  const openTabBtn = document.getElementById('previewOpenTabBtn');

  if (!modal || !iframe) return;

  const url = `/view/${pageId}`;
  iframe.src = url;
  if (titleEl) titleEl.textContent = title || 'AI Generated Review Page';
  if (openTabBtn) openTabBtn.href = url;

  modal.classList.add('open');
}

// ============================================================================
// Steering & Diligence Cycle Controls
// ============================================================================

function openSteeringModal() {
  const modal = document.getElementById('steeringModal');
  if (modal) modal.classList.add('open');
}

async function submitSteeringFromModal() {
  const textEl = document.getElementById('modalSteeringText');
  const triggerEl = document.getElementById('modalSteeringTrigger');
  const note = textEl ? textEl.value.trim() : '';
  const trigger = triggerEl ? triggerEl.checked : false;

  if (!note) {
    alert('Please enter an operational steering note or fact correction.');
    return;
  }

  await doSubmitSteering(note, trigger);
  if (textEl) textEl.value = '';
  closeModal('steeringModal');
}

async function submitSteeringNote() {
  const textEl = document.getElementById('steeringInputText');
  const triggerEl = document.getElementById('steeringTriggerCycle');
  const note = textEl ? textEl.value.trim() : '';
  const trigger = triggerEl ? triggerEl.checked : false;

  if (!note) {
    alert('Please enter an operational steering note or fact correction.');
    return;
  }

  await doSubmitSteering(note, trigger);
  if (textEl) textEl.value = '';
}

async function doSubmitSteering(note, triggerCycle) {
  try {
    const res = await fetch('/api/steering', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ note: note, run_cycle_now: triggerCycle })
    });

    if (!res.ok) throw new Error('Failed to submit steering note');
    const data = await res.json();

    alert('Steering instruction archived into governance inbox! The recursive loop will ingest it.');
    await loadAuditorData();
  } catch (err) {
    console.error('Error submitting steering:', err);
    alert(`Error: ${err.message}`);
  }
}

async function triggerManualCycle() {
  const logBox = document.getElementById('cycleStatusLog');
  if (logBox) {
    logBox.style.display = 'block';
    logBox.innerHTML = '<span class="pulse-dot"></span> Launching recursive diligence cycle with Google Search and Adversarial Diligence Auditor in background...';
  }

  try {
    const res = await fetch('/api/run-cycle', { method: 'POST' });
    if (!res.ok) throw new Error('Failed to launch cycle');
    const data = await res.json();

    if (logBox) {
      logBox.innerHTML = `<strong>Cycle Launched!</strong> ${data.message} Status will automatically update when the cycle finishes.`;
    }
  } catch (err) {
    console.error('Error launching cycle:', err);
    if (logBox) {
      logBox.innerHTML = `<span style="color: var(--accent-rose);">Failed to launch cycle: ${err.message}</span>`;
    }
  }
}

// ============================================================================
// Modal Utilities & Helpers
// ============================================================================

function closeModal(modalId) {
  const modal = document.getElementById(modalId);
  if (modal) {
    modal.classList.remove('open');
    if (modalId === 'previewModal') {
      const iframe = document.getElementById('previewIframe');
      if (iframe) iframe.src = 'about:blank';
    }
  }
}

function closeModalOnBackdrop(event, modalId) {
  if (event.target && event.target.id === modalId) {
    closeModal(modalId);
  }
}

function escapeHtml(str) {
  if (!str) return '';
  return String(str)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#39;');
}
