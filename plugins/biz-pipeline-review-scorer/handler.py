"""Handler for Pipeline Review Scorer (biz-pipeline-review-scorer). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'score', 'items': ['pipeline review facts supplied only', 'pipeline review audience fit', 'pipeline review approval gate', 'pipeline review next step clarity', 'pipeline review evidence noted'], 'slug': 'biz-pipeline-review-scorer', 'name': 'Pipeline Review Scorer'}
def run(args):
    return run_engine(CONFIG, args or {})
