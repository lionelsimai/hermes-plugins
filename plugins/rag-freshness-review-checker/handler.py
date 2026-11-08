"""Handler for Freshness Review Checker (rag-freshness-review-checker). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'prioritize', 'items': ['freshness review source fidelity', 'freshness review retrieval relevance', 'freshness review citation coverage', 'freshness review freshness', 'freshness review gap honesty'], 'slug': 'rag-freshness-review-checker', 'name': 'Freshness Review Checker'}
def run(args):
    return run_engine(CONFIG, args or {})
