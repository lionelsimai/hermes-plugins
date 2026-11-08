"""Handler for Voiceover Script Planner (media-voiceover-script-planner). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'checklist', 'items': ['voiceover script brief clarity', 'voiceover script format spec', 'voiceover script rights and consent', 'voiceover script quality gate', 'voiceover script approval gate'], 'slug': 'media-voiceover-script-planner', 'name': 'Voiceover Script Planner'}
def run(args):
    return run_engine(CONFIG, args or {})
