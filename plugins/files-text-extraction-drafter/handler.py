"""Handler for Text Extraction Drafter (files-text-extraction-drafter). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'classify', 'items': ['text extraction format fit', 'text extraction completeness', 'text extraction naming consistency', 'text extraction source fidelity', 'text extraction output location'], 'slug': 'files-text-extraction-drafter', 'name': 'Text Extraction Drafter'}
def run(args):
    return run_engine(CONFIG, args or {})
