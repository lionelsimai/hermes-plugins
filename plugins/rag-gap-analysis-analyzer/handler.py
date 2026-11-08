"""Handler for Gap Analysis Analyzer (rag-gap-analysis-analyzer). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'prioritize', 'items': ['gap analysis source fidelity', 'gap analysis retrieval relevance', 'gap analysis citation coverage', 'gap analysis freshness', 'gap analysis gap honesty'], 'slug': 'rag-gap-analysis-analyzer', 'name': 'Gap Analysis Analyzer'}
def run(args):
    return run_engine(CONFIG, args or {})
