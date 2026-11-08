"""Handler for Whatsapp Broadcast Draft Summarizer (messaging-whatsapp-broadcast-draft-summarizer). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'prioritize', 'items': ['whatsapp broadcast draft audience fit', 'whatsapp broadcast draft tone fit', 'whatsapp broadcast draft length fit', 'whatsapp broadcast draft approval gate', 'whatsapp broadcast draft platform fit'], 'slug': 'messaging-whatsapp-broadcast-draft-summarizer', 'name': 'Whatsapp Broadcast Draft Summarizer'}
def run(args):
    return run_engine(CONFIG, args or {})
