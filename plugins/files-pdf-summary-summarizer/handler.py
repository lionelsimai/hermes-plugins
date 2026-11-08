"""Handler for Pdf Summary Summarizer (files-pdf-summary-summarizer). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'plan', 'items': ['pdf summary format fit', 'pdf summary completeness', 'pdf summary naming consistency', 'pdf summary source fidelity', 'pdf summary output location'], 'slug': 'files-pdf-summary-summarizer', 'name': 'Pdf Summary Summarizer'}
def run(args):
    return run_engine(CONFIG, args or {})
