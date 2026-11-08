"""Handler for Spreadsheet Export Summarizer (files-spreadsheet-export-summarizer). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'prioritize', 'items': ['spreadsheet export format fit', 'spreadsheet export completeness', 'spreadsheet export naming consistency', 'spreadsheet export source fidelity', 'spreadsheet export output location'], 'slug': 'files-spreadsheet-export-summarizer', 'name': 'Spreadsheet Export Summarizer'}
def run(args):
    return run_engine(CONFIG, args or {})
