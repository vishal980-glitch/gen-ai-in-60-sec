"""Gen AI in 60 Sec - Day 16: Mini Project: AND Gate Neuron
Challenge: AND ki jagah OR gate train karo
Run free in Google Colab - no setup needed.
"""
data = [(0,0,0), (0,1,0), (1,0,0), (1,1,1)]
w1 = w2 = b = 0
for _ in range(20):
    for x1, x2, y in data:
        p = int(w1*x1 + w2*x2 + b > 0)
        w1 += (y - p) * x1
        w2 += (y - p) * x2
        b += y - p
print(w1, w2, b)
print("AND gate seekh liya!")
