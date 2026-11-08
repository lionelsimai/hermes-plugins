"""Handler for External Send Gate Gate (safety-external-send-gate-gate). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'plan', 'items': ['external send gate risk identified', 'external send gate approval required', 'external send gate least privilege', 'external send gate reversibility', 'external send gate audit logged'], 'slug': 'safety-external-send-gate-gate', 'name': 'External Send Gate Gate'}
def run(args):
    return run_engine(CONFIG, args or {})
