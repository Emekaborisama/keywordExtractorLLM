# import pytest

# from ..extractor import \
#     KeywordExtractor  # Replace 'your_module' with the actual module name


# # Create a fixture for the KeywordExtractor
# @pytest.fixture
# def keyword_extractor():
#     # You may initialize the KeywordExtractor here or provide relevant parameters
#     # for your specific use case.
#     # Example: KeywordExtractor(pipeline=your_pipeline)
#     yield KeywordExtractor(pipeline=None)  # Replace 'None' with your actual pipeline


# # Test KeywordExtractor class methods


# def test_extract_keyword(keyword_extractor):
#     text = "This is a sample text"
#     # Define the kwargs you want to pass to the method
#     kwargs = {
#         "max_new_tokens": 100,
#         "do_sample": True,
#         "temperature": 0.7
#         # Add other kwargs as needed
#     }
#     result = keyword_extractor.extract_keyword(text, **kwargs)
#     # Add your assertions here to validate the result


# def test_extractor(keyword_extractor):
#     text = "Another sample text"
#     max_attempt = 3
#     # Define the kwargs you want to pass to the method
#     kwargs = {
#         "max_new_tokens": 100,
#         "do_sample": True,
#         "temperature": 0.7
#         # Add other kwargs as needed
#     }
#     result = keyword_extractor.extractor(text, max_attempt, **kwargs)
#     # Add your assertions here to validate the result


# def test_extract_dict_inside_markdown_json(keyword_extractor):
#     text = '{"key": "value"}'
#     result = keyword_extractor.extract_dict_inside_markdown_json(text)
#     # Add your assertions here to validate the result
