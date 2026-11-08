"""Handler for Log Alert Review Checklist (devops-log-alert-review-checklist). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'template', 'items': ['log alert review risk noted', 'log alert review rollback step', 'log alert review verification', 'log alert review owner named', 'log alert review window fit'], 'slug': 'devops-log-alert-review-checklist', 'name': 'Log Alert Review Checklist'}
def run(args):
    return run_engine(CONFIG, args or {})
