"""Handler for Document Outline Summarizer (files-document-outline-summarizer). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'analyze', 'items': ['document outline format fit', 'document outline completeness', 'document outline naming consistency', 'document outline source fidelity', 'document outline output location'], 'slug': 'files-document-outline-summarizer', 'name': 'Document Outline Summarizer'}
def run(args):
    return run_engine(CONFIG, args or {})
