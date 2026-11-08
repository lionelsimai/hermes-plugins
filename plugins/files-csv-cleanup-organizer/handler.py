"""Handler for Csv Cleanup Organizer (files-csv-cleanup-organizer). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'score', 'items': ['csv cleanup format fit', 'csv cleanup completeness', 'csv cleanup naming consistency', 'csv cleanup source fidelity', 'csv cleanup output location'], 'slug': 'files-csv-cleanup-organizer', 'name': 'Csv Cleanup Organizer'}
def run(args):
    return run_engine(CONFIG, args or {})
