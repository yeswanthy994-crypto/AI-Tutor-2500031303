# BPE tokenization using pre-trained GPT-2 tokenizer

from transformers import AutoTokenizer
from collections import Counter

tokenizer = AutoTokenizer.from_pretrained("gpt2")

text = input("Enter a sentence : ") or "I love learning Python"

tokens = tokenizer.tokenize(text)
token_ids = tokenizer.convert_tokens_to_ids(tokens)
print("Original sentence :", text)
print("BPETokens :", tokens)
print("Token IDs :", token_ids)
print("Length of tokens :", len(tokens))
