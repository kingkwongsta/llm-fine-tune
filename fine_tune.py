import replicate
import * as dotenv from "dotenv"
dotenv.config()

training = replicate.trainings.create(
  version="meta/llama-2-7b:73001d654114dad81ec65da3b834e2f691af1e1526453189b7bf36fb3f32d0f9",
  input={
    "train_data": "https://raw.githubusercontent.com/kingkwongsta/file-storage/main/output_cocktail.jsonl",
    "num_train_epochs": 3
  },
  destination="kingkwongsta/first-training"
)

print(training)


