"""Handler for Form Fill Plan Sequencer (browser-form-fill-plan-sequencer). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'score', 'items': ['form fill plan step clarity', 'form fill plan fallback step', 'form fill plan data accuracy', 'form fill plan confirmation gate', 'form fill plan completion proof'], 'slug': 'browser-form-fill-plan-sequencer', 'name': 'Form Fill Plan Sequencer'}
def run(args):
    return run_engine(CONFIG, args or {})
