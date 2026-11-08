"""Handler for Data Entry Check Reporter (browser-data-entry-check-reporter). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'analyze', 'items': ['data entry check step clarity', 'data entry check fallback step', 'data entry check data accuracy', 'data entry check confirmation gate', 'data entry check completion proof'], 'slug': 'browser-data-entry-check-reporter', 'name': 'Data Entry Check Reporter'}
def run(args):
    return run_engine(CONFIG, args or {})
