"""Handler for Folder Structure Organizer (files-folder-structure-organizer). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'classify', 'items': ['folder structure format fit', 'folder structure completeness', 'folder structure naming consistency', 'folder structure source fidelity', 'folder structure output location'], 'slug': 'files-folder-structure-organizer', 'name': 'Folder Structure Organizer'}
def run(args):
    return run_engine(CONFIG, args or {})
