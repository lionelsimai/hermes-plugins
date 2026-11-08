"""Handler for Kpi Table Checker (data-kpi-table-checker). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'checklist', 'items': ['kpi table data completeness', 'kpi table column consistency', 'kpi table outliers flagged', 'kpi table totals verified', 'kpi table format fit'], 'slug': 'data-kpi-table-checker', 'name': 'Kpi Table Checker'}
def run(args):
    return run_engine(CONFIG, args or {})
