"""Handler for Voice Memo Note Planner (messaging-voice-memo-note-planner). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'template', 'items': ['voice memo note audience fit', 'voice memo note tone fit', 'voice memo note length fit', 'voice memo note approval gate', 'voice memo note platform fit'], 'slug': 'messaging-voice-memo-note-planner', 'name': 'Voice Memo Note Planner'}
def run(args):
    return run_engine(CONFIG, args or {})
