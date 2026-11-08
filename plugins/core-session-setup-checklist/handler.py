"""Handler for Session Setup Checklist (core-session-setup-checklist). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'score', 'items': ['session setup goal clarity', 'session setup setup completeness', 'session setup toolset fit', 'session setup guardrail coverage', 'session setup verification step'], 'slug': 'core-session-setup-checklist', 'name': 'Session Setup Checklist'}
def run(args):
    return run_engine(CONFIG, args or {})
