"""Handler for Glossary Build Checker (rag-glossary-build-checker). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'template', 'items': ['glossary build source fidelity', 'glossary build retrieval relevance', 'glossary build citation coverage', 'glossary build freshness', 'glossary build gap honesty'], 'slug': 'rag-glossary-build-checker', 'name': 'Glossary Build Checker'}
def run(args):
    return run_engine(CONFIG, args or {})
