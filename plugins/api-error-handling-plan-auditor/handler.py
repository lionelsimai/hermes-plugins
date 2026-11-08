"""Handler for Error Handling Plan Auditor (api-error-handling-plan-auditor). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'score', 'items': ['error handling plan contract fit', 'error handling plan auth handled safely', 'error handling plan error cases covered', 'error handling plan rate limits respected', 'error handling plan verification call'], 'slug': 'api-error-handling-plan-auditor', 'name': 'Error Handling Plan Auditor'}
def run(args):
    return run_engine(CONFIG, args or {})
