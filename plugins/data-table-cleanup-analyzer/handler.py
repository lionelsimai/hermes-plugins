"""Handler for Table Cleanup Analyzer (data-table-cleanup-analyzer). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'template', 'items': ['table cleanup data completeness', 'table cleanup column consistency', 'table cleanup outliers flagged', 'table cleanup totals verified', 'table cleanup format fit'], 'slug': 'data-table-cleanup-analyzer', 'name': 'Table Cleanup Analyzer'}
def run(args):
    return run_engine(CONFIG, args or {})
