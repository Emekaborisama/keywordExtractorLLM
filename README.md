# keywordExtractorLLM

keyword_extract_LLM is a Python library designed to simplify the process of keyword extraction from a given text using pretrain LLM(large language model) via Huggingface, specifically tailored for the Hugging Face Transformers ecosystem. With the library, you can effortlessly extract relevant keywords from text, making it an invaluable tool for tasks like content analysis, and information retrieval.

## Features
- Utilizes Hugging Face Transformers pipeline: keyword_extract_LLM leverages the power of Hugging Face's state-of-the-art language models.
- Keyword Extraction: Extracts keywords from a given text using any LLM mode via huggingface pipeline language models.
- Customization: You can customize various parameters for the extraction process to your specific needs.


## Getting Started
### Installation
You can install keyword_extract_LLM using pip:

```python
pip install keyword_extract_LLM
```
```python
import torch
from transformers import pipeline
from keyword_extract_llm import extractor as extract

# Initialize the language model pipeline
kwargs = dict(max_new_tokens=206, do_sample=True, temperature=0.3, top_k=50, top_p=0.95)
pipe = pipeline("text-generation", model="HuggingFaceH4/zephyr-7b-alpha", torch_dtype=torch.bfloat16, device_map="auto")

# Input text
text = "Your input text goes here."

# Initialize the KeywordExtractor
extractor = extract.KeywordExtractor(pipeline=pipe)

# Extract keywords
keyword = extractor.extractor(text=text, max_attempt=2, **kwargs)

# Print the extracted keywords
print(keyword)
```

- text: The input text from which keywords will be extracted.
- max_attempt: The maximum number of attempts for keyword extraction.
- **kwargs: Additional keyword arguments for customizing the extraction process.

Contribution guide:

- git clone the repo
- make changes, run test and ensure your changes pass the test
- ensure the pre commit hook yaml file is in your directory 
- install and initialize pre commit hook using `pip install pre-commit` and `pre-commit install`
- stage your commit  and push to a new branch