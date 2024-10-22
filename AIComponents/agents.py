import os
from crewai import Agent
from langchain_openai import ChatOpenAI

from dotenv import load_dotenv
import os

import openai
from openai import OpenAI
from AIComponents.tools import *

def configure():
    load_dotenv()
configure()
class Agents:
    configure()
    def __init__(self,):
        self.openaigpt4 = ChatOpenAI(model='gpt-4o', 
                                     temperature=0.2, 
                                     api_key=os.getenv('openapi_key'))
    def DataSearch(self):
        Data = Agent(role='Data Searcher', 
                               goal="""Menyediakan data terhadap konteks yang diberikan dengan mencarinya secara online""", 
                               backstory="""Kamu adalah seorang yang ahli dalam mengumpulkan data dari berbagai sumber terhadap topik yang diberikan, caramu bekerja adalah - melihat topik, menentukan kata kunci pencarian - memulai pencarian""", 
                               allow_delegation=False, 
                               verbose=True, 
                               llm=self.openaigpt4,
                               max_iter=2
                               )
        return Data
    def Contextualize(self):
        Context = Agent(role='Customer Service', 
                               goal="""Berikan penjelasan singkat padat (KONTEKS) dari input customer yang diberikan""", 
                               backstory="""Kamu merupakan seorang consument service yang berpengalaman selama +- 8 tahun dan telah bekerja di berbagai perusahan terkemuka sebagai seorang yang menerjemahkan keinginan konsumen kepada anggota lainnya""", 
                               allow_delegation=False, 
                               verbose=True,
                               llm=self.openaigpt4,
                               max_iter=2
                               )
        return Context
    
    def Augment(self):
        Prompt = Agent(role='specialized promp template model',
                               goal="""Memberikan prompt template yang berisi list yang memandu chatbot memberikan hasil terbaik terhadap input pengguna dan data yang diberikan""", 
                               backstory="""Kamu adalah sebuah model yang digunakan untuk melakukan Augmented yang dilatih berdasarkan Prompt dengan keluaran terbaik kamu merupakan model teradvance yang ada dan saat ini digunakan sebagai prompt generator""",  
                               allow_delegation=False, 
                               verbose=True, 
                               llm=self.openaigpt4,
                               max_iter=5
                               )
        return Prompt
    def Adviser(self):
        sugestion = Agent(role='Expertise Adviser',
                               goal="""Memberikan jawaban terbaik dari data, konteks, dan prompt yang disediakan""", 
                               backstory="""Kamu merupakan seorang yang expert di bidangnya sehingga sering dimintai berbagai saran di bidang terkait kamu menmiliki 10 Tahun pengalaman di bidang itu dan saat ini kamu bekerja sebagai seorang konsultant kamu sangat suka memberikan jawaban yang terpadu mengenai segala hal secara terperinci dan detail step by stepnya dan membagikan sumber dimana kamu belajar hal itu""", 
                               allow_delegation=False, 
                               verbose=True, 
                               llm=self.openaigpt4,
                               max_iter=5
                               )
        return sugestion