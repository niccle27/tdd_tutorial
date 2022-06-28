from unittest.mock import Mock
from unittest import TestCase
from compute_stats_refactoring import compute_harmonic_mean, compute_variance, compute_standard_deviation

class TestComputeStats(TestCase):
    def test_compute_harmonic_mean(self):
        harmonic_mean = compute_harmonic_mean([1,4,4])
        self.assertEqual(harmonic_mean, 2)
    def test_compute_variance(self):
        variance = compute_variance([5, 6, 1])
        self.assertEqual(variance, 7)
    def test_compute_standard_dev(self):
        std = compute_standard_deviation([5, 6, 1])
        self.assertAlmostEqual(std, 2.645, delta=0.001)