"""Handler for Site Navigation Checker (browser-site-navigation-checker). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'analyze', 'items': ['site navigation step clarity', 'site navigation fallback step', 'site navigation data accuracy', 'site navigation confirmation gate', 'site navigation completion proof'], 'slug': 'browser-site-navigation-checker', 'name': 'Site Navigation Checker'}
def run(args):
    return run_engine(CONFIG, args or {})
