"""Handler for Screenshot Review Planner (browser-screenshot-review-planner). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'classify', 'items': ['screenshot review step clarity', 'screenshot review fallback step', 'screenshot review data accuracy', 'screenshot review confirmation gate', 'screenshot review completion proof'], 'slug': 'browser-screenshot-review-planner', 'name': 'Screenshot Review Planner'}
def run(args):
    return run_engine(CONFIG, args or {})
