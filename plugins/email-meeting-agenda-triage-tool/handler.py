"""Handler for Meeting Agenda Triage Tool (email-meeting-agenda-triage-tool). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'plan', 'items': ['meeting agenda priority accuracy', 'meeting agenda tone fit', 'meeting agenda facts supplied only', 'meeting agenda approval gate', 'meeting agenda next step clarity'], 'slug': 'email-meeting-agenda-triage-tool', 'name': 'Meeting Agenda Triage Tool'}
def run(args):
    return run_engine(CONFIG, args or {})
