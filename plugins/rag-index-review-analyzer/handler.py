"""Handler for Index Review Analyzer (rag-index-review-analyzer). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'classify', 'items': ['index review source fidelity', 'index review retrieval relevance', 'index review citation coverage', 'index review freshness', 'index review gap honesty'], 'slug': 'rag-index-review-analyzer', 'name': 'Index Review Analyzer'}
def run(args):
    return run_engine(CONFIG, args or {})
