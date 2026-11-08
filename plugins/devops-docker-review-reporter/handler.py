"""Handler for Docker Review Reporter (devops-docker-review-reporter). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'prioritize', 'items': ['docker review risk noted', 'docker review rollback step', 'docker review verification', 'docker review owner named', 'docker review window fit'], 'slug': 'devops-docker-review-reporter', 'name': 'Docker Review Reporter'}
def run(args):
    return run_engine(CONFIG, args or {})
