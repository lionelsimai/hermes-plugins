"""Handler for Proposal Outline Planner (biz-proposal-outline-planner). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'checklist', 'items': ['proposal outline facts supplied only', 'proposal outline audience fit', 'proposal outline approval gate', 'proposal outline next step clarity', 'proposal outline evidence noted'], 'slug': 'biz-proposal-outline-planner', 'name': 'Proposal Outline Planner'}
def run(args):
    return run_engine(CONFIG, args or {})
