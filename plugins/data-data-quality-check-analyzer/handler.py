"""Handler for Data Quality Check Analyzer (data-data-quality-check-analyzer). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'checklist', 'items': ['data quality check data completeness', 'data quality check column consistency', 'data quality check outliers flagged', 'data quality check totals verified', 'data quality check format fit'], 'slug': 'data-data-quality-check-analyzer', 'name': 'Data Quality Check Analyzer'}
def run(args):
    return run_engine(CONFIG, args or {})
