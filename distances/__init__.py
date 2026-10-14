"""Provides functions for computing distances between two points."""
__all__ = ["chebyshev", "cosine", "euclid", "taxicab"]
from math import sqrt, hypot, sumprod
from typing import Final

def euclid(fst: tuple[float, ...], snd: tuple[float, ...]) -> float:
    """Computes the Euclidean distance between two points."""
    return sqrt(sum((dt := f - s) * dt for f, s in zip(fst, snd, strict=True)))

def taxicab(fst: tuple[float, ...], snd: tuple[float, ...]) -> float:
    """Computes the taxicab distance between two points."""
    return sum(abs(f - s) for f, s in zip(fst, snd, strict=True))

def chebyshev(fst: tuple[float, ...], snd: tuple[float, ...]) -> float:
    """Computes the Chebyshev distance between two points."""
    return max(abs(f - s) for f, s in zip(fst, snd, strict=True))

def cosine(fst: tuple[float, ...], snd: tuple[float, ...]) -> float:
    """Computes the cosine distance between two vectors."""
    return 1 - sumprod(fst, snd) / (hypot(*fst) * hypot(*snd))
    
