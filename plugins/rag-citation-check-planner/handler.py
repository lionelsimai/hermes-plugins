"""Handler for Citation Check Planner (rag-citation-check-planner). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'template', 'items': ['citation check source fidelity', 'citation check retrieval relevance', 'citation check citation coverage', 'citation check freshness', 'citation check gap honesty'], 'slug': 'rag-citation-check-planner', 'name': 'Citation Check Planner'}
def run(args):
    return run_engine(CONFIG, args or {})
