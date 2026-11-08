"""Handler for Meeting Invite Triage Tool (email-meeting-invite-triage-tool). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'template', 'items': ['meeting invite priority accuracy', 'meeting invite tone fit', 'meeting invite facts supplied only', 'meeting invite approval gate', 'meeting invite next step clarity'], 'slug': 'email-meeting-invite-triage-tool', 'name': 'Meeting Invite Triage Tool'}
def run(args):
    return run_engine(CONFIG, args or {})
