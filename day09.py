"""Gen AI in 60 Sec - Day 9: Neuron — Weights aur Bias
Challenge: Input aur weight ki value badlo
Run free in Google Colab - no setup needed.
"""
def neuron(x, w, b):
    return x * w + b
w, b = 2, 1
print(neuron(1, w, b))
print(neuron(2, w, b))
print(neuron(3, w, b))
print(neuron(10, w, b))
print("w = importance, b = bias")
