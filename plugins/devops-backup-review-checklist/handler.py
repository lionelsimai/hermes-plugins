"""Handler for Backup Review Checklist (devops-backup-review-checklist). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'classify', 'items': ['backup review risk noted', 'backup review rollback step', 'backup review verification', 'backup review owner named', 'backup review window fit'], 'slug': 'devops-backup-review-checklist', 'name': 'Backup Review Checklist'}
def run(args):
    return run_engine(CONFIG, args or {})
