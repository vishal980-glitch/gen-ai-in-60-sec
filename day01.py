"""Gen AI in 60 Sec - Day 1: Generative AI kya hai?
Challenge: Data mein apna ek sentence add karo
Run free in Google Colab - no setup needed.
"""
text = "main code likh raha hoon"
text += " main app bana raha hoon"
words = text.split()
nxt = {}
for a, b in zip(words, words[1:]):
    nxt.setdefault(a, []).append(b)
print("main →", nxt["main"])
print("raha →", nxt["raha"])
