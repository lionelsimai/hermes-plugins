"""Handler for Lead List Check Reviewer (biz-lead-list-check-reviewer). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'analyze', 'items': ['lead list check facts supplied only', 'lead list check audience fit', 'lead list check approval gate', 'lead list check next step clarity', 'lead list check evidence noted'], 'slug': 'biz-lead-list-check-reviewer', 'name': 'Lead List Check Reviewer'}
def run(args):
    return run_engine(CONFIG, args or {})
