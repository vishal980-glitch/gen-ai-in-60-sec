"""Gen AI in 60 Sec - Day 24: Mini Project: Text Generator
Challenge: Seed badlo, naya text generate karo
Run free in Google Colab - no setup needed.
"""
import random
random.seed(7)
corpus = "ai seekho ai banao ai bechho".split()
m = {}
for a, b in zip(corpus, corpus[1:]):
    m.setdefault(a, []).append(b)
word, out = "ai", []
for _ in range(6):
    out.append(word)
    word = random.choice(m.get(word, ["ai"]))
print(" ".join(out))
