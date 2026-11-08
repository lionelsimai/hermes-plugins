"""Handler for Report Delivery Scheduler Review (cron-report-delivery-scheduler-review). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'template', 'items': ['report delivery schedule clarity', 'report delivery delivery target', 'report delivery failure handling', 'report delivery idempotency', 'report delivery owner named'], 'slug': 'cron-report-delivery-scheduler-review', 'name': 'Report Delivery Scheduler Review'}
def run(args):
    return run_engine(CONFIG, args or {})
