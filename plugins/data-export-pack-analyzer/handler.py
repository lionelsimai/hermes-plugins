"""Handler for Export Pack Analyzer (data-export-pack-analyzer). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'prioritize', 'items': ['export pack data completeness', 'export pack column consistency', 'export pack outliers flagged', 'export pack totals verified', 'export pack format fit'], 'slug': 'data-export-pack-analyzer', 'name': 'Export Pack Analyzer'}
def run(args):
    return run_engine(CONFIG, args or {})
