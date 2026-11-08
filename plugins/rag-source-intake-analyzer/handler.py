"""Handler for Source Intake Analyzer (rag-source-intake-analyzer). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'template', 'items': ['source intake source fidelity', 'source intake retrieval relevance', 'source intake citation coverage', 'source intake freshness', 'source intake gap honesty'], 'slug': 'rag-source-intake-analyzer', 'name': 'Source Intake Analyzer'}
def run(args):
    return run_engine(CONFIG, args or {})
