"""Handler for Gateway Health Summarizer (messaging-gateway-health-summarizer). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'audit', 'items': ['gateway health audience fit', 'gateway health tone fit', 'gateway health length fit', 'gateway health approval gate', 'gateway health platform fit'], 'slug': 'messaging-gateway-health-summarizer', 'name': 'Gateway Health Summarizer'}
def run(args):
    return run_engine(CONFIG, args or {})
