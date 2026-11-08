"""Handler for Case Study Draft Scorer (biz-case-study-draft-scorer). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'prioritize', 'items': ['case study draft facts supplied only', 'case study draft audience fit', 'case study draft approval gate', 'case study draft next step clarity', 'case study draft evidence noted'], 'slug': 'biz-case-study-draft-scorer', 'name': 'Case Study Draft Scorer'}
def run(args):
    return run_engine(CONFIG, args or {})
