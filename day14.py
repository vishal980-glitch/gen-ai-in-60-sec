"""Gen AI in 60 Sec - Day 14: Training Loop — Epochs
Challenge: Epochs 500 karo, w kahan pahunchta hai?
Run free in Google Colab - no setup needed.
"""
w = b = 0.0
data = [(0, 1), (1, 4), (2, 7)]
for epoch in range(500):
    for x, y in data:
        e = (w * x + b) - y
        w -= 0.05 * e * x
        b -= 0.05 * e
print(round(w, 2), round(b, 2))
