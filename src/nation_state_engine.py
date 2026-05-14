# Updated nation_state_engine.py (integrating spoofing)
# ... (previous content) + new import and calls

from .spoofing_detector import NationStateSpoofingDetector

class NationStateEngine:
    def __init__(self):
        self.spoof_detector = NationStateSpoofingDetector()
        # ... rest of previous code

    def analyze_packet(self, packet):
        spoof_alert = self.spoof_detector.detect_spoofing(packet)
        if spoof_alert:
            print(f'[NATION-STATE SPOOF ALERT] {spoof_alert["description"]}')
        false_flag = self.spoof_detector.identify_false_flag(packet)
        if false_flag:
            print(f'[FALSE FLAG DETECTED] {false_flag["details"]}')
        # ... existing analysis
        return spoof_alert or false_flag

# This update makes Sword detect exactly how nation-states spoof, false-flag, and move between group identities.
