"""Handler for Wiki Outline Reviewer (rag-wiki-outline-reviewer). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'checklist', 'items': ['wiki outline source fidelity', 'wiki outline retrieval relevance', 'wiki outline citation coverage', 'wiki outline freshness', 'wiki outline gap honesty'], 'slug': 'rag-wiki-outline-reviewer', 'name': 'Wiki Outline Reviewer'}
def run(args):
    return run_engine(CONFIG, args or {})
