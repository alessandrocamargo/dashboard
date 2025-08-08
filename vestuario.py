import streamlit as st
import pandas as pd
import plotly.express as px

# Título do app
st.markdown("""
<div style='text-align: center'>
    <h1>Lunelli - Computadores</h1>
    <h2>Unidade: VESTUÁRIO</h2>
</div>
""", unsafe_allow_html=True)


# Carregar dados
df = pd.read_excel("computadoresLunelliv4.xlsx", sheet_name="VESTUARIO")

# Limpar dados de sistema operacional
df["Operating system"] = df["Operating system"].astype(str).str.replace("<|>", "", regex=True).str.strip()

# Filtro por sistema operacional
sistemas = sorted(df["Operating system"].dropna().unique())
sistema_escolhido = st.selectbox("🖥️ Selecione o Sistema Operacional", sistemas)

# Filtrar o DataFrame
df_filtrado = df[df["Operating system"] == sistema_escolhido]

# Mostrar total
st.markdown(f"**Total de máquinas com {sistema_escolhido}:** {len(df_filtrado)}")

# Gráfico de CPUs
st.subheader("📊 Processadores mais comuns")
cpu_count = df_filtrado["CPU"].value_counts().reset_index()
cpu_count.columns = ["CPU", "Quantidade"]

fig = px.bar(cpu_count, x="Quantidade", y="CPU", orientation="h", title="Distribuição de CPUs")
st.plotly_chart(fig, use_container_width=True)

# Lista de máquinas
st.subheader("📋 Máquinas Detalhadas")
st.dataframe(df_filtrado[["Name", "CPU", "Operating system"]].reset_index(drop=True))

# Voltar para o portal
st.markdown(
    """
    <a href="https://alessandrocamargo.github.io/portal/" target="_self">
        <button style="background-color: #003366; color: white; padding: 10px 20px; 
        border: none; border-radius: 5px; cursor: pointer;">
            ⬅ Voltar para o Portal
        </button>
    </a>
    """,
    unsafe_allow_html=True
)


