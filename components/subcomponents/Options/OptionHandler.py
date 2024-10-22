from components.subcomponents.Options.OptionPage import *
import streamlit as st


def Option(option, lang) :
    if option == None :
        OptionPage("","","","","").StartPage()
    elif option == "Informasi Umum Kakao":
        OptionPage("Masukkan Pertanyaan disini!",
                   """##### Informasi Umum Kakao 
menyediakan Informasi yang umum mengenai berbagai hal tentang kakao    """,
                    "Pusat Informasi Umum Kakao",
                    lang,
                    KokoaCrew.BaseCrew).BaseIO()
    elif option == "Cluster Tanaman Kakao":
        OptionPage("Cari Informasi Seputar Tanaman Kakao disini!",
                   """##### Cluster Tanaman Kakao
Memberikan informasi terkait:
- Pembibitan
- Sambung Pucuk
- Sambung Samping
- Pemupukan
- Pemeliharaan
- Panen""",
                    "Pusat Informasi Tanaman Kakao (Pembibitan, Sambung pucuk,Sambung samping, Pemupukan, Pemeliharaan, Panen)",
                    lang,
                    KokoaCrew.BaseCrew).BaseIO()
    elif option == "Cluster Penyakit Kakao":
        OptionPage("Penyakit atau Hama apa yang ingin di cari tahu?",
                   """##### Cluster Penyakit Kakao
Memberikan informasi terkait penyakit dan Hama kakao serta langkah-langkah penanggulangan, pembasmian, maupun pencegahannya.
""", 
                   "Pusat Informasi dan Penanganan Penyakit Kakao",
                   lang, 
                   KokoaCrew.BaseCrew).BaseIO()
    elif option == "Cluster Pasca Panen":
        OptionPage("Proses Pasca Panen apa yang membuat anda tertarik?",
                   """##### Cluster Pasca Panen
Memberikan informasi terkait:
- Proses Lapangan
- Distribusi
- Harga Jual""", 
                   "Pusat Informasi Lengkap dan Panduan Lengkap Pasca Panen Kakao (Proses Lapangan, Harga Jual)", 
                   lang,
                   KokoaCrew.BaseCrew).BaseIO()
    else:
        st.write("Masih dalam pengembangan")
