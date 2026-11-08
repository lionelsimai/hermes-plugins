"""Handler for Sponsor Brief Planner (biz-sponsor-brief-planner). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'classify', 'items': ['sponsor brief facts supplied only', 'sponsor brief audience fit', 'sponsor brief approval gate', 'sponsor brief next step clarity', 'sponsor brief evidence noted'], 'slug': 'biz-sponsor-brief-planner', 'name': 'Sponsor Brief Planner'}
def run(args):
    return run_engine(CONFIG, args or {})
