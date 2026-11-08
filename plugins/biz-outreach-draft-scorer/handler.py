"""Handler for Outreach Draft Scorer (biz-outreach-draft-scorer). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'checklist', 'items': ['outreach draft facts supplied only', 'outreach draft audience fit', 'outreach draft approval gate', 'outreach draft next step clarity', 'outreach draft evidence noted'], 'slug': 'biz-outreach-draft-scorer', 'name': 'Outreach Draft Scorer'}
def run(args):
    return run_engine(CONFIG, args or {})
