"""Handler for Prompt Injection Review Planner (safety-prompt-injection-review-planner). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'checklist', 'items': ['prompt injection review risk identified', 'prompt injection review approval required', 'prompt injection review least privilege', 'prompt injection review reversibility', 'prompt injection review audit logged'], 'slug': 'safety-prompt-injection-review-planner', 'name': 'Prompt Injection Review Planner'}
def run(args):
    return run_engine(CONFIG, args or {})
