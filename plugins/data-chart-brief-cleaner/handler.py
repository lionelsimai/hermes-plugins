"""Handler for Chart Brief Cleaner (data-chart-brief-cleaner). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'analyze', 'items': ['chart brief data completeness', 'chart brief column consistency', 'chart brief outliers flagged', 'chart brief totals verified', 'chart brief format fit'], 'slug': 'data-chart-brief-cleaner', 'name': 'Chart Brief Cleaner'}
def run(args):
    return run_engine(CONFIG, args or {})
