"""Gen AI in 60 Sec - Day 33: Chatbot Memory
Challenge: History mein 3 messages add karo
Run free in Google Colab - no setup needed.
"""
history = []
def chat(msg):
    history.append(("user", msg))
    reply = f"yaad: {len(history)} msgs"
    history.append(("bot", reply))
    return reply
print(chat("hi"))
print(chat("naam batao"))
