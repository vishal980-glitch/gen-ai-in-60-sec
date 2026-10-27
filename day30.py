"""Gen AI in 60 Sec - Day 30: Structured Output — JSON
Challenge: JSON mein ek naya key add karo
Run free in Google Colab - no setup needed.
"""
import json
reply = '{"naam": "Ravi", "umar": 25}'
data = json.loads(reply)
print(data["naam"])
print(data["umar"] + 1)
print(type(data).__name__)
print("JSON = code ke liye safe format")
