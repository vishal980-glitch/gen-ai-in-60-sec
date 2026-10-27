"""Gen AI in 60 Sec - Day 11: Layers — Network Banao
Challenge: Ek aur layer add karo
Run free in Google Colab - no setup needed.
"""
from operator import mul
def dot(a, b): return sum(map(mul, a, b))
W1 = [[0.5, -1], [1, 1]]
h = [max(0, dot([1, 2], r)) for r in W1]
W2 = [1, 2]
out = dot(h, W2)
print("hidden:", h)
print("output:", out)
