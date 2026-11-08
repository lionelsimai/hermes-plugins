"""Handler for Outreach Draft Checker (biz-outreach-draft-checker). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'audit', 'items': ['outreach draft facts supplied only', 'outreach draft audience fit', 'outreach draft approval gate', 'outreach draft next step clarity', 'outreach draft evidence noted'], 'slug': 'biz-outreach-draft-checker', 'name': 'Outreach Draft Checker'}
def run(args):
    return run_engine(CONFIG, args or {})
