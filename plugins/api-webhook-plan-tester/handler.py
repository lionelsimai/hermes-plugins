"""Handler for Webhook Plan Tester (api-webhook-plan-tester). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'prioritize', 'items': ['webhook plan contract fit', 'webhook plan auth handled safely', 'webhook plan error cases covered', 'webhook plan rate limits respected', 'webhook plan verification call'], 'slug': 'api-webhook-plan-tester', 'name': 'Webhook Plan Tester'}
def run(args):
    return run_engine(CONFIG, args or {})
