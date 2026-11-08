"""Handler for Partner Shortlist Reviewer (biz-partner-shortlist-reviewer). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'score', 'items': ['partner shortlist facts supplied only', 'partner shortlist audience fit', 'partner shortlist approval gate', 'partner shortlist next step clarity', 'partner shortlist evidence noted'], 'slug': 'biz-partner-shortlist-reviewer', 'name': 'Partner Shortlist Reviewer'}
def run(args):
    return run_engine(CONFIG, args or {})
