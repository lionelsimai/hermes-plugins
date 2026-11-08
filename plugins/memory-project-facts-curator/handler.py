"""Handler for Project Facts Curator (memory-project-facts-curator). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'analyze', 'items': ['project facts fact accuracy', 'project facts size budget fit', 'project facts staleness', 'project facts duplication', 'project facts source noted'], 'slug': 'memory-project-facts-curator', 'name': 'Project Facts Curator'}
def run(args):
    return run_engine(CONFIG, args or {})
