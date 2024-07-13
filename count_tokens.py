from vertexai.preview import tokenization

def count_tokens(contents: str) -> int:
  model_name = "gemini-1.5-flash-001"
  tokenizer = tokenization.get_tokenizer_for_model(model_name)
  result = tokenizer.count_tokens(contents)
  return result.total_tokens
