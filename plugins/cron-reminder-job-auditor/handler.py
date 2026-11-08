"""Handler for Reminder Job Auditor (cron-reminder-job-auditor). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'prioritize', 'items': ['reminder job schedule clarity', 'reminder job delivery target', 'reminder job failure handling', 'reminder job idempotency', 'reminder job owner named'], 'slug': 'cron-reminder-job-auditor', 'name': 'Reminder Job Auditor'}
def run(args):
    return run_engine(CONFIG, args or {})
