"""Handler for Test Run Planner (terminal-test-run-planner). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'classify', 'items': ['test run command safety', 'test run expected output', 'test run timeout set', 'test run rollback step', 'test run verification'], 'slug': 'terminal-test-run-planner', 'name': 'Test Run Planner'}
def run(args):
    return run_engine(CONFIG, args or {})
