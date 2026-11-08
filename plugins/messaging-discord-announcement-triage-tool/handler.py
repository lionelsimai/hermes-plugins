"""Handler for Discord Announcement Triage Tool (messaging-discord-announcement-triage-tool). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'classify', 'items': ['discord announcement audience fit', 'discord announcement tone fit', 'discord announcement length fit', 'discord announcement approval gate', 'discord announcement platform fit'], 'slug': 'messaging-discord-announcement-triage-tool', 'name': 'Discord Announcement Triage Tool'}
def run(args):
    return run_engine(CONFIG, args or {})
