"""Gen AI in 60 Sec - Day 36: Semantic Search
Challenge: Ek aur doc add karo, search karo
Run free in Google Colab - no setup needed.
"""
docs = {"python": [1, 0], "pizza": [0, 1]}
q = [0.9, 0.2]
def sim(a, b): return a[0]*b[0] + a[1]*b[1]
best = max(docs, key=lambda d: sim(q, docs[d]))
print("sawaal vector:", q)
print("best match:", best)
