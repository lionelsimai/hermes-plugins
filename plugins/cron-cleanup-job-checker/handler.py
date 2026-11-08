"""Handler for Cleanup Job Checker (cron-cleanup-job-checker). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'prioritize', 'items': ['cleanup job schedule clarity', 'cleanup job delivery target', 'cleanup job failure handling', 'cleanup job idempotency', 'cleanup job owner named'], 'slug': 'cron-cleanup-job-checker', 'name': 'Cleanup Job Checker'}
def run(args):
    return run_engine(CONFIG, args or {})
