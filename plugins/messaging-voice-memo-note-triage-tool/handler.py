"""Handler for Voice Memo Note Triage Tool (messaging-voice-memo-note-triage-tool). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'prioritize', 'items': ['voice memo note audience fit', 'voice memo note tone fit', 'voice memo note length fit', 'voice memo note approval gate', 'voice memo note platform fit'], 'slug': 'messaging-voice-memo-note-triage-tool', 'name': 'Voice Memo Note Triage Tool'}
def run(args):
    return run_engine(CONFIG, args or {})
