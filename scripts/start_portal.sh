#!/usr/bin/env bash
# ==============================================================================
# Start Lily Corp Diligence Cockpit & AI Page Generator
# ==============================================================================

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"

cd "${ROOT_DIR}"

PYTHON_BIN="${ROOT_DIR}/engine/.venv/bin/python"

if [ ! -f "${PYTHON_BIN}" ]; then
  echo "Error: Python venv not found at ${PYTHON_BIN}"
  exit 1
fi

PORT="${PORT:-8080}"
echo "=========================================================="
echo " Starting Lily Corp Cockpit & AI Page Generator on port ${PORT}"
echo " URL: http://localhost:${PORT}"
echo "=========================================================="

exec "${PYTHON_BIN}" portal/server.py
