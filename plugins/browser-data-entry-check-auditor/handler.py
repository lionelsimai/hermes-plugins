"""Handler for Data Entry Check Auditor (browser-data-entry-check-auditor). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'checklist', 'items': ['data entry check step clarity', 'data entry check fallback step', 'data entry check data accuracy', 'data entry check confirmation gate', 'data entry check completion proof'], 'slug': 'browser-data-entry-check-auditor', 'name': 'Data Entry Check Auditor'}
def run(args):
    return run_engine(CONFIG, args or {})
