"""Handler for Pipeline Review Checker (biz-pipeline-review-checker). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'classify', 'items': ['pipeline review facts supplied only', 'pipeline review audience fit', 'pipeline review approval gate', 'pipeline review next step clarity', 'pipeline review evidence noted'], 'slug': 'biz-pipeline-review-checker', 'name': 'Pipeline Review Checker'}
def run(args):
    return run_engine(CONFIG, args or {})
