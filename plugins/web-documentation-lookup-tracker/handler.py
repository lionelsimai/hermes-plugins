"""Handler for Documentation Lookup Tracker (web-documentation-lookup-tracker). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'analyze', 'items': ['documentation lookup source quality', 'documentation lookup recency', 'documentation lookup corroboration', 'documentation lookup citation completeness', 'documentation lookup scope fit'], 'slug': 'web-documentation-lookup-tracker', 'name': 'Documentation Lookup Tracker'}
def run(args):
    return run_engine(CONFIG, args or {})
