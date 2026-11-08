"""Handler for Weekly Review Triage Tool (prod-weekly-review-triage-tool). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'prioritize', 'items': ['weekly review priority clarity', 'weekly review time realism', 'weekly review next action named', 'weekly review review cadence', 'weekly review owner named'], 'slug': 'prod-weekly-review-triage-tool', 'name': 'Weekly Review Triage Tool'}
def run(args):
    return run_engine(CONFIG, args or {})
