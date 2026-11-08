"""Handler for Channel Summary Drafter (messaging-channel-summary-drafter). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'checklist', 'items': ['channel summary audience fit', 'channel summary tone fit', 'channel summary length fit', 'channel summary approval gate', 'channel summary platform fit'], 'slug': 'messaging-channel-summary-drafter', 'name': 'Channel Summary Drafter'}
def run(args):
    return run_engine(CONFIG, args or {})
