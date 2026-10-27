"""Gen AI in 60 Sec - Day 31: System Prompt vs User Prompt
Challenge: System prompt ki language badlo
Run free in Google Colab - no setup needed.
"""
sys_p = "Tum Hinglish mein bolte ho"
user_p = "AI kya hai?"
messages = [("system", sys_p), ("user", user_p)]
for role, text in messages:
    print(role.upper(), ":", text)
print("system = niyam, user = sawaal")
