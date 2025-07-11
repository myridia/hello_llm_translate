#!/usr/bin/env python
import os
from transformers import AutoTokenizer, pipeline, MarianMTModel, MarianTokenizer
from datasets import load_dataset

import torch

# Check if CUDA is available
if torch.cuda.is_available():
    device = torch.device("cuda")
    print("CUDA is available! Using GPU.")


model_name = "Helsinki-NLP/opus-mt-en-de"  # Correct model name!
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)

src_text = ["Hello, how are you?"]
encoded = tokenizer(src_text, return_tensors="pt", padding=True)
generated_tokens = model.generate(**encoded)
translated = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)

print(translated)
