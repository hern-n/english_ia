from groq import Groq
import dotenv
from importlib.resources import files
import os

dotenv.load_dotenv(files("english_ia").joinpath(".env"))

class GroqAgent:
    def __init__(self):
        self.client = Groq()

    def generate(self, question, system):
        completion = self.client.chat.completions.create(
            model="moonshotai/kimi-k2-instruct-0905",
            messages=[
            {
                "role": "system",
                "content": system
            },
            {
                "role": "user",
                "content": question
            }
            ],
            temperature=0.6,
            max_completion_tokens=4096,
            top_p=1,
            stream=True,
            stop=None
        )

        for chunk in completion:
            yield chunk.choices[0].delta.content or ""

    def test(self):
        return self.generate("Fibbonai en python")
    
    def __str__(self):
        return "Agent moonshotai/kimi-k2-instruct-0905 from Groq"


groqAgent = GroqAgent()

if __name__ == "__main__":
    
    for chunk in groqAgent.test():
        print(chunk, end="")
    print("\n")