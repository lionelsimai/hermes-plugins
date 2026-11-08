"""Handler for Csv Cleanup Summarizer (files-csv-cleanup-summarizer). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'checklist', 'items': ['csv cleanup format fit', 'csv cleanup completeness', 'csv cleanup naming consistency', 'csv cleanup source fidelity', 'csv cleanup output location'], 'slug': 'files-csv-cleanup-summarizer', 'name': 'Csv Cleanup Summarizer'}
def run(args):
    return run_engine(CONFIG, args or {})
