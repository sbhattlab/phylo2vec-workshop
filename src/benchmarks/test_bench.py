"""Example benchmarks."""

import pytest

import phylo2vec as p2v

from src.example import fibonacci

# 100, 200, ..., 900
BENCHMARK_RANGE = range(100, 1000, 100)


# Test the fibonacci function
@pytest.mark.parametrize("sample_size", BENCHMARK_RANGE)
def test_fibonacci(benchmark, sample_size):
    benchmark(fibonacci, sample_size)


# Test the sample_vector function from phylo2vec
@pytest.mark.parametrize("sample_size", BENCHMARK_RANGE)
def test_p2v_sample_vector(benchmark, sample_size):
    benchmark(p2v.sample_vector, sample_size)
