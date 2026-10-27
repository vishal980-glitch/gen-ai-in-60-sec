"""Gen AI in 60 Sec - Day 13: Gradient Descent
Challenge: Learning rate 0.01 karke dekho
Run free in Google Colab - no setup needed.
"""
w = 5.0
lr = 0.1
for step in range(30):
    grad = 2 * (w - 2)
    w = w - lr * grad
print("final w =", round(w, 2))
print("grad:", round(grad, 3))
print("steps:", step + 1)
