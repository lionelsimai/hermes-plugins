"""Handler for Health Report Summarizer (community-health-report-summarizer). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'score', 'items': ['health report member fit', 'health report tone fit', 'health report approval gate', 'health report safety check', 'health report follow up named'], 'slug': 'community-health-report-summarizer', 'name': 'Health Report Summarizer'}
def run(args):
    return run_engine(CONFIG, args or {})
