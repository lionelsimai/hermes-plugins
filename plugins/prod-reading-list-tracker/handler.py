"""Handler for Reading List Tracker (prod-reading-list-tracker). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'analyze', 'items': ['reading list priority clarity', 'reading list time realism', 'reading list next action named', 'reading list review cadence', 'reading list owner named'], 'slug': 'prod-reading-list-tracker', 'name': 'Reading List Tracker'}
def run(args):
    return run_engine(CONFIG, args or {})
