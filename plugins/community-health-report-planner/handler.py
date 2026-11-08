"""Handler for Health Report Planner (community-health-report-planner). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'plan', 'items': ['health report member fit', 'health report tone fit', 'health report approval gate', 'health report safety check', 'health report follow up named'], 'slug': 'community-health-report-planner', 'name': 'Health Report Planner'}
def run(args):
    return run_engine(CONFIG, args or {})
