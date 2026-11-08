"""Handler for Gap Analysis Checker (rag-gap-analysis-checker). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'classify', 'items': ['gap analysis source fidelity', 'gap analysis retrieval relevance', 'gap analysis citation coverage', 'gap analysis freshness', 'gap analysis gap honesty'], 'slug': 'rag-gap-analysis-checker', 'name': 'Gap Analysis Checker'}
def run(args):
    return run_engine(CONFIG, args or {})
