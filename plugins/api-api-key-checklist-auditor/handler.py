"""Handler for Api Key Checklist Auditor (api-api-key-checklist-auditor). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'prioritize', 'items': ['api key checklist contract fit', 'api key checklist auth handled safely', 'api key checklist error cases covered', 'api key checklist rate limits respected', 'api key checklist verification call'], 'slug': 'api-api-key-checklist-auditor', 'name': 'Api Key Checklist Auditor'}
def run(args):
    return run_engine(CONFIG, args or {})
