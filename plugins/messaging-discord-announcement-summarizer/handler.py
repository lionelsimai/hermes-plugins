"""Handler for Discord Announcement Summarizer (messaging-discord-announcement-summarizer). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'audit', 'items': ['discord announcement audience fit', 'discord announcement tone fit', 'discord announcement length fit', 'discord announcement approval gate', 'discord announcement platform fit'], 'slug': 'messaging-discord-announcement-summarizer', 'name': 'Discord Announcement Summarizer'}
def run(args):
    return run_engine(CONFIG, args or {})
