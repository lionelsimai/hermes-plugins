"""Handler for Chart Brief Summarizer (data-chart-brief-summarizer). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'plan', 'items': ['chart brief data completeness', 'chart brief column consistency', 'chart brief outliers flagged', 'chart brief totals verified', 'chart brief format fit'], 'slug': 'data-chart-brief-summarizer', 'name': 'Chart Brief Summarizer'}
def run(args):
    return run_engine(CONFIG, args or {})
