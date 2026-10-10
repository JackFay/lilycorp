"""
Google Cloud Storage Adapter for Lily Corp Diligence Engine.
Manages reading and writing state, evidence, steering notes, and plan modules in GCS.
"""

import json
import os
from typing import Dict, Any, List, Optional
from google.cloud import storage

class GCSStorageAdapter:
    def __init__(self, bucket_name: Optional[str] = None):
        self.bucket_name = bucket_name or os.environ.get("GCS_BUCKET_NAME", "lilycorp-diligence-engine")
        self.client = storage.Client()
        self.bucket = self.client.bucket(self.bucket_name)

    def read_text(self, path: str) -> str:
        """Read a text file from GCS. Returns empty string if not found."""
        blob = self.bucket.blob(path.lstrip("/"))
        if not blob.exists():
            return ""
        return blob.download_as_text()

    def write_text(self, path: str, content: str, content_type: str = "text/plain"):
        """Write text content to GCS."""
        blob = self.bucket.blob(path.lstrip("/"))
        blob.upload_from_string(content, content_type=content_type)

    def read_json(self, path: str) -> Optional[Dict[str, Any]]:
        """Read and parse JSON from GCS."""
        text = self.read_text(path)
        if not text:
            return None
        return json.loads(text)

    def write_json(self, path: str, data: Dict[str, Any]):
        """Write JSON data to GCS."""
        content = json.dumps(data, indent=2)
        self.write_text(path, content, content_type="application/json")

    def list_files(self, prefix: str) -> List[str]:
        """List all object paths matching a prefix."""
        blobs = self.client.list_blobs(self.bucket, prefix=prefix.lstrip("/"))
        return [blob.name for blob in blobs]
