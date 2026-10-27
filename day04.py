"""Gen AI in 60 Sec - Day 4: Dataset — AI ka Khana
Challenge: Dirty list mein 2 aur items daalo
Run free in Google Colab - no setup needed.
"""
raw = ["  Hello ", "HELLO", "", "AI  ", "ai"]
clean = []
for t in raw:
    t = t.strip().lower()
    if t and t not in clean:
        clean.append(t)
print(clean)
print(len(raw), "->", len(clean))
