"""Handler for Toolset Selection Auditor (core-toolset-selection-auditor). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'analyze', 'items': ['toolset selection goal clarity', 'toolset selection setup completeness', 'toolset selection toolset fit', 'toolset selection guardrail coverage', 'toolset selection verification step'], 'slug': 'core-toolset-selection-auditor', 'name': 'Toolset Selection Auditor'}
def run(args):
    return run_engine(CONFIG, args or {})
