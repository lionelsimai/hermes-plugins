"""Handler for Wiki Outline Drafter (rag-wiki-outline-drafter). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'template', 'items': ['wiki outline source fidelity', 'wiki outline retrieval relevance', 'wiki outline citation coverage', 'wiki outline freshness', 'wiki outline gap honesty'], 'slug': 'rag-wiki-outline-drafter', 'name': 'Wiki Outline Drafter'}
def run(args):
    return run_engine(CONFIG, args or {})
