"""Handler for Sync Job Planner (cron-sync-job-planner). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'template', 'items': ['sync job schedule clarity', 'sync job delivery target', 'sync job failure handling', 'sync job idempotency', 'sync job owner named'], 'slug': 'cron-sync-job-planner', 'name': 'Sync Job Planner'}
def run(args):
    return run_engine(CONFIG, args or {})
