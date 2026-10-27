"""Gen AI in 60 Sec - Day 26: Role Prompting
Challenge: Role badlo, jawab ka style dekho
Run free in Google Colab - no setup needed.
"""
task = "AI samjhao"
roles = ["Teacher", "Poet", "Pirate"]
for r in roles:
    p = f"Tum ek {r} ho. {task}."
    print(p)
print("role badla = style badli!")
