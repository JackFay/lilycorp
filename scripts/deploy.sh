#!/usr/bin/env bash
set -e

# Configuration
PROJECT_ID=${GCP_PROJECT:-"dulcet-voyager-496719-e3"}
REGION=${GCP_REGION:-"us-central1"}
BUCKET_NAME="lilycorp-diligence-${PROJECT_ID}"
FUNCTION_NAME="lilycorp-diligence-engine"
SCHEDULER_JOB_NAME="lilycorp-diligence-cron"
SCHEDULE_CRON="*/15 * * * *" # Every 15 minutes

echo "======================================================="
echo "Deploying Lily Corp Diligence Engine to Google Cloud"
echo "Project:    ${PROJECT_ID}"
echo "Region:     ${REGION}"
echo "GCS Bucket: gs://${BUCKET_NAME}"
echo "Schedule:   ${SCHEDULE_CRON}"
echo "======================================================="

# Load .env if present
if [ -f .env ]; then
  export $(grep -v '^#' .env | xargs)
fi

# 1. Set GCloud Project
gcloud config set project "${PROJECT_ID}"

# 2. Enable Required Google Cloud APIs
echo "\nEnabling necessary APIs (Cloud Functions, Cloud Build, Cloud Storage, Cloud Scheduler, Vertex AI)..."
gcloud services enable \
  cloudfunctions.googleapis.com \
  cloudbuild.googleapis.com \
  run.googleapis.com \
  storage.googleapis.com \
  cloudscheduler.googleapis.com \
  aiplatform.googleapis.com

# 3. Create GCS Storage Bucket if not exists
echo "\nEnsuring GCS bucket exists..."
if ! gsutil ls -b "gs://${BUCKET_NAME}" >/dev/null 2>&1; then
  gsutil mb -p "${PROJECT_ID}" -c STANDARD -l "${REGION}" "gs://${BUCKET_NAME}"
  echo "Created bucket gs://${BUCKET_NAME}"
else
  echo "Bucket gs://${BUCKET_NAME} already exists."
fi

# Ensure Compute SA has Storage Object Admin permissions
PROJECT_NUMBER=$(gcloud projects describe "${PROJECT_ID}" --format="value(projectNumber)")
COMPUTE_SA="${PROJECT_NUMBER}-compute@developer.gserviceaccount.com"
echo "Granting Storage Object Admin to ${COMPUTE_SA}..."
gcloud projects add-iam-policy-binding "${PROJECT_ID}" \
  --member="serviceAccount:${COMPUTE_SA}" \
  --role="roles/storage.objectAdmin" >/dev/null 2>&1 || true

# 4. Upload Initial Evidence, State, and Plan to GCS
echo "\nUploading repository evidence, state, and steering to GCS..."
engine/.venv/bin/python scripts/sync_gcs.py init

# 5. Create Service Account for Cloud Scheduler Invocation
echo "\nConfiguring Invoker Service Account..."
SA_NAME="lilycorp-scheduler-invoker"
SA_EMAIL="${SA_NAME}@${PROJECT_ID}.iam.gserviceaccount.com"

if ! gcloud iam service-accounts describe "${SA_EMAIL}" >/dev/null 2>&1; then
  gcloud iam service-accounts create "${SA_NAME}" \
    --display-name="Lily Corp Scheduler Invoker"
  echo "Created service account: ${SA_EMAIL}"
fi

# 6. Deploy Cloud Function (2nd Gen)
echo "\nDeploying Cloud Function (2nd Gen)..."
gcloud functions deploy "${FUNCTION_NAME}" \
  --gen2 \
  --runtime=python312 \
  --region="${REGION}" \
  --source=./cloud_function \
  --entry-point=run_diligence_cycle \
  --trigger-http \
  --no-allow-unauthenticated \
  --memory=512MiB \
  --timeout=540s \
  --set-env-vars="GCS_BUCKET_NAME=${BUCKET_NAME},GCP_PROJECT=${PROJECT_ID},GCP_LOCATION=${REGION},GEMINI_MODEL=gemini-3.8-flash,GEMINI_API_KEY=${GEMINI_API_KEY},GITHUB_TOKEN=${GITHUB_TOKEN},GITHUB_REPO=${GITHUB_REPO:-JackFay/lilycorp},GITHUB_DEFAULT_BRANCH=${GITHUB_DEFAULT_BRANCH:-main},GITHUB_AUTO_MERGE_THRESHOLD=${GITHUB_AUTO_MERGE_THRESHOLD:-7.5}"

# Get Function URL
FUNCTION_URL=$(gcloud functions describe "${FUNCTION_NAME}" --gen2 --region="${REGION}" --format="value(serviceConfig.uri)")
echo "Function deployed at: ${FUNCTION_URL}"

# Grant Invoker Role to Service Account
echo "\nGranting invoker permissions..."
gcloud run services add-iam-policy-binding "${FUNCTION_NAME}" \
  --region="${REGION}" \
  --member="serviceAccount:${SA_EMAIL}" \
  --role="roles/run.invoker"

# 7. Configure Cloud Scheduler Job
echo "\nConfiguring Cloud Scheduler (Trigger every 10 minutes)..."
if gcloud scheduler jobs describe "${SCHEDULER_JOB_NAME}" --location="${REGION}" >/dev/null 2>&1; then
  gcloud scheduler jobs update http "${SCHEDULER_JOB_NAME}" \
    --location="${REGION}" \
    --schedule="${SCHEDULE_CRON}" \
    --uri="${FUNCTION_URL}" \
    --http-method=POST \
    --oidc-service-account-email="${SA_EMAIL}" \
    --oidc-token-audience="${FUNCTION_URL}"
  echo "Updated existing Cloud Scheduler job: ${SCHEDULER_JOB_NAME}"
else
  gcloud scheduler jobs create http "${SCHEDULER_JOB_NAME}" \
    --location="${REGION}" \
    --schedule="${SCHEDULE_CRON}" \
    --uri="${FUNCTION_URL}" \
    --http-method=POST \
    --oidc-service-account-email="${SA_EMAIL}" \
    --oidc-token-audience="${FUNCTION_URL}"
  echo "Created new Cloud Scheduler job: ${SCHEDULER_JOB_NAME}"
fi

echo "\n======================================================="
echo "DEPLOYMENT COMPLETE!"
echo "Function:  ${FUNCTION_NAME}"
echo "URL:       ${FUNCTION_URL}"
echo "Scheduler: ${SCHEDULER_JOB_NAME} (${SCHEDULE_CRON})"
echo "GCS State: gs://${BUCKET_NAME}"
echo "======================================================="
