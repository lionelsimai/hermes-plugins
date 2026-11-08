"""Handler for Outlier Review Cleaner (data-outlier-review-cleaner). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'checklist', 'items': ['outlier review data completeness', 'outlier review column consistency', 'outlier review outliers flagged', 'outlier review totals verified', 'outlier review format fit'], 'slug': 'data-outlier-review-cleaner', 'name': 'Outlier Review Cleaner'}
def run(args):
    return run_engine(CONFIG, args or {})
