# flake8: noqa
# There's no way to ignore "F401 '...' imported but unused" warnings in this
# module, but to preserve other warnings. So, don't check this module at all.

from ..file_utils import is_tf_available, is_torch_available


if is_torch_available():
    from .benchmark_args import PyTorchBenchmarkArguments
    from .benchmark import PyTorchBenchmarks

if is_tf_available():
    from .benchmark_tf_args import TensorflowBenchmarkArguments
