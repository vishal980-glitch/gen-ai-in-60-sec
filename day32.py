"""Gen AI in 60 Sec - Day 32: LLM API Call ka Structure
Challenge: Temperature badlo, request dekho
Run free in Google Colab - no setup needed.
"""
req = {"model": "gpt", "temperature": 0.7}
msg = {"role": "user", "content": "Hi"}
req["messages"] = [msg]
def fake_api(r):
    return {"reply": "Namaste! " + r["model"]}
resp = fake_api(req)
print(resp["reply"])
print(list(req.keys()))
