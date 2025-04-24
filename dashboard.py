import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Meu Dashboard", layout="wide")

# Título
st.title("📊 Meu Primeiro Dashboard com Streamlit")

# Subtítulo
st.markdown("Exemplo simples com Streamlit + gráfico + tabela")

# Dados de exemplo
df = pd.DataFrame({
    "Categoria": ["A", "B", "C"],
    "Valores": [100, 150, 200]
})

# Mostrar tabela
st.subheader("Tabela de Dados")
st.dataframe(df)

# Mostrar gráfico
st.subheader("Gráfico de Barras")
fig, ax = plt.subplots()
ax.bar(df["Categoria"], df["Valores"], color="skyblue")
ax.set_title("Valores por Categoria")
st.pyplot(fig)
