"""Handler for Page Extraction Tracker (web-page-extraction-tracker). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'template', 'items': ['page extraction source quality', 'page extraction recency', 'page extraction corroboration', 'page extraction citation completeness', 'page extraction scope fit'], 'slug': 'web-page-extraction-tracker', 'name': 'Page Extraction Tracker'}
def run(args):
    return run_engine(CONFIG, args or {})
