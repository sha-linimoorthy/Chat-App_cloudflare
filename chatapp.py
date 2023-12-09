import requests


API_BASE_URL = "https://api.cloudflare.com/client/v4/accounts/ACCOUNT_ID/ai/run/"
headers = {"Authorization": f"Bearer {API_TOKEN}"}

def run(model, inputs):
    input = { "messages": inputs }
    response = requests.post(f"{API_BASE_URL}{model}", headers=headers, json=input)
    return response.json()


inputs = [
    { "role": "system", "content": "You are a friendly assistant that helps write stories" },
    { "role": "user", "content": "Write a short story about a MLH global hack week"}
];
output = run("@cf/meta/llama-2-7b-chat-int8", inputs)
print(output)
