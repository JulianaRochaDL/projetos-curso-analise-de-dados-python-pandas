from datetime import datetime
import streamlit as st
import pandas as pd

caminho_datasets = "datasets"

df_compras = pd.read_csv(f"{caminho_datasets}/compras.csv", sep=";", decimal=",", index_col=0)
df_lojas = pd.read_csv(f"{caminho_datasets}/lojas.csv", sep=";", decimal=",")
df_produtos = pd.read_csv(f"{caminho_datasets}/produtos.csv", sep=";", decimal=",")

df_lojas["cidade/estado"] = df_lojas["cidade"] + '/' + df_lojas["estado"]
lista_lojas = df_lojas["cidade/estado"].to_list()
loja_selecionada = st.sidebar.selectbox("Selecione a loja:", lista_lojas)
