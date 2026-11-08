"""Handler for Partner Shortlist Scorer (biz-partner-shortlist-scorer). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'checklist', 'items': ['partner shortlist facts supplied only', 'partner shortlist audience fit', 'partner shortlist approval gate', 'partner shortlist next step clarity', 'partner shortlist evidence noted'], 'slug': 'biz-partner-shortlist-scorer', 'name': 'Partner Shortlist Scorer'}
def run(args):
    return run_engine(CONFIG, args or {})
