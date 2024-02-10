import json

def convert_to_jsonl(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        # Read lines from the file
        lines = f.readlines()

    # Join lines into a single string
    data = ''.join(lines)

    # Split the input data into individual JSON objects
    json_objects = []
    current_json = ''
    for char in data:
        if char == '}':
            current_json += char
            json_objects.append(current_json)
            current_json = ''
        else:
            current_json += char

    with open(output_file, 'w', encoding='utf-8') as f:
        # Write each JSON object to a new line in the output file
        for obj in json_objects:
            f.write(obj.strip() + '\n')

# Replace 'input.json' and 'output.jsonl' with your input and output file paths
convert_to_jsonl('deduplicated_cocktails.jsonl', 'output.jsonl')
