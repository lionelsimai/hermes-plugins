"""Handler for Preference Notes Curator (memory-preference-notes-curator). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'score', 'items': ['preference notes fact accuracy', 'preference notes size budget fit', 'preference notes staleness', 'preference notes duplication', 'preference notes source noted'], 'slug': 'memory-preference-notes-curator', 'name': 'Preference Notes Curator'}
def run(args):
    return run_engine(CONFIG, args or {})
