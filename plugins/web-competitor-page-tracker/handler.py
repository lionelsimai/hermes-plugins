"""Handler for Competitor Page Tracker (web-competitor-page-tracker). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'classify', 'items': ['competitor page source quality', 'competitor page recency', 'competitor page corroboration', 'competitor page citation completeness', 'competitor page scope fit'], 'slug': 'web-competitor-page-tracker', 'name': 'Competitor Page Tracker'}
def run(args):
    return run_engine(CONFIG, args or {})
