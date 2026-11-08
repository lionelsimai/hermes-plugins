"""Handler for Chart Brief Planner (data-chart-brief-planner). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'prioritize', 'items': ['chart brief data completeness', 'chart brief column consistency', 'chart brief outliers flagged', 'chart brief totals verified', 'chart brief format fit'], 'slug': 'data-chart-brief-planner', 'name': 'Chart Brief Planner'}
def run(args):
    return run_engine(CONFIG, args or {})
