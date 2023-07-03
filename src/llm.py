import os
import openai

from dotenv import load_dotenv


load_dotenv()

class LLM:
    def __init__(self, memory):
        self.memory = memory
        openai.api_key = os.environ.get("OPENAI_API_KEY", "")

    def generate(self):
        messages = self.memory.message_history
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-16k",
            messages=messages,
            max_tokens=4000,
            temperature=0.4,
        )

        return response
