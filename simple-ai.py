import os
import time
from mistralai import Mistral

api_key = os.environ["MISTRAL_API_KEY"]
model = os.environ["MISTRAL_MODEL"]

client = Mistral(api_key=api_key)


prompt = "given search criteria on (make, model, color, options) what would this search translate into 'Find me a corvette with leather seats'"

start_time = time.time()
chat_response = client.chat.complete(
    model= model,
    messages = [
        {
            "role": "user",
            "content": prompt,
        },
    ]
)
end_time = time.time()

print(chat_response.choices[0].message.content)

execution_time = end_time - start_time
print(f"Execution time: {execution_time:.6f} seconds")



prompt = "given search criteria on (make, model, color, options) what would this search translate into 'Find me a family friendly SUV with leather seats and good millage'"

start_time = time.time()
chat_response = client.chat.complete(
    model= model,
    messages = [
        {
            "role": "user",
            "content": prompt,
        },
    ]
)
end_time = time.time()

print(chat_response.choices[0].message.content)

execution_time = end_time - start_time
print(f"Execution time: {execution_time:.6f} seconds")
