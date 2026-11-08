"""Handler for Member Onboarding Reporter (community-member-onboarding-reporter). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'audit', 'items': ['member onboarding member fit', 'member onboarding tone fit', 'member onboarding approval gate', 'member onboarding safety check', 'member onboarding follow up named'], 'slug': 'community-member-onboarding-reporter', 'name': 'Member Onboarding Reporter'}
def run(args):
    return run_engine(CONFIG, args or {})
