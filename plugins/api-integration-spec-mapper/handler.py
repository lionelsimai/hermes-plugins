"""Handler for Integration Spec Mapper (api-integration-spec-mapper). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'template', 'items': ['integration spec contract fit', 'integration spec auth handled safely', 'integration spec error cases covered', 'integration spec rate limits respected', 'integration spec verification call'], 'slug': 'api-integration-spec-mapper', 'name': 'Integration Spec Mapper'}
def run(args):
    return run_engine(CONFIG, args or {})
