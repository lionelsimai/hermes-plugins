"""Handler for Table Cleanup Checker (data-table-cleanup-checker). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'analyze', 'items': ['table cleanup data completeness', 'table cleanup column consistency', 'table cleanup outliers flagged', 'table cleanup totals verified', 'table cleanup format fit'], 'slug': 'data-table-cleanup-checker', 'name': 'Table Cleanup Checker'}
def run(args):
    return run_engine(CONFIG, args or {})
