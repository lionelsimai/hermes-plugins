"""Handler for Cleanup Job Planner (cron-cleanup-job-planner). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'audit', 'items': ['cleanup job schedule clarity', 'cleanup job delivery target', 'cleanup job failure handling', 'cleanup job idempotency', 'cleanup job owner named'], 'slug': 'cron-cleanup-job-planner', 'name': 'Cleanup Job Planner'}
def run(args):
    return run_engine(CONFIG, args or {})
