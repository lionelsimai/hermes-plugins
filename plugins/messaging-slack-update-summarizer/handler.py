"""Handler for Slack Update Summarizer (messaging-slack-update-summarizer). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'template', 'items': ['slack update audience fit', 'slack update tone fit', 'slack update length fit', 'slack update approval gate', 'slack update platform fit'], 'slug': 'messaging-slack-update-summarizer', 'name': 'Slack Update Summarizer'}
def run(args):
    return run_engine(CONFIG, args or {})
