"""Handler for Dashboard Check Reporter (browser-dashboard-check-reporter). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'classify', 'items': ['dashboard check step clarity', 'dashboard check fallback step', 'dashboard check data accuracy', 'dashboard check confirmation gate', 'dashboard check completion proof'], 'slug': 'browser-dashboard-check-reporter', 'name': 'Dashboard Check Reporter'}
def run(args):
    return run_engine(CONFIG, args or {})
