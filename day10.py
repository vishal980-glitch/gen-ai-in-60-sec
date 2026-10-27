"""Gen AI in 60 Sec - Day 10: Activation Function
Challenge: Input ko negative karke dekho
Run free in Google Colab - no setup needed.
"""
import math
def relu(x): return max(0, x)
def sigmoid(x):
    return 1 / (1 + math.exp(-x))
print(relu(-3), relu(5))
print(round(sigmoid(0), 2))
print(round(sigmoid(5), 2))
print(round(sigmoid(-5), 2))
