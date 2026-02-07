from cerebras.cloud.sdk import Cerebras
from importlib.resources import files
import os
import dotenv

class CerebrasAgent:
    def __init__(self):
        dotenv.load_dotenv(files("english_ia").joinpath(".env"))
        self.client = Cerebras( api_key=os.getenv("CEREBRAS_API_KEY" ) )

    def generate(self, question, system=""):
        stream = self.client.chat.completions.create(
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
            model="zai-glm-4.7",
            stream=True,
            max_completion_tokens=2048,
            temperature=1,
            top_p=1,
        )

        for chunk in stream:
            yield chunk.choices[0].delta.content or ""

    def test(self):
        return self.generate("Fibbonacci en python")
    
    def __str__(self):
        return "Agent zai-glm-4.7 from Cerebras"


cerebrasAgent = CerebrasAgent()

if __name__ == "__main__":
    
    try:
        for chunk in cerebrasAgent.test():
            print(chunk, end="")
        print("\n")

    except Exception as e:
        print(e)

    #print(cerebrasAgent.client.models.list())