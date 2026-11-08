"""Handler for Form Fill Plan Auditor (browser-form-fill-plan-auditor). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'prioritize', 'items': ['form fill plan step clarity', 'form fill plan fallback step', 'form fill plan data accuracy', 'form fill plan confirmation gate', 'form fill plan completion proof'], 'slug': 'browser-form-fill-plan-auditor', 'name': 'Form Fill Plan Auditor'}
def run(args):
    return run_engine(CONFIG, args or {})
