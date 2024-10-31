import streamlit as st
import pandas as pd
import numpy as np

df = pd.read_csv("educacion.csv")
st.title("analis de datos de educacion en colombia")
uploaded_file = st.file_uploader("Cargar archivo 'educacion.csv'", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)
    st.sidebar.header("Filtros")
nivel_educativo = st.sidebar.multiselect(
    "Nivel educativo", df["Nivel educativo"].unique()
)
carrera = st.sidebar.multiselect("Carrera", df["Carrera"].unique())
institucion = st.sidebar.multiselect("Institución", df["Institución"].unique())

df_filtrado = df.copy()
if nivel_educativo:
    df_filtrado = df_filtrado[df_filtrado["Nivel educativo"].isin(nivel_educativo)]
if carrera:
    df_filtrado = df_filtrado[df_filtrado["Carrera"].isin(carrera)]
if institucion:
    df_filtrado = df_filtrado[df_filtrado["Institución"].isin(institucion)]
    st.dataframe(df_filtrado)
    st.subheader("Estadísticas Descriptivas")
st.write(df_filtrado.describe())

st.subheader("Estadísticas Descriptivas")
st.write(df_filtrado.describe())

# Conteo de estudiantes por nivel educativo
st.subheader("Conteo de Estudiantes por Nivel Educativo")
st.bar_chart(df_filtrado["Nivel educativo"].value_counts())
st.subheader("Distribución de la Edad")
df = pd.read_csv("educacion.csv")
df_filtrado = df[df['Edad'].notna()]

# Crear histogram data
histogram_values = np.histogram(df_filtrado["Edad"], bins=10)[0]
st.bar_chart(histogram_values)

