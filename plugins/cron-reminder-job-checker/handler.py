"""Handler for Reminder Job Checker (cron-reminder-job-checker). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'score', 'items': ['reminder job schedule clarity', 'reminder job delivery target', 'reminder job failure handling', 'reminder job idempotency', 'reminder job owner named'], 'slug': 'cron-reminder-job-checker', 'name': 'Reminder Job Checker'}
def run(args):
    return run_engine(CONFIG, args or {})
