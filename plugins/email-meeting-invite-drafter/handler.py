"""Handler for Meeting Invite Drafter (email-meeting-invite-drafter). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'analyze', 'items': ['meeting invite priority accuracy', 'meeting invite tone fit', 'meeting invite facts supplied only', 'meeting invite approval gate', 'meeting invite next step clarity'], 'slug': 'email-meeting-invite-drafter', 'name': 'Meeting Invite Drafter'}
def run(args):
    return run_engine(CONFIG, args or {})
