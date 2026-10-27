"""Gen AI in 60 Sec - Day 43: AI Safety aur Bias
Challenge: Data mein ek aur example daalo
Run free in Google Colab - no setup needed.
"""
data = ["dr: he", "dr: he", "dr: she"]
count = {}
for line in data:
    g = line.split(": ")[1]
    count[g] = count.get(g, 0) + 1
print(count)
print("zyada 'he' = AI bhi 'he' bolega")
print("data mein bias = AI mein bias")
