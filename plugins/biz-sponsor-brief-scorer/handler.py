"""Handler for Sponsor Brief Scorer (biz-sponsor-brief-scorer). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'plan', 'items': ['sponsor brief facts supplied only', 'sponsor brief audience fit', 'sponsor brief approval gate', 'sponsor brief next step clarity', 'sponsor brief evidence noted'], 'slug': 'biz-sponsor-brief-scorer', 'name': 'Sponsor Brief Scorer'}
def run(args):
    return run_engine(CONFIG, args or {})
