"""Gen AI in 60 Sec - Day 27: Few-Shot Prompting
Challenge: Ek aur example (shot) add karo
Run free in Google Colab - no setup needed.
"""
shots = ["bahut badhiya -> positive"]
shots.append("bekaar tha -> negative")
shots.append("mazaa aa gaya ->")
for s in shots:
    print(s)
print("AI pattern dekh ke bharega")
