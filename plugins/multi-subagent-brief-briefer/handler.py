"""Handler for Subagent Brief Briefer (multi-subagent-brief-briefer). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'template', 'items': ['subagent brief scope clarity', 'subagent brief independence of subtasks', 'subagent brief merge criteria', 'subagent brief context budget', 'subagent brief verification step'], 'slug': 'multi-subagent-brief-briefer', 'name': 'Subagent Brief Briefer'}
def run(args):
    return run_engine(CONFIG, args or {})
