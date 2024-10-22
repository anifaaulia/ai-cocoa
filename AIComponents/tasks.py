import os
from AIComponents.agents import Agents
from AIComponents.tools import *
from dotenv import load_dotenv
from crewai import Task

load_dotenv()


# the chat generation model 
openaigpt4 = ChatOpenAI(model='gpt-4o', 
                        temperature=0.2, 
                        api_key=os.getenv('openapi_key'))

class Tasks:
    def __init__(self, Input, Context, lang):
        self.Input = Input
        self.Context = Context
        self.lang = lang

    def SearchDataTask(self):
        CocoaSearchData = Task(
            description = f"""Lakukan riset dan pencarian data mengenai hasil (KONTEKS) berdasarkan pertanyaan "{self.Input}" dari pengguna,  mengenai {self.Context},
                             Gunakan SearchTools untuk membantu pencarian datamu,
                             cross validasi datamu berdasarkan {self.Input} dan {self.Context},
                             rapikan datamu seperti sebuah artikel wikipedia dan cantumkan link referensi yang sesuai di bawahnya
                             Incorporate any relevant context or expert advice to provide a comprehensive understanding of the topic.""", 
            expected_output = """Laporan yang detail dan terperinci berdasarkan (KONTEKS) yang  mengandung:
                                 - Penjelasan yang jelas terkait (KONTEKS) dari pertanyaan pengguna,
                                 - Poin poin lainnya yang dibuat seperti sumber informasi dari artikel Wikipedia
                                 - Referensi yang paling relevan dan bisa digunakan""",
        agent=Agents().DataSearch(),
        tools=[SearchTools])

        return CocoaSearchData
    
    def ContextUserQuer(self):
        ContextedUserQuer = Task(
            description = f"""Analisa InputPengguna ini = {self.Input}.
                             Berikan (KONTEKS) yang jelas dan terarah dari masalah yang berhasi diidentifikasi""", 
            expected_output=f"""Sebuah Laporan terstruktur yang berisi:
                                  - Input pengguna original yaitu {self.Input}
                                  - Penjelasan mengenai apa yang sebenarnya diinginkan oleh pengguna
                                  - Penjelasan mengenai apa output yang diharapkan penggna
                                  - Daftar Referensi yang relevan dan bisa digunakan
                                  """, 
            agent=Agents().Contextualize(),
            )
        return ContextedUserQuer
    
    def AugmentContext(self):
        AugmentedContext = Task(
            description = f"""Analisa (KONTEKS) yang diberikan, Bandingkan dengan {self.Input}, Gunakan informasi, dan referensi yang diberikan untuk 
                             Lebih memahami (KONTEKS), buatlah prompt yang terbaik untuk menggenerate response terbaik untuk menjawab pertanyaan {self.Input} dalam lingkup {self.Context}
                             """,
            expected_output=f"""Sebuah Laporan yang berisi
                                - Input pengguna original yaitu {self.Input}
                                - Penjelasan mengenai apa yang sebenarnya diinginkan oleh pengguna
                                - Prompt untuk menjawab konteks(Prompt harus berisi Informasi yang telah dicari sebelumya)
                                - Daftar Referensi yang relevan dan bisa digunakan""", 
            agent=Agents().Augment()
            )
        return AugmentedContext

    def AnalyseAugContext(self):
        AnalysedAugContext = Task(
            description = f"""Jawab Input pengguna {self.Input} dengan memperhatikan (KONTEKS) yang diberikan berdasarkan sumber informasi yang ada pada Prompt yang diberikan merupakan petunjuk lanjutan langkah 
                             dalam memberikan Output yang dinginkan pengguna, gunakan SearchTools untuk mencari informasi tambahan dari referensi yang diberikan jika diperlukan
                             """, 
            expected_output=f"""sebuah lembar Saran MUST IN {self.lang} yang include:
                                  - Penjelasan mendalam untuk poin kunci dari (KONTEKS)
                                  - Informasi tambahan mengenai (KONTEKS) yang disesuaikan dengan prompt dan KONTEKS={self.Context}
                                  - Jika diminta Informasi maka berikan informasi yang sejelas jelasnya SESUAIKAN DENGAN KONTEKS={self.Context}!!
                                  - Atau jika diminta langkah langkah berikan langkah langkah yang detail dengan Informasi terkait SESUAIKAN DENGAN KONTEKS={self.Context}!!
                                  - Berikan daftar referensi yang digunakan 
                                  YOU MUST USE {self.lang}""", 
            agent=Agents().Adviser(),
            tools=[SearchTools])
        return AnalysedAugContext