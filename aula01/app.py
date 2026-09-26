"""Dashboard de Livros: app Streamlit.
"""

import streamlit as st
import dados

st.set_page_config(layout="wide")
st.title("📚 Dashboard de Livros")
st.write("Se você está vendo esta página, o seu ambiente está pronto! 🎉")

col1, col2, col3, col4 = st.columns(4)

livros = dados.ler_livros()

qtd_livros = len(livros)

col1.metric("Total de livros:" , qtd_livros)

preco_medio = dados.calculo_preco_medio(livros)

col2.metric("Preço médio:" , f"£{preco_medio:.2f}")

cinco_estrelas = dados.contar_cinco_estrelas(livros)
col3.metric("Qtd de livros com 5 estrelas : " , cinco_estrelas)

preco_caro = dados.preco_mais_caro(livros)
livro_caro = dados.livro_mais_caro(livros)
col4.metric("Preço mais caro:" , f"£{preco_caro:.2f}")
col4.caption(f" {livro_caro['titulo']}")

st.dataframe(livros)

