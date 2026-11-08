"""Handler for Faq Draft Planner (rag-faq-draft-planner). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'classify', 'items': ['faq draft source fidelity', 'faq draft retrieval relevance', 'faq draft citation coverage', 'faq draft freshness', 'faq draft gap honesty'], 'slug': 'rag-faq-draft-planner', 'name': 'Faq Draft Planner'}
def run(args):
    return run_engine(CONFIG, args or {})
