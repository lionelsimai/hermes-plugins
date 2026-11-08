"""Handler for Faq Draft Reviewer (rag-faq-draft-reviewer). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'plan', 'items': ['faq draft source fidelity', 'faq draft retrieval relevance', 'faq draft citation coverage', 'faq draft freshness', 'faq draft gap honesty'], 'slug': 'rag-faq-draft-reviewer', 'name': 'Faq Draft Reviewer'}
def run(args):
    return run_engine(CONFIG, args or {})
