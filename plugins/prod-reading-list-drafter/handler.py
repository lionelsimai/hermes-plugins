"""Handler for Reading List Drafter (prod-reading-list-drafter). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'classify', 'items': ['reading list priority clarity', 'reading list time realism', 'reading list next action named', 'reading list review cadence', 'reading list owner named'], 'slug': 'prod-reading-list-drafter', 'name': 'Reading List Drafter'}
def run(args):
    return run_engine(CONFIG, args or {})
