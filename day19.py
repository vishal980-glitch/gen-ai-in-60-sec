"""Gen AI in 60 Sec - Day 19: Top-k Sampling
Challenge: k = 1 karo, kya hota hai?
Run free in Google Colab - no setup needed.
"""
p = {"hai": .5, "tha": .2, "hoon": .15}
p.update({"ghar": .1, "xyz": .05})
k = 3
top = sorted(p, key=p.get, reverse=True)[:k]
print("top-k:", top)
s = sum(p[w] for w in top)
print({w: round(p[w] / s, 2) for w in top})
