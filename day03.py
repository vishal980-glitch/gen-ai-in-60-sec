"""Gen AI in 60 Sec - Day 3: Training vs Inference
Challenge: w ki starting value 5 karo
Run free in Google Colab - no setup needed.
"""
w = 0.0
data = [(1, 2), (2, 4), (3, 6)]
for epoch in range(50):
    for x, y in data:
        w += 0.02 * (y - w * x) * x
print("trained w =", round(w, 2))
def predict(x): return w * x
print("predict(10) =", round(predict(10)))
