"""Gen AI in 60 Sec - Day 34: Streaming — Word by Word
Challenge: Delay kam-zyada karke dekho
Run free in Google Colab - no setup needed.
"""
import time
reply = "ChatGPT ek ek word karke likhta hai"
for word in reply.split():
    print(word, end=" ", flush=True)
    time.sleep(0.2)
print()
print("streaming = turant dikhna")
