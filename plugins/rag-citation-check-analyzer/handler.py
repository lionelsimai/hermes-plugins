"""Handler for Citation Check Analyzer (rag-citation-check-analyzer). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'plan', 'items': ['citation check source fidelity', 'citation check retrieval relevance', 'citation check citation coverage', 'citation check freshness', 'citation check gap honesty'], 'slug': 'rag-citation-check-analyzer', 'name': 'Citation Check Analyzer'}
def run(args):
    return run_engine(CONFIG, args or {})
