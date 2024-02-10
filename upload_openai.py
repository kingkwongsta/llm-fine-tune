import os
import requests
# Load the environment variables from the .env file
from dotenv import load_dotenv

load_dotenv()
# Get the API key from the environment
api_key = os.environ.get("OPENAI_API_KEY")

# Ensure the key is loaded
if not api_key:
    print("Error: OPENAI_API_KEY not found in .env file!")
    exit(1)

# Set the file path and purpose
file_path = "./data/cocktail_small.jsonl"  # Replace with the actual path to your file
purpose = "fine-tune"  # Options: "fine-tune" or "assistants"

# Open the file in binary mode
with open(file_path, "rb") as f:
    file_data = f.read()

# Prepare the request data
data = {
    "purpose": purpose,
}
files = {"file": (os.path.basename(file_path), file_data)}

# Set the API endpoint
url = "https://api.openai.com/v1/files"

# Set the authorization header
headers = {"Authorization": f"Bearer {api_key}"}

# Send the POST request
response = requests.post(url, headers=headers, data=data, files=files)

# Check for successful upload
if response.status_code == 200:
    data = response.json()
    print(f"File uploaded successfully! ID: {data['id']}")
else:
    print(f"Error uploading file: {response.status_code} - {response.text}")
