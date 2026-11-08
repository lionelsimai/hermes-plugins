"""Handler for Meeting Prep Checker (biz-meeting-prep-checker). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'checklist', 'items': ['meeting prep facts supplied only', 'meeting prep audience fit', 'meeting prep approval gate', 'meeting prep next step clarity', 'meeting prep evidence noted'], 'slug': 'biz-meeting-prep-checker', 'name': 'Meeting Prep Checker'}
def run(args):
    return run_engine(CONFIG, args or {})
