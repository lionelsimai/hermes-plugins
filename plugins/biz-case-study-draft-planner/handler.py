"""Handler for Case Study Draft Planner (biz-case-study-draft-planner). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'audit', 'items': ['case study draft facts supplied only', 'case study draft audience fit', 'case study draft approval gate', 'case study draft next step clarity', 'case study draft evidence noted'], 'slug': 'biz-case-study-draft-planner', 'name': 'Case Study Draft Planner'}
def run(args):
    return run_engine(CONFIG, args or {})
