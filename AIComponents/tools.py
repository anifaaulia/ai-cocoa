import os
from langchain_openai import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults

from dotenv import load_dotenv
import os

import openai

from openai import OpenAI

load_dotenv()

# the chat generation model 
openaigpt4 = ChatOpenAI(model='gpt-4o', 
                        temperature=0.2, 
                        api_key=os.getenv('openapi_key'))

os.environ['TAVILY_API_KEY']=os.getenv('tavilyapi_key')

SearchTools = TavilySearchResults(k=3)
