"""Handler for Pricing Review Scorer (biz-pricing-review-scorer). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'classify', 'items': ['pricing review facts supplied only', 'pricing review audience fit', 'pricing review approval gate', 'pricing review next step clarity', 'pricing review evidence noted'], 'slug': 'biz-pricing-review-scorer', 'name': 'Pricing Review Scorer'}
def run(args):
    return run_engine(CONFIG, args or {})
