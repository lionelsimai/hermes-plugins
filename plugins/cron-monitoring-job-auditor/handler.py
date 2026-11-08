"""Handler for Monitoring Job Auditor (cron-monitoring-job-auditor). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'classify', 'items': ['monitoring job schedule clarity', 'monitoring job delivery target', 'monitoring job failure handling', 'monitoring job idempotency', 'monitoring job owner named'], 'slug': 'cron-monitoring-job-auditor', 'name': 'Monitoring Job Auditor'}
def run(args):
    return run_engine(CONFIG, args or {})
