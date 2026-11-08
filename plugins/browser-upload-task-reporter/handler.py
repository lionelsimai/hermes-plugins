"""Handler for Upload Task Reporter (browser-upload-task-reporter). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'checklist', 'items': ['upload task step clarity', 'upload task fallback step', 'upload task data accuracy', 'upload task confirmation gate', 'upload task completion proof'], 'slug': 'browser-upload-task-reporter', 'name': 'Upload Task Reporter'}
def run(args):
    return run_engine(CONFIG, args or {})
