"""Handler for Allowlist Review Auditor (safety-allowlist-review-auditor). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'checklist', 'items': ['allowlist review risk identified', 'allowlist review approval required', 'allowlist review least privilege', 'allowlist review reversibility', 'allowlist review audit logged'], 'slug': 'safety-allowlist-review-auditor', 'name': 'Allowlist Review Auditor'}
def run(args):
    return run_engine(CONFIG, args or {})
