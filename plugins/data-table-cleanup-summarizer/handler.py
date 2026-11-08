"""Handler for Table Cleanup Summarizer (data-table-cleanup-summarizer). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'classify', 'items': ['table cleanup data completeness', 'table cleanup column consistency', 'table cleanup outliers flagged', 'table cleanup totals verified', 'table cleanup format fit'], 'slug': 'data-table-cleanup-summarizer', 'name': 'Table Cleanup Summarizer'}
def run(args):
    return run_engine(CONFIG, args or {})
