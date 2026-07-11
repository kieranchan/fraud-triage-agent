"""Classification metrics for the triage eval.

Implement these by hand at least once — computing precision/recall/FPR from the
confusion matrix is exactly the understanding an interviewer will probe. You can reach
for scikit-learn later for convenience, but do the arithmetic yourself first.

Reminder on what matters here (anti-fraud framing):
  - Recall = of the truly-fraudulent, how many did we catch? -> the metric you weight most.
  - Precision = of those we flagged, how many were really fraud? -> relates to false alarms.
  - FPR = of the legit messages, how many did we wrongly flag? -> needs negatives in the set.
  - "宁误报不漏报": bias toward high recall, but be able to state the cost (FPR rises) and
    how you'd manage it (threshold, human-review layer).
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Metrics:
    accuracy: float
    precision: float
    recall: float
    fpr: float
    tp: int
    fp: int
    tn: int
    fn: int


def compute(y_true: list[str], y_pred: list[str], *, positive: str = "fraud") -> Metrics:
    """Compute the confusion matrix and derived metrics.

    TODO(you): implement. Steps:
      - decide how multi-class (high/med/low) maps to the binary fraud/legit split, or
        keep the labels binary from the start.
      - count TP/FP/TN/FN against `positive`.
      - derive accuracy / precision / recall / FPR (guard against divide-by-zero).
    """
    raise NotImplementedError


def print_confusion_matrix(m: Metrics) -> None:
    """Pretty-print the TP/FP/TN/FN grid. TODO(you)."""
    raise NotImplementedError
