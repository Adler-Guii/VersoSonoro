# VersoSonoro 
# Buscador de Letras de Música

Este é um aplicativo web simples que permite buscar letras de músicas usando a API [Lyrics.ovh](https://lyricsovh.docs.apiary.io/).

## Como Usar

1.  **Instale as dependências:**

    ```bash
    pip install requests streamlit
    ```

2.  **Execute o aplicativo:**

    ```bash
    streamlit run app.py
    ```

3.  Abra o navegador e acesse o endereço exibido no terminal.

4.  Digite o nome da banda e da música nos campos correspondentes.

5.  Clique no botão "pesquisar" para buscar a letra da música.

## Funcionalidades

* Busca de letras de músicas através da API Lyrics.ovh.
* Interface simples e intuitiva usando Streamlit.
* Tratamento de erros para casos em que a letra da música não é encontrada ou ocorre um erro na API.

## Código

O código principal do aplicativo está no arquivo `app.py`. Ele utiliza as seguintes bibliotecas:

* `requests`: Para fazer requisições à API Lyrics.ovh.
* `streamlit`: Para criar a interface web.

## Exemplo

```python
import requests
import streamlit as st

def buscar_letras(banda, musica):
    endpoint = f"[https://api.lyrics.ovh/v1/](https://api.lyrics.ovh/v1/){banda}/{musica}"
    response = requests.get(endpoint)
    if response.status_code == 200:
        try:
            letra = response.json()["lyrics"]
        except KeyError:
            letra = "Letra não encontrada na resposta da API."
    else:
        letra = "Erro ao buscar a letra da música."
    return letra

st.image("[https://i.imgur.com/SmktDIH.png](https://i.imgur.com/SmktDIH.png)")
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
