"""Handler for Nightly Backup Check Reporter (cron-nightly-backup-check-reporter). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'score', 'items': ['nightly backup check schedule clarity', 'nightly backup check delivery target', 'nightly backup check failure handling', 'nightly backup check idempotency', 'nightly backup check owner named'], 'slug': 'cron-nightly-backup-check-reporter', 'name': 'Nightly Backup Check Reporter'}
def run(args):
    return run_engine(CONFIG, args or {})
