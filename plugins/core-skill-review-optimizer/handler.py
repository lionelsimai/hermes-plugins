"""Handler for Skill Review Optimizer (core-skill-review-optimizer). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'template', 'items': ['skill review goal clarity', 'skill review setup completeness', 'skill review toolset fit', 'skill review guardrail coverage', 'skill review verification step'], 'slug': 'core-skill-review-optimizer', 'name': 'Skill Review Optimizer'}
def run(args):
    return run_engine(CONFIG, args or {})
