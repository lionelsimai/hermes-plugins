"""Handler for Table Scrape Plan Reporter (browser-table-scrape-plan-reporter). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'template', 'items': ['table scrape plan step clarity', 'table scrape plan fallback step', 'table scrape plan data accuracy', 'table scrape plan confirmation gate', 'table scrape plan completion proof'], 'slug': 'browser-table-scrape-plan-reporter', 'name': 'Table Scrape Plan Reporter'}
def run(args):
    return run_engine(CONFIG, args or {})
