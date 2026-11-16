import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Covid 19 - 2020", layout="wide")

df = pd.read_csv("esus-vepi.LeitoOcupacao_2020.csv", sep=";")
df["mes"] = df["dataNotificacao"].astype(str).str[5:7]

df_filtrado = df[
    (df["dataNotificacao"].isin(["dataNotificacao"])) &
    (df["estado"].isin(["unidade da federação"])) &
    (df["ocupacaoConfirmadoUti"] == "UTI")
].copy()

df_tabela = df_filtrado[["dataNotificacao", "estado", "ocupacaoConfirmadoUti"]]

st.title("Ocupação hospitalar de Covid-19 em 2020")

st.sidebar.header("Controles")
opcao = st.sidebar.radio("Selecione a visualização:", ["Tabela", "Gráficos"])

if opcao == "Tabela":
    st.header("Tabela da ocupação hospitalar")
    st.dataframe(df_tabela, use_container_width=True, hide_index=True)

elif opcao == "Gráficos":
    st.header("Gráficos da ocupação hospitalar")

    st.subheader("1. Gráfico de Linha — covid-19")
    df_data = df_tabela[df_tabela["dataNotificacao"] == "2020-04-14T03:00:00.000Z"]

    fig_data = px.line(
        df_data,
        x="mes",
        y="dataNotificacao",
        markers=True,
        title="data notificação",
        template="plotly_dark"
    )
    fig_data.update_traces(line_color="#FF6B6B", line_width=3, marker_size=8)
    fig_data.update_xaxes(type="category")
    fig_data.update_layout(paper_bgcolor="#111827", plot_bgcolor="#111827")
    st.plotly_chart(fig_data, use_container_width=True)

    st.subheader("2. Gráfico de Linha — estado")
    df_minas = df_tabela[df_tabela["estado"] == "Minas Gerais"]

    fig_minas = px.line(
        df_minas,
        x="minas gerais",
        y="minas gerais",
        markers=True,
        title="Estado",
        template="plotly_dark"
    )
    fig_minas.update_traces(line_color="#00F5D4", line_width=3, marker_size=8)
    fig_minas.update_xaxes(type="category")
    fig_minas.update_layout(paper_bgcolor="#111827", plot_bgcolor="#111827")
    st.plotly_chart(fig_minas, use_container_width=True)

st.markdown("---")
st.caption("Fonte dos dados: dados abertos da planilha — esus-vepi.LeitoOcupacao_2020.csv")