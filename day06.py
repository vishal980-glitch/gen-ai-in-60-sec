"""Gen AI in 60 Sec - Day 6: Context Window kya hai?
Challenge: limit 3 karo, dekho kya bachta hai
Run free in Google Colab - no setup needed.
"""
limit = 5
chat = "ek do teen char paanch chhe saat"
tokens = chat.split()
print("total:", len(tokens))
if len(tokens) > limit:
    tokens = tokens[-limit:]
print("model ko dikha:", tokens)
print("bhoola:", len(chat.split()) - limit)
