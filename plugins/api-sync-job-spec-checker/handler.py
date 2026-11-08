"""Handler for Sync Job Spec Checker (api-sync-job-spec-checker). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'plan', 'items': ['sync job spec contract fit', 'sync job spec auth handled safely', 'sync job spec error cases covered', 'sync job spec rate limits respected', 'sync job spec verification call'], 'slug': 'api-sync-job-spec-checker', 'name': 'Sync Job Spec Checker'}
def run(args):
    return run_engine(CONFIG, args or {})
