"""Handler for Reading List Triage Tool (prod-reading-list-triage-tool). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'checklist', 'items': ['reading list priority clarity', 'reading list time realism', 'reading list next action named', 'reading list review cadence', 'reading list owner named'], 'slug': 'prod-reading-list-triage-tool', 'name': 'Reading List Triage Tool'}
def run(args):
    return run_engine(CONFIG, args or {})
