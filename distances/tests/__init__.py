"""Tests for the distances library."""
__all__ = ["TestDistances"]
import distances
from math import dist
from typing import override
import unittest

class TestDistances(unittest.TestCase):
    @override
    def setUp(self) -> None:
        self.fst = (2.72, 2.02, 7.70)
        self.snd = (1.99, 8.48, 4.21)

    def test_euclid(self) -> None:
        self.assertAlmostEqual(
            distances.euclid(self.fst, self.snd), dist(self.fst, self.snd), 2
        )

    def test_taxicab(self) -> None:
        self.assertAlmostEqual(
            distances.taxicab(self.fst, self.snd), 10.68, 2
        )

    def test_chebyshev(self) -> None:
        self.assertAlmostEqual(
            distances.chebyshev(self.fst, self.snd), 6.46, 2
        )

    def test_cosine(self) -> None:
        self.assertAlmostEqual(
            distances.cosine(self.fst, self.snd), .32, 2
        )
