"""Handler for Folder Structure Summarizer (files-folder-structure-summarizer). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'audit', 'items': ['folder structure format fit', 'folder structure completeness', 'folder structure naming consistency', 'folder structure source fidelity', 'folder structure output location'], 'slug': 'files-folder-structure-summarizer', 'name': 'Folder Structure Summarizer'}
def run(args):
    return run_engine(CONFIG, args or {})
