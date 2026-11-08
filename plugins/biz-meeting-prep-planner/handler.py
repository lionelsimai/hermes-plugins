"""Handler for Meeting Prep Planner (biz-meeting-prep-planner). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'analyze', 'items': ['meeting prep facts supplied only', 'meeting prep audience fit', 'meeting prep approval gate', 'meeting prep next step clarity', 'meeting prep evidence noted'], 'slug': 'biz-meeting-prep-planner', 'name': 'Meeting Prep Planner'}
def run(args):
    return run_engine(CONFIG, args or {})
