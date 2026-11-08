"""Handler for Rate Limit Review Planner (api-rate-limit-review-planner). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'prioritize', 'items': ['rate limit review contract fit', 'rate limit review auth handled safely', 'rate limit review error cases covered', 'rate limit review rate limits respected', 'rate limit review verification call'], 'slug': 'api-rate-limit-review-planner', 'name': 'Rate Limit Review Planner'}
def run(args):
    return run_engine(CONFIG, args or {})
