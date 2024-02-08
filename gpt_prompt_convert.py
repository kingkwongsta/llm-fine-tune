import json

# Set the input file path
input_file = "./data/output_cocktail.jsonl"

# Open the input file
with open(input_file, "r") as f:
    # Read each line as a JSON object
    data_list = [json.loads(line) for line in f]

# Process each entry and create output list
output_list = []
for entry in data_list:
    # Create the desired output format
    output = {
        "messages": [
            {"role": "system", "content": "You are a helpful mixologist designed to output JSON"},
            {"role": "user", "content": f"What are the ingredients of a {entry['title']}"},
            {"role": "assistant", "content": ", ".join(entry["ingredients"])},
        ],
    }
    # Append the formatted entry to the output list
    output_list.append(output)

# Set the output file path
output_file = "CONVERTED_DATA.jsonl"

# Open the output file with UTF-8 encoding
with open(output_file, "w", encoding="utf-8") as f:  # Added encoding="utf-8"
    # Write each entry to the file on a single line
    for entry in output_list:
        json.dump(entry, f, ensure_ascii=False)
        f.write("\n")

print(f"Successfully converted data from {input_file} and saved to {output_file}")
