"""Handler for Prompt Injection Review Gate (safety-prompt-injection-review-gate). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'audit', 'items': ['prompt injection review risk identified', 'prompt injection review approval required', 'prompt injection review least privilege', 'prompt injection review reversibility', 'prompt injection review audit logged'], 'slug': 'safety-prompt-injection-review-gate', 'name': 'Prompt Injection Review Gate'}
def run(args):
    return run_engine(CONFIG, args or {})
