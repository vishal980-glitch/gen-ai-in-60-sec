"""Gen AI in 60 Sec - Day 21: Attention — Kis Word Pe Focus
Challenge: Query vector badlo, focus dekho
Run free in Google Colab - no setup needed.
"""
import math
nadi, paisa = [1, 0], [0, 1]
q = [0.9, 0.1]
s1 = q[0]*nadi[0] + q[1]*nadi[1]
s2 = q[0]*paisa[0] + q[1]*paisa[1]
e1, e2 = math.exp(s1), math.exp(s2)
print("nadi  :", round(e1 / (e1 + e2), 2))
print("paisa :", round(e2 / (e1 + e2), 2))
