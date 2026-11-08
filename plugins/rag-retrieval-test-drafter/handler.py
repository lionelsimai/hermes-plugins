"""Handler for Retrieval Test Drafter (rag-retrieval-test-drafter). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'score', 'items': ['retrieval test source fidelity', 'retrieval test retrieval relevance', 'retrieval test citation coverage', 'retrieval test freshness', 'retrieval test gap honesty'], 'slug': 'rag-retrieval-test-drafter', 'name': 'Retrieval Test Drafter'}
def run(args):
    return run_engine(CONFIG, args or {})
