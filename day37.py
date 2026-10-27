"""Gen AI in 60 Sec - Day 37: RAG — Apna Data AI Ko Do
Challenge: kb mein ek aur fact add karo
Run free in Google Colab - no setup needed.
"""
kb = ["Python: 1991", "Java: 1995"]
q = "Python kab bani"
hit = [d for d in kb if "Python" in d][0]
prompt = f"Context: {hit}. Sawaal: {q}"
print(prompt)
print("AI ab sahi jawab dega!")
