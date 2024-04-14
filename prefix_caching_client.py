from openai import OpenAI
import time

# Modify OpenAI's API key and API base to use vLLM's API server.
openai_api_key = "EMPTY"
openai_api_base = "http://localhost:8000/v1"

client = OpenAI(
    api_key=openai_api_key,
    base_url=openai_api_base,
)

models = client.models.list()
model = models.data[0].id

N = 256
N_REQUESTS = 10

for idx in range(N_REQUESTS):
    
    start = time.perf_counter()
    completion = client.completions.create(
        prompt="Hello_"*N,
        max_tokens=20,
    )
    end = time.perf_counter()

    print(f"Iteration {idx}: {end - start :0.4f}s")

print("Chat completion results:")
print(chat_completion)
