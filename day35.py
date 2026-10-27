"""Gen AI in 60 Sec - Day 35: Function Calling — Tools
Challenge: Ek naya tool function banao
Run free in Google Colab - no setup needed.
"""
def weather(c): return c + ": 30C"
tools = {"weather": weather}
call = {"name": "weather", "arg": "Delhi"}
fn = tools[call["name"]]
result = fn(call["arg"])
print("AI ne kaha:", call)
print("Tool ne diya:", result)
