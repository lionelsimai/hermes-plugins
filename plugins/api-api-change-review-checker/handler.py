"""Handler for Api Change Review Checker (api-api-change-review-checker). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'analyze', 'items': ['api change review contract fit', 'api change review auth handled safely', 'api change review error cases covered', 'api change review rate limits respected', 'api change review verification call'], 'slug': 'api-api-change-review-checker', 'name': 'Api Change Review Checker'}
def run(args):
    return run_engine(CONFIG, args or {})
