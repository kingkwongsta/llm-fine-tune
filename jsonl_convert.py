import pandas as pd

df = pd.read_parquet('brianarbuckle_cocktail_recipes.parquet')
df.to_json('output_cocktail.jsonl', orient='records', lines=True)
