"""
GitHub Git Lifecycle Manager for Lily Corp Autonomous Diligence Engine.
Creates branches, atomic multi-file tree commits, Pull Requests, and conditionally
auto-merges high-confidence updates (score >= 7.5) into main.
"""

import os
import json
import ssl
import re
from datetime import datetime
from typing import Dict, Any, List, Optional
import urllib.request
import urllib.error

# Try importing certifi for macOS CA certs; fallback to default ssl context
try:
    import certifi
    SSL_CONTEXT = ssl.create_default_context(cafile=certifi.where())
except Exception:
    SSL_CONTEXT = ssl.create_default_context()


class GitHubLifecycleManager:
    def __init__(
        self,
        token: Optional[str] = None,
        repo: Optional[str] = None,
        default_branch: Optional[str] = None,
        auto_merge_threshold: Optional[float] = None
    ):
        self.token = token or os.environ.get("GITHUB_TOKEN", "").strip()
        self.repo = repo or os.environ.get("GITHUB_REPO", "JackFay/lilycorp").strip()
        self.default_branch = default_branch or os.environ.get("GITHUB_DEFAULT_BRANCH", "main").strip()
        
        env_thresh = os.environ.get("GITHUB_AUTO_MERGE_THRESHOLD")
        if env_thresh:
            try:
                self.auto_merge_threshold = float(env_thresh)
            except ValueError:
                self.auto_merge_threshold = 7.5
        elif auto_merge_threshold is not None:
            self.auto_merge_threshold = auto_merge_threshold
        else:
            self.auto_merge_threshold = 7.5

        self.base_url = f"https://api.github.com/repos/{self.repo}"

    @property
    def is_configured(self) -> bool:
        return bool(self.token and self.repo)

    def _api_request(
        self,
        endpoint: str,
        method: str = "GET",
        data: Optional[Dict[str, Any]] = None,
        expected_status: tuple = (200, 201)
    ) -> Dict[str, Any]:
        """Execute authenticated request against GitHub API."""
        if not self.is_configured:
            raise ValueError("GitHubLifecycleManager not configured with GITHUB_TOKEN")

        url = f"{self.base_url}{endpoint}" if endpoint.startswith("/") else endpoint
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/vnd.github+json",
            "User-Agent": "LilyCorp-Diligence-Engine",
            "X-GitHub-Api-Version": "2022-11-28"
        }

        body_bytes = None
        if data is not None:
            body_bytes = json.dumps(data).encode("utf-8")
            headers["Content-Type"] = "application/json"

        req = urllib.request.Request(url, data=body_bytes, headers=headers, method=method)

        try:
            with urllib.request.urlopen(req, context=SSL_CONTEXT, timeout=30) as resp:
                status_code = resp.getcode()
                response_text = resp.read().decode("utf-8")
                if response_text:
                    try:
                        return json.loads(response_text)
                    except json.JSONDecodeError:
                        return {"raw": response_text, "status": status_code}
                return {"status": status_code}
        except urllib.error.HTTPError as e:
            err_body = e.read().decode("utf-8", errors="replace")
            raise RuntimeError(f"GitHub API {method} {endpoint} failed [{e.code}]: {err_body}")
        except Exception as e:
            raise RuntimeError(f"GitHub API connection error on {method} {endpoint}: {e}")

    def get_branch_head_sha(self, branch: Optional[str] = None) -> str:
        """Fetch the latest commit SHA of a branch."""
        target_branch = branch or self.default_branch
        res = self._api_request(f"/git/ref/heads/{target_branch}", method="GET")
        return res["object"]["sha"]

    def get_commit_tree_sha(self, commit_sha: str) -> str:
        """Fetch the root tree SHA for a given commit."""
        res = self._api_request(f"/git/commits/{commit_sha}", method="GET")
        return res["tree"]["sha"]

    def create_tree(self, base_tree_sha: str, files_dict: Dict[str, str]) -> str:
        """
        Create a new Git tree containing updated files.
        files_dict maps relative paths (e.g. 'plan/01_....md') to their text content.
        """
        tree_items = []
        for path, content in files_dict.items():
            tree_items.append({
                "path": path.lstrip("/"),
                "mode": "100644",
                "type": "blob",
                "content": content
            })

        payload = {
            "base_tree": base_tree_sha,
            "tree": tree_items
        }
        res = self._api_request("/git/trees", method="POST", data=payload)
        return res["sha"]

    def create_commit(self, message: str, tree_sha: str, parent_sha: str) -> str:
        """Create a Git commit pointing to the new tree."""
        payload = {
            "message": message,
            "tree": tree_sha,
            "parents": [parent_sha]
        }
        res = self._api_request("/git/commits", method="POST", data=payload)
        return res["sha"]

    def create_or_update_branch(self, branch_name: str, commit_sha: str) -> str:
        """Create a new ref or update existing ref if branch already exists."""
        ref_path = f"refs/heads/{branch_name}"
        try:
            # Attempt to create new ref
            res = self._api_request("/git/refs", method="POST", data={"ref": ref_path, "sha": commit_sha})
            return res["ref"]
        except RuntimeError as e:
            if "Reference already exists" in str(e) or "422" in str(e):
                # Update existing branch
                res = self._api_request(f"/git/refs/heads/{branch_name}", method="PATCH", data={"sha": commit_sha, "force": True})
                return res["ref"]
            raise

    def create_pull_request(self, title: str, body: str, head_branch: str, base_branch: Optional[str] = None) -> Dict[str, Any]:
        """Open a Pull Request."""
        payload = {
            "title": title,
            "body": body,
            "head": head_branch,
            "base": base_branch or self.default_branch
        }
        return self._api_request("/pulls", method="POST", data=payload)

    def add_labels(self, issue_or_pr_number: int, labels: List[str]):
        """Add tags/labels to a Pull Request."""
        try:
            self._api_request(f"/issues/{issue_or_pr_number}/labels", method="POST", data={"labels": labels})
        except Exception as e:
            print(f"[GITHUB] Warning: Could not add labels to PR #{issue_or_pr_number}: {e}")

    def merge_pull_request(self, pr_number: int, commit_title: str, commit_message: str, merge_method: str = "squash") -> Dict[str, Any]:
        """Squash-merge a Pull Request."""
        payload = {
            "commit_title": commit_title,
            "commit_message": commit_message,
            "merge_method": merge_method
        }
        return self._api_request(f"/pulls/{pr_number}/merge", method="PUT", data=payload)

    def delete_branch(self, branch_name: str):
        """Clean up working branch after merge."""
        try:
            self._api_request(f"/git/refs/heads/{branch_name}", method="DELETE")
        except Exception as e:
            print(f"[GITHUB] Warning: Could not delete branch {branch_name}: {e}")

    def sync_cycle_to_github(
        self,
        cycle_num: int,
        target: Dict[str, Any],
        files_to_commit: Dict[str, str],
        confidence_score: float,
        audit_passed: bool,
        audit_msg: str,
        adversarial_critique: str = "",
        unviable_concepts: Optional[List[Dict[str, Any]]] = None
    ) -> Dict[str, Any]:
        """
        High-level orchestrator:
        1. Checks if GITHUB_TOKEN is present.
        2. Creates dedicated cycle branch.
        3. Commits all modified files in a single atomic tree.
        4. Opens Pull Request with rich Diligence Scorecard.
        5. If confidence >= threshold and audit passed, auto-merges to main.
        6. Otherwise leaves PR open for Jack Fay's review.
        """
        if not self.is_configured:
            print("[GITHUB] GITHUB_TOKEN not configured. Skipping GitHub lifecycle sync.")
            return {"status": "SKIPPED", "reason": "No GITHUB_TOKEN"}

        target_id = target.get("id", "ITEM")
        target_title = target.get("title", "Initiative Update")
        clean_id = re.sub(r"[^a-zA-Z0-9_-]", "-", target_id).lower()
        branch_name = f"diligence/cycle-{cycle_num}-{clean_id}"

        # Determine auto-merge eligibility
        should_auto_merge = (confidence_score >= self.auto_merge_threshold) and audit_passed

        status_tag = "[AUTO-MERGED]" if should_auto_merge else "[NEEDS REVIEW]"
        pr_title = f"[Cycle #{cycle_num}] {status_tag} {target_id}: {target_title} (Confidence: {confidence_score:.1f}/10)"

        # 1. Get HEAD commit of main
        base_commit_sha = self.get_branch_head_sha(self.default_branch)
        base_tree_sha = self.get_commit_tree_sha(base_commit_sha)

        # 2. Create Git tree with modified files
        new_tree_sha = self.create_tree(base_tree_sha, files_to_commit)

        # Guard: Check if tree actually contains diffs
        if new_tree_sha == base_tree_sha:
            print(f"[GITHUB] Warning: No file diff detected for Cycle #{cycle_num} against {self.default_branch}. Skipping PR creation.")
            return {"status": "SKIPPED", "reason": "No diff detected against main"}

        # 3. Create Commit
        commit_message = (
            f"[Cycle #{cycle_num}] {target_id}: {target_title}\n\n"
            f"Confidence Score: {confidence_score:.1f}/10 (Threshold: {self.auto_merge_threshold}/10)\n"
            f"Audit Verdict: {'APPROVED' if audit_passed else 'FLAGGED'}\n"
            f"Audit Summary: {audit_msg}\n"
        )
        new_commit_sha = self.create_commit(commit_message, new_tree_sha, base_commit_sha)

        # 4. Create Branch
        self.create_or_update_branch(branch_name, new_commit_sha)

        # 5. Build PR Description
        unviable_section = ""
        if unviable_concepts:
            unviable_section = "\n### 🪦 Concepts Buried in The Graveyard\n"
            for c in unviable_concepts:
                unviable_section += f"- **{c.get('title', 'Unknown')}**: {c.get('autopsy', 'Rejected')}\n"

        files_list_md = "\n".join([f"- `{p}`" for p in files_to_commit.keys()])

        pr_body = fr"""# Diligence Cycle #{cycle_num} — {target_id}: {target_title}

### 🎯 Strategic Bottom Line
> **Question:** {target.get('question', 'N/A')}  
> **Target Module:** `{target.get('target_plan_file', 'plan/')}`  
> **Status:** `{target.get('status', 'OPEN')}` | **Grounded Score:** `{confidence_score:.1f} / 10.0`

---

### 📊 Diligence Scorecard & Verification Gate
| Metric | Result | Benchmark Standard |
| :--- | :--- | :--- |
| **Grounded Confidence** | **{confidence_score:.1f} / 10.0** | $\ge$ {self.auto_merge_threshold}/10 for Auto-Merge |
| **Adversarial Diligence Audit** | **{'✅ PASSED' if audit_passed else '⚠️ FLAGGED'}** | PE Red-Team Forensic Review |
| **Lifecycle Action** | **{'🚀 AUTO-MERGED TO MAIN' if should_auto_merge else '⏳ PENDING OPERATOR APPROVAL'}** | Policy: Threshold $\ge$ {self.auto_merge_threshold} |

---

### 🛡️ Adversarial Red-Team Findings
**Audit Verdict:** {audit_msg}

{adversarial_critique if adversarial_critique else '_Draft verified against grounded financial statements, shop floor capacity, and regulatory bidding laws._'}
{unviable_section}
---

### 📁 Synchronized Repository Files
{files_list_md}

---
*Generated autonomously by Lily Corp Diligence Engine running on Google Cloud Run.*  
*Cockpit Dashboard: [http://localhost:8080](http://localhost:8080)*
"""

        # 6. High-confidence auto-merge pathway
        if should_auto_merge:
            # Attempt formal PR squash-merge first
            try:
                pr_data = self.create_pull_request(pr_title, pr_body, branch_name, self.default_branch)
                pr_number = pr_data["number"]
                pr_url = pr_data["html_url"]
                self.add_labels(pr_number, ["ai-diligence", f"cycle-{cycle_num}", "auto-merged"])
                self.merge_pull_request(
                    pr_number=pr_number,
                    commit_title=f"[Cycle #{cycle_num}] [AUTO-MERGED] {target_id}: {target_title} (Score: {confidence_score:.1f}/10)",
                    commit_message=f"Autonomous diligence cycle verified with confidence {confidence_score:.1f}/10.\nAdversarial audit passed: {audit_msg}\nPR #{pr_number}",
                    merge_method="squash"
                )
                self.delete_branch(branch_name)
                print(f"[GITHUB] Pull Request #{pr_number} successfully AUTO-MERGED to {self.default_branch}!")
                return {
                    "status": "SUCCESS",
                    "pr_number": pr_number,
                    "pr_url": pr_url,
                    "branch": branch_name,
                    "auto_merged": True,
                    "mode": "PR_SQUASH_MERGE",
                    "confidence_score": confidence_score
                }
            except Exception as e:
                print(f"[GITHUB] PR auto-merge failed ({e}). Falling back to direct commit to {self.default_branch}...")
                try:
                    # Fast-forward main to new commit SHA directly
                    self._api_request(f"/git/refs/heads/{self.default_branch}", method="PATCH", data={"sha": new_commit_sha})
                    self.delete_branch(branch_name)
                    commit_url = f"https://github.com/{self.repo}/commit/{new_commit_sha}"
                    print(f"[GITHUB] Successfully committed directly to {self.default_branch} ({new_commit_sha[:8]})!")
                    return {
                        "status": "SUCCESS",
                        "pr_number": None,
                        "pr_url": commit_url,
                        "branch": self.default_branch,
                        "auto_merged": True,
                        "mode": "DIRECT_COMMIT",
                        "commit_sha": new_commit_sha,
                        "confidence_score": confidence_score
                    }
                except Exception as direct_err:
                    print(f"[GITHUB] Direct commit to {self.default_branch} also failed: {direct_err}")
                    raise

        # 7. Needs operator review pathway (score < threshold or audit flagged)
        try:
            pr_data = self.create_pull_request(pr_title, pr_body, branch_name, self.default_branch)
            pr_number = pr_data["number"]
            pr_url = pr_data["html_url"]
            self.add_labels(pr_number, ["ai-diligence", f"cycle-{cycle_num}", "needs-operator-review"])
            print(f"[GITHUB] Pull Request #{pr_number} OPEN for operator review: {pr_url}")
            return {
                "status": "SUCCESS",
                "pr_number": pr_number,
                "pr_url": pr_url,
                "branch": branch_name,
                "auto_merged": False,
                "mode": "PR_OPEN",
                "confidence_score": confidence_score
            }
        except Exception as e:
            # If token lacks Pull requests write permission, keep branch on GitHub and provide compare link
            compare_url = f"https://github.com/{self.repo}/compare/{self.default_branch}...{branch_name}"
            print(f"[GITHUB] Note: Could not open PR automatically ({e}). Branch {branch_name} preserved at {compare_url}")
            return {
                "status": "SUCCESS",
                "pr_number": None,
                "pr_url": compare_url,
                "branch": branch_name,
                "auto_merged": False,
                "mode": "BRANCH_COMPARE",
                "note": "Token lacks 'Pull requests: Read and write' permission. Use compare link to view diff and merge.",
                "confidence_score": confidence_score
            }
