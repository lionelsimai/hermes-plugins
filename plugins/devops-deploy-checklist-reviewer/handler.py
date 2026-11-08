"""Handler for Deploy Checklist Reviewer (devops-deploy-checklist-reviewer). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'analyze', 'items': ['deploy checklist risk noted', 'deploy checklist rollback step', 'deploy checklist verification', 'deploy checklist owner named', 'deploy checklist window fit'], 'slug': 'devops-deploy-checklist-reviewer', 'name': 'Deploy Checklist Reviewer'}
def run(args):
    return run_engine(CONFIG, args or {})
