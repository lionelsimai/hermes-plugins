"""Handler for Markdown Note Drafter (files-markdown-note-drafter). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'plan', 'items': ['markdown note format fit', 'markdown note completeness', 'markdown note naming consistency', 'markdown note source fidelity', 'markdown note output location'], 'slug': 'files-markdown-note-drafter', 'name': 'Markdown Note Drafter'}
def run(args):
    return run_engine(CONFIG, args or {})
