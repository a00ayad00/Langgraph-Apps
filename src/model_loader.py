from src.utils import read_yaml
# import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI

load_dotenv()

config = read_yaml("config.yaml")

class ModelLoader:
    def __init__(self):
        self.config = config
        self.provider = self.config.llm.provider
        self.model_name = self.config.llm.model_name
    
    def load_llm(self):
        """
        Load and return the LLM model.
        """
        print(f"Loading model from provider: {self.provider}")
        if self.provider == "groq":
            print("Loading LLM from Groq..............")
            # groq_api_key = os.getenv("GROQ_API_KEY")
            # llm=ChatGroq(model=model_name, api_key=groq_api_key)
            llm = ChatGroq(model = self.model_name)
        elif self.provider == "openai":
            print("Loading LLM from OpenAI..............")
            # openai_api_key = os.getenv("OPENAI_API_KEY")
            # llm = ChatOpenAI(model_name = self.model_name, api_key=openai_api_key)
            llm = ChatOpenAI(model_name = self.model_name)
        
        return llm