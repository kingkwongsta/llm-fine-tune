import json

def remove_duplicates(filename):
  """
  Removes duplicate entries from a JSON file based on the "content" field.

  Args:
    filename: The path to the JSON file.

  Returns:
    A list of unique entries.
  """
  with open(filename, "r", encoding="utf-8") as f:  # Use UTF-8 encoding for reading
    data_list = json.load(f)

  seen_content = set()
  unique_entries = []
  for entry in data_list:
    content = entry["messages"][2]["content"]
    if content not in seen_content:
      seen_content.add(content)
      unique_entries.append(entry)

  return unique_entries

# Example usage
unique_entries = remove_duplicates("data/CONVERTED_DATA.jsonl")

# Save the deduplicated data to a new file
with open("deduplicated_data.json", "w", encoding="utf-8") as f:  # Use UTF-8 encoding for writing
  json.dump(unique_entries, f, indent=4)

print("Deduplication complete!")
