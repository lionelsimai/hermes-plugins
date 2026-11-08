"""Handler for Merge Plan Checker (data-merge-plan-checker). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'plan', 'items': ['merge plan data completeness', 'merge plan column consistency', 'merge plan outliers flagged', 'merge plan totals verified', 'merge plan format fit'], 'slug': 'data-merge-plan-checker', 'name': 'Merge Plan Checker'}
def run(args):
    return run_engine(CONFIG, args or {})
