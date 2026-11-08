"""Handler for Shopping List Drafter (prod-shopping-list-drafter). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'analyze', 'items': ['shopping list priority clarity', 'shopping list time realism', 'shopping list next action named', 'shopping list review cadence', 'shopping list owner named'], 'slug': 'prod-shopping-list-drafter', 'name': 'Shopping List Drafter'}
def run(args):
    return run_engine(CONFIG, args or {})
