"""Handler for Rest Endpoint Test Auditor (api-rest-endpoint-test-auditor). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'audit', 'items': ['rest endpoint test contract fit', 'rest endpoint test auth handled safely', 'rest endpoint test error cases covered', 'rest endpoint test rate limits respected', 'rest endpoint test verification call'], 'slug': 'api-rest-endpoint-test-auditor', 'name': 'Rest Endpoint Test Auditor'}
def run(args):
    return run_engine(CONFIG, args or {})
