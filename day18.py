"""Gen AI in 60 Sec - Day 18: Temperature — Creativity Knob
Challenge: Temperature 0.1 aur 2 try karo
Run free in Google Colab - no setup needed.
"""
import math
def soft(s, t):
    e = [math.exp(x / t) for x in s]
    return [round(v / sum(e), 2) for v in e]
scores = [2.0, 1.0, 0.5]
print("t=0.5:", soft(scores, 0.5))
print("t=1.0:", soft(scores, 1.0))
print("t=2.0:", soft(scores, 2.0))
