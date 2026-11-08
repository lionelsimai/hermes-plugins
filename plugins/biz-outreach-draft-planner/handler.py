"""Handler for Outreach Draft Planner (biz-outreach-draft-planner). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'prioritize', 'items': ['outreach draft facts supplied only', 'outreach draft audience fit', 'outreach draft approval gate', 'outreach draft next step clarity', 'outreach draft evidence noted'], 'slug': 'biz-outreach-draft-planner', 'name': 'Outreach Draft Planner'}
def run(args):
    return run_engine(CONFIG, args or {})
