"""Handler for Ci Pipeline Check Reporter (devops-ci-pipeline-check-reporter). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'template', 'items': ['ci pipeline check risk noted', 'ci pipeline check rollback step', 'ci pipeline check verification', 'ci pipeline check owner named', 'ci pipeline check window fit'], 'slug': 'devops-ci-pipeline-check-reporter', 'name': 'Ci Pipeline Check Reporter'}
def run(args):
    return run_engine(CONFIG, args or {})
