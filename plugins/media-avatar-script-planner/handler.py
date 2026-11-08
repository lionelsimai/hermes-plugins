"""Handler for Avatar Script Planner (media-avatar-script-planner). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'prioritize', 'items': ['avatar script brief clarity', 'avatar script format spec', 'avatar script rights and consent', 'avatar script quality gate', 'avatar script approval gate'], 'slug': 'media-avatar-script-planner', 'name': 'Avatar Script Planner'}
def run(args):
    return run_engine(CONFIG, args or {})
