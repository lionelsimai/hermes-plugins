"""Handler for Oauth Flow Check Checker (api-oauth-flow-check-checker). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'prioritize', 'items': ['oauth flow check contract fit', 'oauth flow check auth handled safely', 'oauth flow check error cases covered', 'oauth flow check rate limits respected', 'oauth flow check verification call'], 'slug': 'api-oauth-flow-check-checker', 'name': 'Oauth Flow Check Checker'}
def run(args):
    return run_engine(CONFIG, args or {})
