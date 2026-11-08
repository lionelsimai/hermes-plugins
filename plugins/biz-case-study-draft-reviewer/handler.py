"""Handler for Case Study Draft Reviewer (biz-case-study-draft-reviewer). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'plan', 'items': ['case study draft facts supplied only', 'case study draft audience fit', 'case study draft approval gate', 'case study draft next step clarity', 'case study draft evidence noted'], 'slug': 'biz-case-study-draft-reviewer', 'name': 'Case Study Draft Reviewer'}
def run(args):
    return run_engine(CONFIG, args or {})
