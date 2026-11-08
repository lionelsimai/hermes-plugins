"""Handler for Booking Flow Checker (browser-booking-flow-checker). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'classify', 'items': ['booking flow step clarity', 'booking flow fallback step', 'booking flow data accuracy', 'booking flow confirmation gate', 'booking flow completion proof'], 'slug': 'browser-booking-flow-checker', 'name': 'Booking Flow Checker'}
def run(args):
    return run_engine(CONFIG, args or {})
