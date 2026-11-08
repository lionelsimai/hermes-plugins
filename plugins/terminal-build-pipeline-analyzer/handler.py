"""Handler for Build Pipeline Analyzer (terminal-build-pipeline-analyzer). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'analyze', 'items': ['build pipeline command safety', 'build pipeline expected output', 'build pipeline timeout set', 'build pipeline rollback step', 'build pipeline verification'], 'slug': 'terminal-build-pipeline-analyzer', 'name': 'Build Pipeline Analyzer'}
def run(args):
    return run_engine(CONFIG, args or {})
