"""Handler for Newsletter Draft Drafter (email-newsletter-draft-drafter). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'template', 'items': ['newsletter draft priority accuracy', 'newsletter draft tone fit', 'newsletter draft facts supplied only', 'newsletter draft approval gate', 'newsletter draft next step clarity'], 'slug': 'email-newsletter-draft-drafter', 'name': 'Newsletter Draft Drafter'}
def run(args):
    return run_engine(CONFIG, args or {})
