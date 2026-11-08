"""Handler for Whatsapp Broadcast Draft Triage Tool (messaging-whatsapp-broadcast-draft-triage-tool). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'plan', 'items': ['whatsapp broadcast draft audience fit', 'whatsapp broadcast draft tone fit', 'whatsapp broadcast draft length fit', 'whatsapp broadcast draft approval gate', 'whatsapp broadcast draft platform fit'], 'slug': 'messaging-whatsapp-broadcast-draft-triage-tool', 'name': 'Whatsapp Broadcast Draft Triage Tool'}
def run(args):
    return run_engine(CONFIG, args or {})
