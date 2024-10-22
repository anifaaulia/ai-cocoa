from components.subcomponents.Options.OptionPage import *
from components.subcomponents.Options.OptionHandler import *

def Main():
    option = st.selectbox(
        " Apa yang bisa kami bantu ? ",
        (
            "Informasi Umum Kakao",
            "Cluster Tanaman Kakao",
            "Cluster Penyakit Kakao",
            "Cluster Pasca Panen"
        ),index=None,
        placeholder="Pilih Cluster"
    )
    bahasa = st.selectbox(
        "Bahasa",
        (
            "Bahasa Indonesia",
            "Bahasa Inggris",
            "Bahasa Jawa",
            "Bahasa Sunda",
        ),index=None
    )
    Option(option,bahasa)
