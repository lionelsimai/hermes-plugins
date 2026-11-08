"""Handler for Index Review Planner (rag-index-review-planner). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'score', 'items': ['index review source fidelity', 'index review retrieval relevance', 'index review citation coverage', 'index review freshness', 'index review gap honesty'], 'slug': 'rag-index-review-planner', 'name': 'Index Review Planner'}
def run(args):
    return run_engine(CONFIG, args or {})
