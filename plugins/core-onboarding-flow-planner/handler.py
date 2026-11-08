"""Handler for Onboarding Flow Planner (core-onboarding-flow-planner). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'prioritize', 'items': ['onboarding flow goal clarity', 'onboarding flow setup completeness', 'onboarding flow toolset fit', 'onboarding flow guardrail coverage', 'onboarding flow verification step'], 'slug': 'core-onboarding-flow-planner', 'name': 'Onboarding Flow Planner'}
def run(args):
    return run_engine(CONFIG, args or {})
