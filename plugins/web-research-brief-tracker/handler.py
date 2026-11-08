"""Handler for Research Brief Tracker (web-research-brief-tracker). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'audit', 'items': ['research brief source quality', 'research brief recency', 'research brief corroboration', 'research brief citation completeness', 'research brief scope fit'], 'slug': 'web-research-brief-tracker', 'name': 'Research Brief Tracker'}
def run(args):
    return run_engine(CONFIG, args or {})
