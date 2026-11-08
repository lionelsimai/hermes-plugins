"""Handler for Search Query Set Extractor (web-search-query-set-extractor). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'audit', 'items': ['search query set source quality', 'search query set recency', 'search query set corroboration', 'search query set citation completeness', 'search query set scope fit'], 'slug': 'web-search-query-set-extractor', 'name': 'Search Query Set Extractor'}
def run(args):
    return run_engine(CONFIG, args or {})
