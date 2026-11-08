"""Handler for Gap Analysis Planner (rag-gap-analysis-planner). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'analyze', 'items': ['gap analysis source fidelity', 'gap analysis retrieval relevance', 'gap analysis citation coverage', 'gap analysis freshness', 'gap analysis gap honesty'], 'slug': 'rag-gap-analysis-planner', 'name': 'Gap Analysis Planner'}
def run(args):
    return run_engine(CONFIG, args or {})
