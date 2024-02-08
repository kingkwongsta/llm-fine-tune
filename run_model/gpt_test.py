import os
import requests
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env file
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
env_path = os.path.join(root_dir, ".env")
load_dotenv(env_path)

# Get API key from environment
api_key = os.environ.get("OPENAI_API_KEY")

# Check if API key is loaded
if not api_key:
    print("Error: OPENAI_API_KEY not found in .env file!")
    exit(1)

# Create OpenAI client
client = OpenAI(api_key=api_key)

# Define chat completion request
completion = client.chat.completions.create(
  model="ft:gpt-3.5-turbo-1106:personal::8ppzPj3k",
    messages=[
        {"role": "system", "content": "You are an expert mixologist providing drink recipies"},
        {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
    ]
)

# Print the generated poem
print(completion.choices[0].message)
