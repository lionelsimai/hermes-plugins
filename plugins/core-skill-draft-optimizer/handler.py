"""Handler for Skill Draft Optimizer (core-skill-draft-optimizer). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'audit', 'items': ['skill draft goal clarity', 'skill draft setup completeness', 'skill draft toolset fit', 'skill draft guardrail coverage', 'skill draft verification step'], 'slug': 'core-skill-draft-optimizer', 'name': 'Skill Draft Optimizer'}
def run(args):
    return run_engine(CONFIG, args or {})
