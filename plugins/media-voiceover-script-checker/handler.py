"""Handler for Voiceover Script Checker (media-voiceover-script-checker). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'template', 'items': ['voiceover script brief clarity', 'voiceover script format spec', 'voiceover script rights and consent', 'voiceover script quality gate', 'voiceover script approval gate'], 'slug': 'media-voiceover-script-checker', 'name': 'Voiceover Script Checker'}
def run(args):
    return run_engine(CONFIG, args or {})
