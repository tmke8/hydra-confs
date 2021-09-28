# Generated by configen, do not edit.
# See https://github.com/facebookresearch/hydra/tree/master/tools/configen
# fmt: off
# isort:skip_file
# flake8: noqa

from dataclasses import dataclass, field
from typing import Any
from typing import Optional


@dataclass
class ExplainedVarianceConf:
    _target_: str = "pytorch_lightning.metrics.regression.ExplainedVariance"
    multioutput: str = "uniform_average"
    compute_on_step: bool = True
    dist_sync_on_step: bool = False
    process_group: Any = None
    dist_sync_fn: Any = None  # Callable


@dataclass
class MeanAbsoluteErrorConf:
    _target_: str = "pytorch_lightning.metrics.regression.MeanAbsoluteError"
    compute_on_step: bool = True
    dist_sync_on_step: bool = False
    process_group: Any = None
    dist_sync_fn: Any = None  # Callable


@dataclass
class MeanSquaredErrorConf:
    _target_: str = "pytorch_lightning.metrics.regression.MeanSquaredError"
    compute_on_step: bool = True
    dist_sync_on_step: bool = False
    process_group: Any = None
    dist_sync_fn: Any = None  # Callable


@dataclass
class MeanSquaredLogErrorConf:
    _target_: str = "pytorch_lightning.metrics.regression.MeanSquaredLogError"
    compute_on_step: bool = True
    dist_sync_on_step: bool = False
    process_group: Any = None
    dist_sync_fn: Any = None  # Callable