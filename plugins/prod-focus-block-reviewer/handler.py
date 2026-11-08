"""Handler for Focus Block Reviewer (prod-focus-block-reviewer). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'analyze', 'items': ['focus block priority clarity', 'focus block time realism', 'focus block next action named', 'focus block review cadence', 'focus block owner named'], 'slug': 'prod-focus-block-reviewer', 'name': 'Focus Block Reviewer'}
def run(args):
    return run_engine(CONFIG, args or {})
