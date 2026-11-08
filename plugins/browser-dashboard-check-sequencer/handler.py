"""Handler for Dashboard Check Sequencer (browser-dashboard-check-sequencer). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'analyze', 'items': ['dashboard check step clarity', 'dashboard check fallback step', 'dashboard check data accuracy', 'dashboard check confirmation gate', 'dashboard check completion proof'], 'slug': 'browser-dashboard-check-sequencer', 'name': 'Dashboard Check Sequencer'}
def run(args):
    return run_engine(CONFIG, args or {})
