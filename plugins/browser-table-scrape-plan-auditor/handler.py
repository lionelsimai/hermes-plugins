"""Handler for Table Scrape Plan Auditor (browser-table-scrape-plan-auditor). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'score', 'items': ['table scrape plan step clarity', 'table scrape plan fallback step', 'table scrape plan data accuracy', 'table scrape plan confirmation gate', 'table scrape plan completion proof'], 'slug': 'browser-table-scrape-plan-auditor', 'name': 'Table Scrape Plan Auditor'}
def run(args):
    return run_engine(CONFIG, args or {})
