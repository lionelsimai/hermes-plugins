"""Handler for Meeting Agenda Checker (email-meeting-agenda-checker). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'score', 'items': ['meeting agenda priority accuracy', 'meeting agenda tone fit', 'meeting agenda facts supplied only', 'meeting agenda approval gate', 'meeting agenda next step clarity'], 'slug': 'email-meeting-agenda-checker', 'name': 'Meeting Agenda Checker'}
def run(args):
    return run_engine(CONFIG, args or {})
