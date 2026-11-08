"""Handler for Index Review Drafter (rag-index-review-drafter). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'analyze', 'items': ['index review source fidelity', 'index review retrieval relevance', 'index review citation coverage', 'index review freshness', 'index review gap honesty'], 'slug': 'rag-index-review-drafter', 'name': 'Index Review Drafter'}
def run(args):
    return run_engine(CONFIG, args or {})
