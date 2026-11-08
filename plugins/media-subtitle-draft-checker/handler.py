"""Handler for Subtitle Draft Checker (media-subtitle-draft-checker). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'checklist', 'items': ['subtitle draft brief clarity', 'subtitle draft format spec', 'subtitle draft rights and consent', 'subtitle draft quality gate', 'subtitle draft approval gate'], 'slug': 'media-subtitle-draft-checker', 'name': 'Subtitle Draft Checker'}
def run(args):
    return run_engine(CONFIG, args or {})
