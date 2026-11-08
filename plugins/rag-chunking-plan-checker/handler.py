"""Handler for Chunking Plan Checker (rag-chunking-plan-checker). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'classify', 'items': ['chunking plan source fidelity', 'chunking plan retrieval relevance', 'chunking plan citation coverage', 'chunking plan freshness', 'chunking plan gap honesty'], 'slug': 'rag-chunking-plan-checker', 'name': 'Chunking Plan Checker'}
def run(args):
    return run_engine(CONFIG, args or {})
