"""Gen AI in 60 Sec - Day 2: AI vs ML vs Deep Learning
Challenge: Spam rule mein ek naya word add karo
Run free in Google Colab - no setup needed.
"""
def rule(m): return "free" in m
data = ["free gift", "win money"]
seen = set(" ".join(data).split())
def ml(m):
    return bool(seen & set(m.split()))
print("rule:", rule("win cash"))
print("ml  :", ml("win cash"))
print("ml  :", ml("hello bro"))
