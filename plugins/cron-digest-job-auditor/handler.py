"""Handler for Digest Job Auditor (cron-digest-job-auditor). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'checklist', 'items': ['digest job schedule clarity', 'digest job delivery target', 'digest job failure handling', 'digest job idempotency', 'digest job owner named'], 'slug': 'cron-digest-job-auditor', 'name': 'Digest Job Auditor'}
def run(args):
    return run_engine(CONFIG, args or {})
