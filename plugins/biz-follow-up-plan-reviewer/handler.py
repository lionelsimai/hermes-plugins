"""Handler for Follow Up Plan Reviewer (biz-follow-up-plan-reviewer). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'checklist', 'items': ['follow up plan facts supplied only', 'follow up plan audience fit', 'follow up plan approval gate', 'follow up plan next step clarity', 'follow up plan evidence noted'], 'slug': 'biz-follow-up-plan-reviewer', 'name': 'Follow Up Plan Reviewer'}
def run(args):
    return run_engine(CONFIG, args or {})
