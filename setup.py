from setuptools import find_packages, setup

with open("README.md") as readme_file:
    README = readme_file.read()

setup_args = {
    "name": "keyword_extract_LLM",
    "packages": find_packages(),
    "version": "1.0.5",
    "description": "using LLM to extract keywords",
    "long_description_content_type": "text/markdown",
    "long_description": README,
    "author": "Emeka Boris Ama",
    "author_email": "borisphilosophy@gmail.com",
    "license": "MIT",
    "include_package_data": True,
    "url": "https://github.com/Emekaborisama/keywordExtractorLLM",
    # install_requires=[],
    "setup_requires": ["pytest-runner"],
    "tests_require": ["pytest==4.4.1"],
    "test_suite": "tests",
}

install_requires = ["torch", "transformers", "setuptools>=47.1.1"]

if __name__ == "__main__":
    setup(**setup_args, install_requires=install_requires)
