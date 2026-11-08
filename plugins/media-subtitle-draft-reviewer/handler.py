"""Handler for Subtitle Draft Reviewer (media-subtitle-draft-reviewer). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'template', 'items': ['subtitle draft brief clarity', 'subtitle draft format spec', 'subtitle draft rights and consent', 'subtitle draft quality gate', 'subtitle draft approval gate'], 'slug': 'media-subtitle-draft-reviewer', 'name': 'Subtitle Draft Reviewer'}
def run(args):
    return run_engine(CONFIG, args or {})
