"""Handler for Login Flow Check Reporter (browser-login-flow-check-reporter). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'audit', 'items': ['login flow check step clarity', 'login flow check fallback step', 'login flow check data accuracy', 'login flow check confirmation gate', 'login flow check completion proof'], 'slug': 'browser-login-flow-check-reporter', 'name': 'Login Flow Check Reporter'}
def run(args):
    return run_engine(CONFIG, args or {})
