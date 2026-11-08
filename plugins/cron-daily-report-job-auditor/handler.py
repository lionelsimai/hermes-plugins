"""Handler for Daily Report Job Auditor (cron-daily-report-job-auditor). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'score', 'items': ['daily report job schedule clarity', 'daily report job delivery target', 'daily report job failure handling', 'daily report job idempotency', 'daily report job owner named'], 'slug': 'cron-daily-report-job-auditor', 'name': 'Daily Report Job Auditor'}
def run(args):
    return run_engine(CONFIG, args or {})
