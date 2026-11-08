"""Handler for Dns Change Plan Reporter (devops-dns-change-plan-reporter). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'classify', 'items': ['dns change plan risk noted', 'dns change plan rollback step', 'dns change plan verification', 'dns change plan owner named', 'dns change plan window fit'], 'slug': 'devops-dns-change-plan-reporter', 'name': 'Dns Change Plan Reporter'}
def run(args):
    return run_engine(CONFIG, args or {})
