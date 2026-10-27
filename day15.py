"""Gen AI in 60 Sec - Day 15: Overfitting kya hai?
Challenge: Train data mein ek aur example daalo
Run free in Google Colab - no setup needed.
"""
train = {"cat": 1, "dog": 0}
test = {"cat": 1, "tiger": 1}
def memorize(x): return train.get(x, 0)
def general(x): return int("t" in x)
for x in test:
    print(x, memorize(x), general(x))
print("sahi:", test)
print("memorize: naya data fail!")
