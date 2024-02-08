import os
import requests
import json
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
        {"role": "system", "content": "You are a helpful mixologist designed to output JSON"},
        {"role": "user", "content": "create a unique cocktail based on the user preferences in the text delimited by triple periods, ensure the drink name doesn't use the same/similar words to Comforting,Sour,Vodka, JSON output should contain: name, ingredients (array of key-value pairs with name and quantity), instructions....contains Tequila and emphasizes a Sour flavor profile for a Comforting mood..."}
    ]
)

message = completion.choices[0].message

# Access the JSON-formatted text content
json_text = message.content

# Check if the content is valid JSON
try:
    json_data = json.loads(json_text)
    
    # Print the parsed JSON data
    print(json.dumps(json_data, indent=4))  # Pretty-print the JSON
except json.JSONDecodeError:
    print("Error: Message content is not valid JSON.")