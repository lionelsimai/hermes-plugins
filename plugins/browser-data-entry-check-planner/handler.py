"""Handler for Data Entry Check Planner (browser-data-entry-check-planner). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'prioritize', 'items': ['data entry check step clarity', 'data entry check fallback step', 'data entry check data accuracy', 'data entry check confirmation gate', 'data entry check completion proof'], 'slug': 'browser-data-entry-check-planner', 'name': 'Data Entry Check Planner'}
def run(args):
    return run_engine(CONFIG, args or {})
