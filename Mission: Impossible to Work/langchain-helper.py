import os
import openai

from dotenv import load_dotenv
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def text_generator(media_type:str, job, category):
    if media_type == "Email":
        llm = OpenAI(temperature=0.7)

        prompt_template_subject = PromptTemplate(
            input_variables=['cuisine'],
            template="I want to open a restaurant for {cuisine} food. Suggest a fency name for this."
        )

        subject_chain = LLMChain(llm=llm, prompt=prompt_template_subject, output_key="restaurant_name")