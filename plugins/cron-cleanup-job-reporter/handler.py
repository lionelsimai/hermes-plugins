"""Handler for Cleanup Job Reporter (cron-cleanup-job-reporter). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'checklist', 'items': ['cleanup job schedule clarity', 'cleanup job delivery target', 'cleanup job failure handling', 'cleanup job idempotency', 'cleanup job owner named'], 'slug': 'cron-cleanup-job-reporter', 'name': 'Cleanup Job Reporter'}
def run(args):
    return run_engine(CONFIG, args or {})
