"""Handler for File Rename Plan Organizer (files-file-rename-plan-organizer). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'prioritize', 'items': ['file rename plan format fit', 'file rename plan completeness', 'file rename plan naming consistency', 'file rename plan source fidelity', 'file rename plan output location'], 'slug': 'files-file-rename-plan-organizer', 'name': 'File Rename Plan Organizer'}
def run(args):
    return run_engine(CONFIG, args or {})
