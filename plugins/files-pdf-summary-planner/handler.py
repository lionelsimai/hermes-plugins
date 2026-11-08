"""Handler for Pdf Summary Planner (files-pdf-summary-planner). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'checklist', 'items': ['pdf summary format fit', 'pdf summary completeness', 'pdf summary naming consistency', 'pdf summary source fidelity', 'pdf summary output location'], 'slug': 'files-pdf-summary-planner', 'name': 'Pdf Summary Planner'}
def run(args):
    return run_engine(CONFIG, args or {})
