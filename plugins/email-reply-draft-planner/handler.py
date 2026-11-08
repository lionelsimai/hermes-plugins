"""Handler for Reply Draft Planner (email-reply-draft-planner). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'score', 'items': ['reply draft priority accuracy', 'reply draft tone fit', 'reply draft facts supplied only', 'reply draft approval gate', 'reply draft next step clarity'], 'slug': 'email-reply-draft-planner', 'name': 'Reply Draft Planner'}
def run(args):
    return run_engine(CONFIG, args or {})
