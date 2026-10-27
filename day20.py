"""Gen AI in 60 Sec - Day 20: Bigram Language Model
Challenge: Apna sentence daalo, model ko train karo
Run free in Google Colab - no setup needed.
"""
w = "ai seekho ai banao ai seekho".split()
pairs = list(zip(w, w[1:]))
print(pairs[:3])
n = sum(1 for a, b in pairs if a == "ai")
for nxt in ("seekho", "banao"):
    c = pairs.count(("ai", nxt))
    print("ai ->", nxt, round(c / n, 2))
