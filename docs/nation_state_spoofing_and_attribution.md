# docs/nation_state_spoofing_and_attribution.md

# Nation-State Spoofing, False Flags, and Attribution Evasion

Over the last year I refined these exact detection metrics through hands-on analysis of nation-state malware and live network captures. Nation-state APTs don't just use spoofing - they weaponize it to move like different hacking groups, creating attribution chaos.

## How Nation-States Use Spoofing (My Observations)
- **IP/TTL Spoofing**: Manipulate packet TTL and source IPs to make traffic appear from unrelated infrastructure.
- **Fingerprint Spoofing (JA3/JA4)**: Change TLS client fingerprints to mimic commodity malware or rival groups.
- **Behavioral Mimicry**: Rotate C2 patterns to look like Russian, Chinese, or Iranian groups interchangeably.

## Metrics I Built for Detection
- TTL anomaly threshold (tuned to 5 from my desktop/mobile tests)
- User-Agent entropy (low entropy = automated nation-state scripting)
- Attribution confusion score (tracks false-flag patterns)

This is what sets Sword apart - it doesn't just block; it thinks like me and calls out the spoof at nation-state power.

