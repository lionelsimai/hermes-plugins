"""Handler for Document Outline Planner (files-document-outline-planner). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'plan', 'items': ['document outline format fit', 'document outline completeness', 'document outline naming consistency', 'document outline source fidelity', 'document outline output location'], 'slug': 'files-document-outline-planner', 'name': 'Document Outline Planner'}
def run(args):
    return run_engine(CONFIG, args or {})
