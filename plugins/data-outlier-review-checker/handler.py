"""Handler for Outlier Review Checker (data-outlier-review-checker). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'analyze', 'items': ['outlier review data completeness', 'outlier review column consistency', 'outlier review outliers flagged', 'outlier review totals verified', 'outlier review format fit'], 'slug': 'data-outlier-review-checker', 'name': 'Outlier Review Checker'}
def run(args):
    return run_engine(CONFIG, args or {})
