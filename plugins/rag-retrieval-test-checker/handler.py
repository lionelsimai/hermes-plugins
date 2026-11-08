"""Handler for Retrieval Test Checker (rag-retrieval-test-checker). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'plan', 'items': ['retrieval test source fidelity', 'retrieval test retrieval relevance', 'retrieval test citation coverage', 'retrieval test freshness', 'retrieval test gap honesty'], 'slug': 'rag-retrieval-test-checker', 'name': 'Retrieval Test Checker'}
def run(args):
    return run_engine(CONFIG, args or {})
