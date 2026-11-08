"""Handler for Rest Endpoint Test Checker (api-rest-endpoint-test-checker). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'plan', 'items': ['rest endpoint test contract fit', 'rest endpoint test auth handled safely', 'rest endpoint test error cases covered', 'rest endpoint test rate limits respected', 'rest endpoint test verification call'], 'slug': 'api-rest-endpoint-test-checker', 'name': 'Rest Endpoint Test Checker'}
def run(args):
    return run_engine(CONFIG, args or {})
