"""Handler for Monitoring Job Scheduler Review (cron-monitoring-job-scheduler-review). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'plan', 'items': ['monitoring job schedule clarity', 'monitoring job delivery target', 'monitoring job failure handling', 'monitoring job idempotency', 'monitoring job owner named'], 'slug': 'cron-monitoring-job-scheduler-review', 'name': 'Monitoring Job Scheduler Review'}
def run(args):
    return run_engine(CONFIG, args or {})
