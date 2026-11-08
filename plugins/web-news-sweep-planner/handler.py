"""Handler for News Sweep Planner (web-news-sweep-planner). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'audit', 'items': ['news sweep source quality', 'news sweep recency', 'news sweep corroboration', 'news sweep citation completeness', 'news sweep scope fit'], 'slug': 'web-news-sweep-planner', 'name': 'News Sweep Planner'}
def run(args):
    return run_engine(CONFIG, args or {})
