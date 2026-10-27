"""Gen AI in 60 Sec - Day 42: Agent with Tools — Calculator
Challenge: Multiply tool bhi add karo
Run free in Google Colab - no setup needed.
"""
def add(a, b): return a + b
def mul(a, b): return a * b
tools = {"add": add, "mul": mul}
plan = [("add", 2, 3), ("mul", 5, 4)]
for name, a, b in plan:
    r = tools[name](a, b)
    print(name, a, b, "=", r)
print("agent ne tools chalaye")
