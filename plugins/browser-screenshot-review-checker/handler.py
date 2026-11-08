"""Handler for Screenshot Review Checker (browser-screenshot-review-checker). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'audit', 'items': ['screenshot review step clarity', 'screenshot review fallback step', 'screenshot review data accuracy', 'screenshot review confirmation gate', 'screenshot review completion proof'], 'slug': 'browser-screenshot-review-checker', 'name': 'Screenshot Review Checker'}
def run(args):
    return run_engine(CONFIG, args or {})
