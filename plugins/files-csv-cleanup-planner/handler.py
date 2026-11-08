"""Handler for Csv Cleanup Planner (files-csv-cleanup-planner). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'classify', 'items': ['csv cleanup format fit', 'csv cleanup completeness', 'csv cleanup naming consistency', 'csv cleanup source fidelity', 'csv cleanup output location'], 'slug': 'files-csv-cleanup-planner', 'name': 'Csv Cleanup Planner'}
def run(args):
    return run_engine(CONFIG, args or {})
