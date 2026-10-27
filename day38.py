"""Gen AI in 60 Sec - Day 38: Mini Project: Mini RAG Q&A
Challenge: Naya question + answer add karo
Run free in Google Colab - no setup needed.
"""
kb = {"fees": "5000 hai", "time": "7 baje"}
def retrieve(q):
    for key in kb:
        if key in q:
            return kb[key]
    return "pata nahi"
print(retrieve("fees kitni hai"))
print(retrieve("class ka time"))
print(retrieve("pizza"))
