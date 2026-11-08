"""Handler for Kpi Table Planner (data-kpi-table-planner). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'analyze', 'items': ['kpi table data completeness', 'kpi table column consistency', 'kpi table outliers flagged', 'kpi table totals verified', 'kpi table format fit'], 'slug': 'data-kpi-table-planner', 'name': 'Kpi Table Planner'}
def run(args):
    return run_engine(CONFIG, args or {})
