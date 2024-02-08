import json

# Define the input data
data = {
    "title": "Mamie Taylor",
    "ingredients": ["2 ounces blended scotch", "1/2 ounce fresh lime juice", "3 to 5 ounces chilled ginger ale", "Lemon slice"],
    "directions": [],
    "misc": [],
    "source": "Jim Meehan",
    "ner": ["cocchi americano", "pernod", "tequila"],
}

# Create the desired output format
output = {
    "messages": [
        {"role": "system", "content": "You are a helpful mixologist designed to output JSON"},
        {"role": "user", "content": "What are the ingredients of a Mamie Taylor"},
        {"role": "assistant", "content": ", ".join(data["ingredients"])},
    ],
}

# Print the converted JSON data
print(json.dumps(output, indent=4))
