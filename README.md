


<h1 align="center">
<p>KEYWORD EXTRACTOR LLM :goat:</p>

<p align="center">

<!-- [![Downloads](https://pepy.tech/badge/keywordextractorllm)](https://pepy.tech/project/keywordextractorllm) -->
<img alt="python" src="https://img.shields.io/badge/python-%3E%3D3.6-blue?logo=python">
<img alt="torch" src="https://img.shields.io/badge/torch-%3E%3D2.3.0-orange?logo=torch">
<a href="https://pypi.org/project/keywordextractorllm/">
  <img alt="PyPI" src="https://img.shields.io/pypi/v/text-gen?color=%234285F4&label=release&logo=pypi&logoColor=%234285F4">
</a>
</p>
</h1>
<h2 align="center">
<p>KEYWORD EXTRACTOR LLM</p>
</h2>

<p align="center">
LLM keyword extractor is a Python library designed to simplify the process of keyword extraction from a given text using pretrain LLM(large language model) via Huggingface, specifically tailored for the Hugging Face Transformers ecosystem. With the library, you can effortlessly extract relevant keywords from text, making it an invaluable tool for tasks like content analysis, and information retrieval.
</p>



## Features
- Utilizes Hugging Face Transformers pipeline: keyword_extract_LLM leverages the power of Hugging Face's state-of-the-art language models.
- Keyword Extraction: Extracts keywords from a given text using any LLM mode via huggingface pipeline language models.
- Customization: You can customize various parameters for the extraction process to your specific needs.


### Installation
You can install keyword extractor LLM using pip:

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