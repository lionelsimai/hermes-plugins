"""Handler for Budget Tracker Analyzer (data-budget-tracker-analyzer). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'analyze', 'items': ['budget tracker data completeness', 'budget tracker column consistency', 'budget tracker outliers flagged', 'budget tracker totals verified', 'budget tracker format fit'], 'slug': 'data-budget-tracker-analyzer', 'name': 'Budget Tracker Analyzer'}
def run(args):
    return run_engine(CONFIG, args or {})
