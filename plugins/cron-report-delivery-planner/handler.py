"""Handler for Report Delivery Planner (cron-report-delivery-planner). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'prioritize', 'items': ['report delivery schedule clarity', 'report delivery delivery target', 'report delivery failure handling', 'report delivery idempotency', 'report delivery owner named'], 'slug': 'cron-report-delivery-planner', 'name': 'Report Delivery Planner'}
def run(args):
    return run_engine(CONFIG, args or {})
