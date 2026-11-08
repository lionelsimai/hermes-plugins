"""Handler for Agent Profile Optimizer (core-agent-profile-optimizer). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'classify', 'items': ['agent profile goal clarity', 'agent profile setup completeness', 'agent profile toolset fit', 'agent profile guardrail coverage', 'agent profile verification step'], 'slug': 'core-agent-profile-optimizer', 'name': 'Agent Profile Optimizer'}
def run(args):
    return run_engine(CONFIG, args or {})
