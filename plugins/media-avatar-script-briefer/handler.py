"""Handler for Avatar Script Briefer (media-avatar-script-briefer). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'audit', 'items': ['avatar script brief clarity', 'avatar script format spec', 'avatar script rights and consent', 'avatar script quality gate', 'avatar script approval gate'], 'slug': 'media-avatar-script-briefer', 'name': 'Avatar Script Briefer'}
def run(args):
    return run_engine(CONFIG, args or {})
