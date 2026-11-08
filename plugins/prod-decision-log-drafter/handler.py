"""Handler for Decision Log Drafter (prod-decision-log-drafter). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'checklist', 'items': ['decision log priority clarity', 'decision log time realism', 'decision log next action named', 'decision log review cadence', 'decision log owner named'], 'slug': 'prod-decision-log-drafter', 'name': 'Decision Log Drafter'}
def run(args):
    return run_engine(CONFIG, args or {})
