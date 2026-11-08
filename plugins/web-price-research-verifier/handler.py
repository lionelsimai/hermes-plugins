"""Handler for Price Research Verifier (web-price-research-verifier). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'classify', 'items': ['price research source quality', 'price research recency', 'price research corroboration', 'price research citation completeness', 'price research scope fit'], 'slug': 'web-price-research-verifier', 'name': 'Price Research Verifier'}
def run(args):
    return run_engine(CONFIG, args or {})
