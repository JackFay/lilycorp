"""
HTTP Entrypoint for Google Cloud Function (2nd gen).
Triggered via Google Cloud Scheduler or direct HTTP POST.
"""

import os
import json
import functions_framework
from flask import jsonify, Request
from diligence_core import run_single_cloud_cycle

@functions_framework.http
def run_diligence_cycle(request: Request):
    """
    HTTP handler triggered by Cloud Scheduler every 10 minutes.
    """
    # Verify request method (allow POST or GET)
    bucket_name = os.environ.get("GCS_BUCKET_NAME")
    if not bucket_name:
        req_json = request.get_json(silent=True)
        if req_json and "bucket_name" in req_json:
            bucket_name = req_json["bucket_name"]
        elif request.args and "bucket_name" in request.args:
            bucket_name = request.args["bucket_name"]

    if not bucket_name:
        return jsonify({
            "error": "Missing GCS_BUCKET_NAME environment variable or query param"
        }), 400

    try:
        result = run_single_cloud_cycle(bucket_name)
        return jsonify({
            "success": True,
            "result": result
        }), 200
    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500
