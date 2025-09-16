import numpy as np
import phylo2vec as p2v
import pytest

from src.example import fibonacci


# Test function for `fibonacci`
def test_fibonacci():
    assert fibonacci(10) == 55
    assert fibonacci(20) == 6765
    assert fibonacci(30) == 832040


# Test function for `fibonacci`
def test_fail_fibonacci():
    assert fibonacci(10) == 54  # This test is expected to fail


@pytest.mark.parametrize("n_leaves", range(5, 50))
def test_from_and_to_newick(n_leaves):
    v = p2v.sample_vector(n_leaves)
    newick = p2v.to_newick(v)
    v2 = p2v.from_newick(newick)
    assert np.array_equal(v, v2)
