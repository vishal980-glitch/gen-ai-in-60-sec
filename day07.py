"""Gen AI in 60 Sec - Day 7: Embeddings — Words ko Numbers
Challenge: Ek naya word + uske numbers add karo
Run free in Google Colab - no setup needed.
"""
emb = {
    "raja":  [0.9, 0.1],
    "rani":  [0.9, 0.9],
    "kutta": [0.1, 0.1],
}
print(emb["raja"])
print(round(emb["rani"][1] - emb["raja"][1], 1))
print(len(emb["kutta"]), "numbers")
