"""Handler for Job Failure Review Auditor (cron-job-failure-review-auditor). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'audit', 'items': ['job failure review schedule clarity', 'job failure review delivery target', 'job failure review failure handling', 'job failure review idempotency', 'job failure review owner named'], 'slug': 'cron-job-failure-review-auditor', 'name': 'Job Failure Review Auditor'}
def run(args):
    return run_engine(CONFIG, args or {})
