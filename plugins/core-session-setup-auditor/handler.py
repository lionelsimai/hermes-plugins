"""Handler for Session Setup Auditor (core-session-setup-auditor). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'plan', 'items': ['session setup goal clarity', 'session setup setup completeness', 'session setup toolset fit', 'session setup guardrail coverage', 'session setup verification step'], 'slug': 'core-session-setup-auditor', 'name': 'Session Setup Auditor'}
def run(args):
    return run_engine(CONFIG, args or {})
