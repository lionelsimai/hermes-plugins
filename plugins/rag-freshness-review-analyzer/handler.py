"""Handler for Freshness Review Analyzer (rag-freshness-review-analyzer). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'template', 'items': ['freshness review source fidelity', 'freshness review retrieval relevance', 'freshness review citation coverage', 'freshness review freshness', 'freshness review gap honesty'], 'slug': 'rag-freshness-review-analyzer', 'name': 'Freshness Review Analyzer'}
def run(args):
    return run_engine(CONFIG, args or {})
