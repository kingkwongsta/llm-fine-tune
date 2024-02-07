import replicate
import os

os.environ["REPLICATE_API_TOKEN"] = "r8_K6KZlb4R1mKTxhCnvTh5iP8OOlJ5OA53vE1QZ"


input = {
    'train_data': "https://raw.githubusercontent.com/kingkwongsta/file-storage/main/output_cocktail.jsonl"
}


training = replicate.trainings.create(
  version="meta/llama-2-7b-chat:13c3cdee13ee059ab779f0291d29054dab00a47dad8261375654de5540165fb0",
  input=input,
  destination="kingkwongsta/test"
)

print(training)