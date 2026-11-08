"""Handler for Cost Review Reviewer (devops-cost-review-reviewer). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'score', 'items': ['cost review risk noted', 'cost review rollback step', 'cost review verification', 'cost review owner named', 'cost review window fit'], 'slug': 'devops-cost-review-reviewer', 'name': 'Cost Review Reviewer'}
def run(args):
    return run_engine(CONFIG, args or {})
