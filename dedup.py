import json

def dedup_cocktails(input_file, output_file):
  """
  Deduplicates rows in a .jsonl file based on cocktail name and content.

  Args:
    input_file: The path to the input .jsonl file.
    output_file: The path to the output .jsonl file.
  """
  seen_cocktails = set()
  unique_entries = []
  with open(input_file, "r", encoding="utf-8") as f, open(output_file, "w", encoding="utf-8") as out:
    for line in f:
      entry = json.loads(line)
      cocktail_name = entry["messages"][1]["content"]
      content = entry["messages"][2]["content"]
      key = (cocktail_name, content)
      if key not in seen_cocktails:
        seen_cocktails.add(key)
        unique_entries.append(entry)
        json.dump(entry, out, ensure_ascii=False, indent=4)

  print(f"Deduplicated {len(unique_entries)} entries. Saved to {output_file}")

# Example usage
input_file = "data/CONVERTED_DATA.jsonl"
output_file = "deduplicated_cocktails.jsonl"
dedup_cocktails(input_file, output_file)
