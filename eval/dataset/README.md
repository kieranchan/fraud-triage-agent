# Test dataset

Labelled samples for the evaluation harness. **You need both positive (fraud/phishing)
and negative (legitimate) samples** — without negatives you can't compute a false-positive
rate.

## Candidate sources
| Source | Content | Use |
|--------|---------|-----|
| PhishTank | verified phishing URLs | URL positives (note: requires an account; feed can be flaky) |
| OpenPhish | phishing URL feed | URL positives (community feed is small) |
| UCI SMS Spam Collection | classic spam/scam SMS | text samples (⚠️ ~2011, UK-centric — dated vs. modern scam scripts) |
| Kaggle phishing datasets | phishing sites/URLs | train + test |
| **your own negatives** | legit site URLs, normal SMS | negatives (don't forget these!) |

## ⚠️ Ground-truth decay — read before building the set
Phishing URLs die fast. A URL that was malicious last week may be offline today, and a
live reputation lookup then returns "clean" → the agent says low-risk → you'd score it a
miss. That's a **data** problem, not a model problem.

**Mitigation:** at dataset-build time, snapshot each sample's tool responses into
`../fixtures/`. Offline eval replays those snapshots, so labels stay valid and metrics
reflect your code — not the current state of the live internet.

## Label scheme
Settle this before you start labelling (keep it consistent):
- binary `fraud` / `legit`, or
- 3-way `high` / `medium` / `low` (then decide how it maps to binary for FPR).
