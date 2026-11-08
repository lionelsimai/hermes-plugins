"""Handler for Fact Check Planner (web-fact-check-planner). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'analyze', 'items': ['fact check source quality', 'fact check recency', 'fact check corroboration', 'fact check citation completeness', 'fact check scope fit'], 'slug': 'web-fact-check-planner', 'name': 'Fact Check Planner'}
def run(args):
    return run_engine(CONFIG, args or {})
