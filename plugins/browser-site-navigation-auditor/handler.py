"""Handler for Site Navigation Auditor (browser-site-navigation-auditor). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'classify', 'items': ['site navigation step clarity', 'site navigation fallback step', 'site navigation data accuracy', 'site navigation confirmation gate', 'site navigation completion proof'], 'slug': 'browser-site-navigation-auditor', 'name': 'Site Navigation Auditor'}
def run(args):
    return run_engine(CONFIG, args or {})
