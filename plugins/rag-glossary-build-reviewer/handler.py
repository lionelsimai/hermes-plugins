"""Handler for Glossary Build Reviewer (rag-glossary-build-reviewer). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'analyze', 'items': ['glossary build source fidelity', 'glossary build retrieval relevance', 'glossary build citation coverage', 'glossary build freshness', 'glossary build gap honesty'], 'slug': 'rag-glossary-build-reviewer', 'name': 'Glossary Build Reviewer'}
def run(args):
    return run_engine(CONFIG, args or {})
