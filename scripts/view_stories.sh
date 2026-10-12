#!/usr/bin/env bash
# Quick launcher to open the Lily Corp Educational Stories in your default browser.
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
STORIES_HTML="$SCRIPT_DIR/../stories/index.html"

echo "=========================================================="
echo "  Launching Lily Corp Operator Stories (ELI5 Edition)     "
echo "=========================================================="
open "$STORIES_HTML"
echo "Opened in your default browser: $STORIES_HTML"
