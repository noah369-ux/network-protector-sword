# src/nation_state_engine.py (updated for Round 4)
# ... (existing code) + new import and integration:
from .psychological_warfare_engine import PsychologicalWarfareEngine

class NationStateEngine:
    def __init__(self):
        self.psywar = PsychologicalWarfareEngine()
    # Integration calls added in methods... (full integration in real code)
