import requests
import streamlit as st

def buscar_letras(banda, musica):
    endpoint = f"https://api.lyrics.ovh/v1/{banda}/{musica}"
    response = requests.get(endpoint)
    if response.status_code == 200:
        try:
            letra = response.json()["lyrics"]
        except KeyError:
            letra = "Letra não encontrada na resposta da API."
    else:
        letra = "Erro ao buscar a letra da música."
    return letra

st.image("https://i.imgur.com/SmktDIH.png")
st.title("Letras de músicas")

banda = st.text_input("Digite o nome da banda: ", key="banda")
musica = st.text_input("Digite o nome da música: ", key="musica")
pesquisar = st.button("pesquisar")

if pesquisar:
    letra = buscar_letras(banda, musica)
    if letra:
        st.success("Encontramos a letra da sua música!")
        st.text(letra)
    else:
        st.error("Infelizmente não foi possível encontrar a letra dessa música.")