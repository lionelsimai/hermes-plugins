"""Handler for Api Change Review Planner (api-api-change-review-planner). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'score', 'items': ['api change review contract fit', 'api change review auth handled safely', 'api change review error cases covered', 'api change review rate limits respected', 'api change review verification call'], 'slug': 'api-api-change-review-planner', 'name': 'Api Change Review Planner'}
def run(args):
    return run_engine(CONFIG, args or {})
