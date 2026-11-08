"""Handler for Digest Job Reporter (cron-digest-job-reporter). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'classify', 'items': ['digest job schedule clarity', 'digest job delivery target', 'digest job failure handling', 'digest job idempotency', 'digest job owner named'], 'slug': 'cron-digest-job-reporter', 'name': 'Digest Job Reporter'}
def run(args):
    return run_engine(CONFIG, args or {})
