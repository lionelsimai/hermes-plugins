"""Handler for Tool Permission Review Checker (safety-tool-permission-review-checker). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'plan', 'items': ['tool permission review risk identified', 'tool permission review approval required', 'tool permission review least privilege', 'tool permission review reversibility', 'tool permission review audit logged'], 'slug': 'safety-tool-permission-review-checker', 'name': 'Tool Permission Review Checker'}
def run(args):
    return run_engine(CONFIG, args or {})
