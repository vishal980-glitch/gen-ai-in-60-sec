"""Gen AI in 60 Sec - Day 5: Tokens kya hote hain?
Challenge: Apna ek sentence tokens mein split karo
Run free in Google Colab - no setup needed.
"""
text = "ai seekho, ai banao"
vocab = {}
tokens = text.replace(",", "").split()
for t in tokens:
    if t not in vocab:
        vocab[t] = len(vocab)
ids = [vocab[t] for t in tokens]
print(vocab, ids)
