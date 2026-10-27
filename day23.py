"""Gen AI in 60 Sec - Day 23: Hallucination Kyun Hoti Hai?
Challenge: facts mein ek naya fact daalo
Run free in Google Colab - no setup needed.
"""
facts = {"india capital": "Delhi"}
def ai(q):
    if q in facts:
        return facts[q]
    return "Mumbai"
print(ai("india capital"))
print(ai("mars capital"))
print("AI ne confident jhooth bola!")
