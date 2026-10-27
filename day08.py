"""Gen AI in 60 Sec - Day 8: Cosine Similarity
Challenge: Dono vectors ke numbers badlo
Run free in Google Colab - no setup needed.
"""
import math
def cos(a, b):
    dot = sum(x*y for x, y in zip(a, b))
    na = math.sqrt(sum(x*x for x in a))
    nb = math.sqrt(sum(y*y for y in b))
    return dot / (na * nb)
print(round(cos([1, 2], [2, 4]), 2))
print(round(cos([1, 0], [0, 1]), 2))
