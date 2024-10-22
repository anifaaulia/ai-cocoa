from AIComponents.agents import *
from AIComponents.tasks import *
from crewai import Crew, Process
class KokoaCrew:
    def __init__(self,Input, Context, lang) :
        self.Input = Input
        self.Context = Context
        self.lang = lang
        
    def BaseCrew(self):
        input = Tasks(self.Input,self.Context,self.lang)
        crew = Crew(
            agents=[Agents().Contextualize(), Agents().DataSearch(),  Agents().Augment(), Agents().Adviser()], 
            tasks=[input.ContextUserQuer(), input.SearchDataTask(), input.AugmentContext(), input.AnalyseAugContext()], 
            process=Process.sequential, 
            manager_llm=openaigpt4
        )
        return crew.kickoff()