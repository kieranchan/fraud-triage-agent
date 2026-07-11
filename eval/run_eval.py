"""Batch-run the agent over the labelled test set and compute metrics.

This is the Week-3 centrepiece — the part that separates this from a demo. Run it in
OFFLINE mode (tools read from eval/fixtures/) so results are reproducible and free:
the numbers reflect your code changes, not external-API drift.

Usage (once implemented):
    python -m eval.run_eval
"""
from __future__ import annotations


def run() -> None:
    """Load the dataset, run the agent on each sample (offline), collect predictions.

    TODO(you): implement. The pipeline:
      1. load labelled samples from eval/dataset/ (each: input + true label high/med/low
         or fraud/legit — settle your label scheme first).
      2. for each sample, run the agent with offline=True so tools hit fixtures.
      3. collect predicted vs. true labels.
      4. hand them to metrics.compute() and print the report + confusion matrix.
      5. (optional) run judge.score() on the rationales for a quality signal.
      6. save a timestamped report so you can compare runs across prompt tweaks.

    Remember: a sample is only usable offline if its tool responses were snapshotted
    into eval/fixtures/ at dataset-build time.
    """
    raise NotImplementedError


if __name__ == "__main__":
    run()
