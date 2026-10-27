"""Gen AI in 60 Sec - Day 22: Transformer ka Idea
Challenge: Attention ke baad ek aur step add karo
Run free in Google Colab - no setup needed.
"""
def attention(x): return x + 1
def feed(x): return x * 2
x = 1
for layer in range(3):
    x = attention(x)
    x = feed(x)
    print("layer", layer + 1, "->", x)
print("attention + feed, repeat!")
