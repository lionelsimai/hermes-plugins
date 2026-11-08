"""Handler for Source Shortlist Extractor (web-source-shortlist-extractor). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'template', 'items': ['source shortlist source quality', 'source shortlist recency', 'source shortlist corroboration', 'source shortlist citation completeness', 'source shortlist scope fit'], 'slug': 'web-source-shortlist-extractor', 'name': 'Source Shortlist Extractor'}
def run(args):
    return run_engine(CONFIG, args or {})
