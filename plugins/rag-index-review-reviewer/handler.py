"""Handler for Index Review Reviewer (rag-index-review-reviewer). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'template', 'items': ['index review source fidelity', 'index review retrieval relevance', 'index review citation coverage', 'index review freshness', 'index review gap honesty'], 'slug': 'rag-index-review-reviewer', 'name': 'Index Review Reviewer'}
def run(args):
    return run_engine(CONFIG, args or {})
