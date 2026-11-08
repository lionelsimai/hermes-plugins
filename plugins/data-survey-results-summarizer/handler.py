"""Handler for Survey Results Summarizer (data-survey-results-summarizer). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'score', 'items': ['survey results data completeness', 'survey results column consistency', 'survey results outliers flagged', 'survey results totals verified', 'survey results format fit'], 'slug': 'data-survey-results-summarizer', 'name': 'Survey Results Summarizer'}
def run(args):
    return run_engine(CONFIG, args or {})
