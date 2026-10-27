"""Gen AI in 60 Sec - Day 25: Achha Prompt vs Bura Prompt
Challenge: Apna ek prompt score karo
Run free in Google Colab - no setup needed.
"""
def score(p):
    s = 0
    s += len(p.split()) > 5
    s += "line" in p or "word" in p
    s += "beginner" in p or "student" in p
    return s
bad = "python"
good = "beginner ke liye python 5 line mein"
print("bad :", score(bad))
print("good:", score(good))
