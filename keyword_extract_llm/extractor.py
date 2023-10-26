"""
keyword extractor
"""
import json
import re

from pydantic import BaseModel, Field, ValidationError


class KeywordLLM(BaseModel):
    """
    Pydantic model for a list of keywords.
    """

    keywords: list


class Pipeline(BaseModel):
    """
    Hugging face pipeline pydantic model.
    """

    pipeline: object


class KeywordExtractor:
    """
    A class for extracting keywords from text using a Hugging Face pipeline.

    Attributes:
        pipeline (object): The Hugging Face pipeline to use for keyword extraction.
    """

    def __init__(self, pipeline):
        self.pipeline = pipeline

    def extract_keyword(self, text: str, **kwargs) -> str:
        """
        Extracts the keyword from a given text.

        Args:
            text (str): The text to extract the keyword from.
            params (dict): Parameters to control the extraction process.

        Returns:
            str: The extracted keyword.
        """
        try:
            if (
                self.pipeline.check_model_type.__module__
                == "transformers.pipelines.base"
            ):
                print("loading model from huggingface pipeline.................")
        except Exception as e:
            raise AttributeError(
                f"{e} - pipeline has no attibute to check_model_type. must be a huggingface model"
            )
        # We use the tokenizer's chat template to format each message - see
        # https://huggingface.co/docs/transformers/main/en/chat_templating
        messages = [
            {
                "role": "system",
                "content": f"""given a text, extract the keywords and return the keywords.
                However, let your response be in the following format:
                ```json
                {KeywordLLM}
                ```""",
            },
            {"role": "user", "content": f"{text}"},
        ]

        # messages[0]['role']['content'] = text

        prompt = self.pipeline.tokenizer.apply_chat_template(
            messages, tokenize=False, add_generation_prompt=True
        )
        outputs = self.pipeline(prompt, **kwargs)

        keyword = outputs[0]["generated_text"]
        return str(keyword)

    def extractor(self, text: str, max_attempt, **kwargs) -> KeywordLLM:
        """
        Extracts the keyword from a given text with multiple attempts.

        Args:
            text (str): The text to extract the keyword from.
            max_attempt (int): The maximum number of attempts to extract the keyword.
            params (dict): Parameters to control the extraction process.

        Returns:
            KeywordLLM: A KeywordLLM object containing the extracted keyword.

        Raises:
            ValueError: If the keyword cannot be extracted after `max_attempt` attempts.
        """

        count = 0
        keyword = self.extract_keyword(text=text, **kwargs)
        # result = self.extract_dict_inside_markdown_json(keyword)
        try:
            result = self.extract_dict_inside_markdown_json(keyword)
            KeywordLLM.model_validate(result)
            return result
        except Exception as e:
            if max_attempt > count:
                count += 1
                return self.extractor(
                    text=text, max_attempt=max_attempt - count, kwargs=kwargs
                )
            else:
                raise ValueError(
                    f"{e} - result wasn't coherence enough or didn't follow the data schema",
                    keyword,
                    e,
                )

    def extract_dict_inside_markdown_json(self, text: str) -> dict[str, any]:
        """
        Extracts the dictionary inside the markdown json using regex.

        Args:
            text (str): A markdown json string.

        Returns:
            dict: A Python dictionary.
        """

        regex_pattern = r"{[^}]*}"
        dict_string = re.findall(regex_pattern, text)[0]
        dict_result = json.loads(dict_string)
        return dict_result
