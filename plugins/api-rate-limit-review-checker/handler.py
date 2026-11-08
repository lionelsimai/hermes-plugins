"""Handler for Rate Limit Review Checker (api-rate-limit-review-checker). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'template', 'items': ['rate limit review contract fit', 'rate limit review auth handled safely', 'rate limit review error cases covered', 'rate limit review rate limits respected', 'rate limit review verification call'], 'slug': 'api-rate-limit-review-checker', 'name': 'Rate Limit Review Checker'}
def run(args):
    return run_engine(CONFIG, args or {})
