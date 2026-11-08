"""Handler for Audio Cleanup Plan Checker (media-audio-cleanup-plan-checker). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'plan', 'items': ['audio cleanup plan brief clarity', 'audio cleanup plan format spec', 'audio cleanup plan rights and consent', 'audio cleanup plan quality gate', 'audio cleanup plan approval gate'], 'slug': 'media-audio-cleanup-plan-checker', 'name': 'Audio Cleanup Plan Checker'}
def run(args):
    return run_engine(CONFIG, args or {})
