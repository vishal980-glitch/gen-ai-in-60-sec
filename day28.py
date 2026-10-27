"""Gen AI in 60 Sec - Day 28: Chain of Thought
Challenge: Apna ek step-by-step sawal banao
Run free in Google Colab - no setup needed.
"""
q = "Ram ke 3 aam, 2 aur mile, 1 khaya"
print("Direct:", 3 + 2 - 1)
steps = [3, 3 + 2, 3 + 2 - 1]
print("Step 1: shuru mein", steps[0])
print("Step 2: aur mile =", steps[1])
print("Step 3: khaya =", steps[2])
print("Soch ke bolo = sahi jawab")
