"""Handler for Document Outline Checker (files-document-outline-checker). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'classify', 'items': ['document outline format fit', 'document outline completeness', 'document outline naming consistency', 'document outline source fidelity', 'document outline output location'], 'slug': 'files-document-outline-checker', 'name': 'Document Outline Checker'}
def run(args):
    return run_engine(CONFIG, args or {})
