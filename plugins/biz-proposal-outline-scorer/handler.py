"""Handler for Proposal Outline Scorer (biz-proposal-outline-scorer). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'analyze', 'items': ['proposal outline facts supplied only', 'proposal outline audience fit', 'proposal outline approval gate', 'proposal outline next step clarity', 'proposal outline evidence noted'], 'slug': 'biz-proposal-outline-scorer', 'name': 'Proposal Outline Scorer'}
def run(args):
    return run_engine(CONFIG, args or {})
