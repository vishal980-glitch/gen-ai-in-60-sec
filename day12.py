"""Gen AI in 60 Sec - Day 12: Loss — Error Measure
Challenge: Prediction ki values badlo, loss dekho
Run free in Google Colab - no setup needed.
"""
y_true = [1, 0, 1, 1]
y_pred = [0.9, 0.2, 0.4, 1.0]
total = 0
for t, p in zip(y_true, y_pred):
    total += (t - p) ** 2
loss = total / len(y_true)
print("loss =", round(loss, 3))
print("0 = perfect model")
