"""Handler for Chart Brief Analyzer (data-chart-brief-analyzer). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'classify', 'items': ['chart brief data completeness', 'chart brief column consistency', 'chart brief outliers flagged', 'chart brief totals verified', 'chart brief format fit'], 'slug': 'data-chart-brief-analyzer', 'name': 'Chart Brief Analyzer'}
def run(args):
    return run_engine(CONFIG, args or {})
