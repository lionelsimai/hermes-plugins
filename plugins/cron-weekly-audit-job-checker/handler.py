"""Handler for Weekly Audit Job Checker (cron-weekly-audit-job-checker). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'analyze', 'items': ['weekly audit job schedule clarity', 'weekly audit job delivery target', 'weekly audit job failure handling', 'weekly audit job idempotency', 'weekly audit job owner named'], 'slug': 'cron-weekly-audit-job-checker', 'name': 'Weekly Audit Job Checker'}
def run(args):
    return run_engine(CONFIG, args or {})
