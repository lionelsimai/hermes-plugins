"""Handler for Channel Summary Checker (messaging-channel-summary-checker). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'classify', 'items': ['channel summary audience fit', 'channel summary tone fit', 'channel summary length fit', 'channel summary approval gate', 'channel summary platform fit'], 'slug': 'messaging-channel-summary-checker', 'name': 'Channel Summary Checker'}
def run(args):
    return run_engine(CONFIG, args or {})
