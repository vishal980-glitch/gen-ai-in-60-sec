"""Gen AI in 60 Sec - Day 39: Image Generation Kaise Hoti Hai?
Challenge: Seed badlo, naya noise dekho
Run free in Google Colab - no setup needed.
"""
from random import randint, seed
seed(1)
img = [10, 20, 30, 40]
x = [p + randint(-50, 50) for p in img]
print("noise:", x)
for _ in range(3):
    x = [(a + b) / 2 for a, b in zip(x, img)]
print("saaf:", [round(v) for v in x])
