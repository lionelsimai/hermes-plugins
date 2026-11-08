"""Handler for Report Draft Organizer (files-report-draft-organizer). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'analyze', 'items': ['report draft format fit', 'report draft completeness', 'report draft naming consistency', 'report draft source fidelity', 'report draft output location'], 'slug': 'files-report-draft-organizer', 'name': 'Report Draft Organizer'}
def run(args):
    return run_engine(CONFIG, args or {})
