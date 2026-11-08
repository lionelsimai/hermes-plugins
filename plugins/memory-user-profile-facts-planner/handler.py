"""Handler for User Profile Facts Planner (memory-user-profile-facts-planner). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'template', 'items': ['user profile facts fact accuracy', 'user profile facts size budget fit', 'user profile facts staleness', 'user profile facts duplication', 'user profile facts source noted'], 'slug': 'memory-user-profile-facts-planner', 'name': 'User Profile Facts Planner'}
def run(args):
    return run_engine(CONFIG, args or {})
