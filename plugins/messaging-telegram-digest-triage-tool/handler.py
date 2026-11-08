"""Handler for Telegram Digest Triage Tool (messaging-telegram-digest-triage-tool). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'prioritize', 'items': ['telegram digest audience fit', 'telegram digest tone fit', 'telegram digest length fit', 'telegram digest approval gate', 'telegram digest platform fit'], 'slug': 'messaging-telegram-digest-triage-tool', 'name': 'Telegram Digest Triage Tool'}
def run(args):
    return run_engine(CONFIG, args or {})
