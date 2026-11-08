"""Handler for Csv Cleanup Checker (files-csv-cleanup-checker). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'template', 'items': ['csv cleanup format fit', 'csv cleanup completeness', 'csv cleanup naming consistency', 'csv cleanup source fidelity', 'csv cleanup output location'], 'slug': 'files-csv-cleanup-checker', 'name': 'Csv Cleanup Checker'}
def run(args):
    return run_engine(CONFIG, args or {})
