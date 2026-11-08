"""Handler for Discord Announcement Planner (messaging-discord-announcement-planner). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'prioritize', 'items': ['discord announcement audience fit', 'discord announcement tone fit', 'discord announcement length fit', 'discord announcement approval gate', 'discord announcement platform fit'], 'slug': 'messaging-discord-announcement-planner', 'name': 'Discord Announcement Planner'}
def run(args):
    return run_engine(CONFIG, args or {})
