"""Gen AI in 60 Sec - Day 29: Prompt Template
Challenge: Role aur topic badal ke try karo
Run free in Google Colab - no setup needed.
"""
t = "Tum {role} ho. {topic} {n} line mein."
p1 = t.format(role="teacher", topic="AI", n=3)
p2 = t.format(role="poet", topic="Python", n=2)
print(p1)
print(p2)
print("ek template, hazaar prompts")
