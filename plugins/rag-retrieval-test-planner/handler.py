"""Handler for Retrieval Test Planner (rag-retrieval-test-planner). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'audit', 'items': ['retrieval test source fidelity', 'retrieval test retrieval relevance', 'retrieval test citation coverage', 'retrieval test freshness', 'retrieval test gap honesty'], 'slug': 'rag-retrieval-test-planner', 'name': 'Retrieval Test Planner'}
def run(args):
    return run_engine(CONFIG, args or {})
