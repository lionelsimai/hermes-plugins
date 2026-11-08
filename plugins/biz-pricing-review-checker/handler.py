"""Handler for Pricing Review Checker (biz-pricing-review-checker). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'score', 'items': ['pricing review facts supplied only', 'pricing review audience fit', 'pricing review approval gate', 'pricing review next step clarity', 'pricing review evidence noted'], 'slug': 'biz-pricing-review-checker', 'name': 'Pricing Review Checker'}
def run(args):
    return run_engine(CONFIG, args or {})
