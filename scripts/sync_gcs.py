#!/usr/bin/env python3
"""
GCS Synchronization Utility for Lily Corp Autonomous Diligence Engine.
Synchronizes evidence, plans, state, and steering notes between local workspace and GCS.
"""

import os
import sys
import argparse
from pathlib import Path
from google.cloud import storage

BASE_DIR = Path(__file__).resolve().parent.parent

def load_env():
    env_file = BASE_DIR / ".env"
    if env_file.exists():
        with open(env_file, "r") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    k, v = line.split("=", 1)
                    os.environ.setdefault(k.strip(), v.strip())

def get_bucket():
    load_env()
    project = os.environ.get("GCP_PROJECT", "dulcet-voyager-496719-e3")
    bucket_name = os.environ.get("GCS_BUCKET_NAME", f"lilycorp-diligence-{project}")
    client = storage.Client(project=project)
    bucket = client.bucket(bucket_name)
    return client, bucket, bucket_name

def upload_directory(bucket, local_dir: Path, gcs_prefix: str):
    if not local_dir.exists():
        return
    for path in local_dir.rglob("*"):
        if path.is_file() and not path.name.startswith(".") and "venv" not in str(path) and "__pycache__" not in str(path):
            rel_path = path.relative_to(local_dir)
            blob_name = f"{gcs_prefix}/{rel_path}".replace("\\", "/")
            blob = bucket.blob(blob_name)
            blob.upload_from_filename(str(path))
            print(f"Uploaded: {path.relative_to(BASE_DIR)} -> gs://{bucket.name}/{blob_name}")

def download_directory(bucket, gcs_prefix: str, local_dir: Path):
    local_dir.mkdir(parents=True, exist_ok=True)
    blobs = bucket.list_blobs(prefix=gcs_prefix.lstrip("/"))
    count = 0
    for blob in blobs:
        if blob.name.endswith("/"):
            continue
        rel_path = blob.name[len(gcs_prefix):].lstrip("/")
        dest_path = local_dir / rel_path
        dest_path.parent.mkdir(parents=True, exist_ok=True)
        blob.download_to_filename(str(dest_path))
        print(f"Downloaded: gs://{bucket.name}/{blob.name} -> {dest_path.relative_to(BASE_DIR)}")
        count += 1
    if count == 0:
        print(f"No files found under gs://{bucket.name}/{gcs_prefix}")

def main():
    parser = argparse.ArgumentParser(description="Sync Lily Corp state with Google Cloud Storage")
    parser.add_argument("action", choices=["init", "push", "pull", "status"], help="Action to perform")
    args = parser.parse_args()

    client, bucket, bucket_name = get_bucket()

    if args.action == "init":
        print(f"Initializing GCS bucket gs://{bucket_name}...")
        if not bucket.exists():
            bucket.create(location="us-central1")
            print(f"Created bucket gs://{bucket_name}")
        else:
            print(f"Bucket gs://{bucket_name} already exists.")
        
        print("\nUploading evidence/...")
        upload_directory(bucket, BASE_DIR / "evidence", "evidence")
        print("\nUploading state/...")
        upload_directory(bucket, BASE_DIR / "state", "state")
        print("\nUploading steering/...")
        upload_directory(bucket, BASE_DIR / "steering", "steering")
        print("\nUploading plan/...")
        upload_directory(bucket, BASE_DIR / "plan", "plan")
        print("\nInit complete! GCS is ready for Cloud Function runs.")

    elif args.action == "push":
        print(f"Pushing local steering notes and state to gs://{bucket_name}...")
        upload_directory(bucket, BASE_DIR / "steering", "steering")
        upload_directory(bucket, BASE_DIR / "state", "state")
        print("Push complete.")

    elif args.action == "pull":
        print(f"Pulling latest plan, state, and digest from gs://{bucket_name}...")
        download_directory(bucket, "plan", BASE_DIR / "plan")
        download_directory(bucket, "state", BASE_DIR / "state")
        download_directory(bucket, "steering", BASE_DIR / "steering")
        print("Pull complete. Local files updated.")

    elif args.action == "status":
        print(f"Bucket: gs://{bucket_name}")
        blobs = list(client.list_blobs(bucket))
        print(f"Total objects in bucket: {len(blobs)}")
        for blob in blobs[:20]:
            print(f" - {blob.name} ({blob.size} bytes)")
        if len(blobs) > 20:
            print(f" ... and {len(blobs) - 20} more.")

if __name__ == "__main__":
    main()
