"""Handler for Shopping List Triage Tool (prod-shopping-list-triage-tool). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'score', 'items': ['shopping list priority clarity', 'shopping list time realism', 'shopping list next action named', 'shopping list review cadence', 'shopping list owner named'], 'slug': 'prod-shopping-list-triage-tool', 'name': 'Shopping List Triage Tool'}
def run(args):
    return run_engine(CONFIG, args or {})
