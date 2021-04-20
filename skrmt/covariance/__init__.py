"""
The :mod:`skrmt.covariance` module implements different methods
to estimate covariance matrices.
"""

from .analytical_shrinkage import AnalyticalShrinkage
from .linear_shrinkage import LinearShrinkage
from .estimator import SampleEstimator, FSOptEstimator

from .metrics import loss_mv, loss_frobenius


__all__ = ["AnalyticalShrinkage", "LinearShrinkage",
           "SampleEstimator", "FSOptEstimator",
           "loss_mv", "loss_frobenius"]