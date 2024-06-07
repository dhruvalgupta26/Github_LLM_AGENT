import os
from langchain_openai import OpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()


llm = OpenAI(openai_api_key=os.getenv('OPENAI_SECRET'))

template = """I really want to travel to {location}. What should I do there? Respond in one short sentence"""

prompt = PromptTemplate(
    input_variables = ["location"],
    template = template,
)

final_prompt = prompt.format(location="Rome")
print(f"Final Prompt: {final_prompt}")
print('.............................')
print(f"LLM output: {llm(final_prompt)}")