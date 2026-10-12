#!/usr/bin/env bash
# ==============================================================================
# Deploy Password-Protected Lily Corp Cockpit to Google Cloud Run
# ==============================================================================

set -euo pipefail

PROJECT_ID=${GCP_PROJECT:-"dulcet-voyager-496719-e3"}
REGION=${GCP_REGION:-"us-central1"}
BUCKET_NAME="lilycorp-diligence-${PROJECT_ID}"
SERVICE_NAME="lilycorp-cockpit"

# Load .env
if [ -f .env ]; then
  export $(grep -v '^#' .env | xargs)
fi

PORTAL_USER=${PORTAL_USERNAME:-"jack"}
PORTAL_PASS=${PORTAL_PASSWORD:-"lilycorp2026"}

echo "=========================================================="
echo " Deploying Lily Corp Password-Protected Cockpit to Cloud Run"
echo " Service:    ${SERVICE_NAME}"
echo " Project:    ${PROJECT_ID}"
echo " Region:     ${REGION}"
echo " GCS Bucket: gs://${BUCKET_NAME}"
echo " Username:   ${PORTAL_USER}"
echo "=========================================================="

# Ensure GCS bucket exists
if ! gsutil ls -b "gs://${BUCKET_NAME}" >/dev/null 2>&1; then
  echo "Creating bucket gs://${BUCKET_NAME}..."
  gsutil mb -p "${PROJECT_ID}" -c STANDARD -l "${REGION}" "gs://${BUCKET_NAME}"
fi

# Sync initial generated pages to GCS if any exist locally
if [ -d "portal/generated" ]; then
  echo "Syncing local generated pages to GCS..."
  gsutil -m rsync -r portal/generated "gs://${BUCKET_NAME}/portal/generated" >/dev/null 2>&1 || true
fi

# Deploy to Cloud Run
echo "\nBuilding and deploying Cloud Run service from source..."
gcloud run deploy "${SERVICE_NAME}" \
  --source=. \
  --region="${REGION}" \
  --allow-unauthenticated \
  --memory=1Gi \
  --timeout=300s \
  --set-env-vars="GCS_BUCKET_NAME=${BUCKET_NAME},GCP_PROJECT=${PROJECT_ID},GCP_LOCATION=${REGION},GEMINI_MODEL=${GEMINI_MODEL:-gemini-3.8-flash},GEMINI_API_KEY=${GEMINI_API_KEY},GITHUB_TOKEN=${GITHUB_TOKEN},GITHUB_REPO=${GITHUB_REPO:-JackFay/lilycorp},GITHUB_DEFAULT_BRANCH=${GITHUB_DEFAULT_BRANCH:-main},PORTAL_USERNAME=${PORTAL_USER},PORTAL_PASSWORD=${PORTAL_PASS}"

URL=$(gcloud run services describe "${SERVICE_NAME}" --region="${REGION}" --format="value(status.url)")

echo "\n=========================================================="
echo " COCKPIT WEB APP SUCCESSFULLY DEPLOYED!"
echo " URL:      ${URL}"
echo " Username: ${PORTAL_USER}"
echo " Password: ${PORTAL_PASS}"
echo " Protection: HTTP Basic Auth (prompted natively in browser)"
echo "=========================================================="
