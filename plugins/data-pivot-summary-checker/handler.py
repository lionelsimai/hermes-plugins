"""Handler for Pivot Summary Checker (data-pivot-summary-checker). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'score', 'items': ['pivot summary data completeness', 'pivot summary column consistency', 'pivot summary outliers flagged', 'pivot summary totals verified', 'pivot summary format fit'], 'slug': 'data-pivot-summary-checker', 'name': 'Pivot Summary Checker'}
def run(args):
    return run_engine(CONFIG, args or {})
