"""Handler for Pipeline Review Planner (biz-pipeline-review-planner). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'plan', 'items': ['pipeline review facts supplied only', 'pipeline review audience fit', 'pipeline review approval gate', 'pipeline review next step clarity', 'pipeline review evidence noted'], 'slug': 'biz-pipeline-review-planner', 'name': 'Pipeline Review Planner'}
def run(args):
    return run_engine(CONFIG, args or {})
