"""Handler for Audio Cleanup Plan Planner (media-audio-cleanup-plan-planner). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'audit', 'items': ['audio cleanup plan brief clarity', 'audio cleanup plan format spec', 'audio cleanup plan rights and consent', 'audio cleanup plan quality gate', 'audio cleanup plan approval gate'], 'slug': 'media-audio-cleanup-plan-planner', 'name': 'Audio Cleanup Plan Planner'}
def run(args):
    return run_engine(CONFIG, args or {})
