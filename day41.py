"""Gen AI in 60 Sec - Day 41: AI Agent kya hai?
Challenge: Goal badlo, agent ko chalao
Run free in Google Colab - no setup needed.
"""
goal, steps = "paani piyo", 0
todo = ["glass lo", "paani bharo", "piyo"]
while todo:
    action = todo.pop(0)
    steps += 1
    print("step", steps, ":", action)
print("goal poora:", goal)
