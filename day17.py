"""Gen AI in 60 Sec - Day 17: Softmax — Probability
Challenge: Scores badlo, probabilities dekho
Run free in Google Colab - no setup needed.
"""
import math
scores = [2.0, 1.0, 0.1]
exps = [math.exp(s) for s in scores]
total = sum(exps)
probs = [e / total for e in exps]
print([round(p, 2) for p in probs])
print("sum =", round(sum(probs), 2))
print("top =", probs.index(max(probs)))
