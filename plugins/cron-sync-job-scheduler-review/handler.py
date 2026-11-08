"""Handler for Sync Job Scheduler Review (cron-sync-job-scheduler-review). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'audit', 'items': ['sync job schedule clarity', 'sync job delivery target', 'sync job failure handling', 'sync job idempotency', 'sync job owner named'], 'slug': 'cron-sync-job-scheduler-review', 'name': 'Sync Job Scheduler Review'}
def run(args):
    return run_engine(CONFIG, args or {})
