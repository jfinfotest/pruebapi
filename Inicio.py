import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar los datos del CSV
df = pd.read_csv("./static/datos_tecnologia_co.csv")

# Título de la aplicación
st.title("Análisis de Penetración de Internet en Colombia")

# Menú lateral para seleccionar las variables
st.sidebar.header("Opciones de visualización")
region = st.sidebar.selectbox("Región", df["Región"].unique())
variable_x = st.sidebar.selectbox("Variable X", df.columns[3:])
variable_y = st.sidebar.selectbox("Variable Y", df.columns[3:])

# Selector de tipo de gráfico
chart_type = st.sidebar.selectbox(
   "Tipo de gráfico",
   ("Dispersión", "Histograma", "Boxplot", "Heatmap"),
)

# Filtrar los datos según la región seleccionada
filtered_df = df[df["Región"] == region]

# Crear el gráfico según el tipo seleccionado
if chart_type == "Dispersión":
   fig, ax = plt.subplots(figsize=(10, 6))
   sns.scatterplot(
      x=variable_x, y=variable_y, data=filtered_df, hue="Departamento", ax=ax
   )
   ax.set_xlabel(variable_x)
   ax.set_ylabel(variable_y)
   ax.set_title(f"Relación entre {variable_x} y {variable_y} en {region}")
elif chart_type == "Histograma":
   fig, ax = plt.subplots(figsize=(10, 6))
   sns.histplot(x=variable_x, data=filtered_df, hue="Departamento", ax=ax)
   ax.set_xlabel(variable_x)
   ax.set_title(f"Histograma de {variable_x} en {region}")
elif chart_type == "Boxplot":
   fig, ax = plt.subplots(figsize=(10, 6))
   sns.boxplot(x="Departamento", y=variable_y, data=filtered_df, ax=ax)
   ax.set_ylabel(variable_y)
   ax.set_title(f"Boxplot de {variable_y} por Departamento en {region}")
elif chart_type == "Heatmap":
   fig, ax = plt.subplots(figsize=(10, 6))
   # Seleccionar solo las columnas numéricas
   numeric_cols = filtered_df.select_dtypes(include=['number'])
   corr_matrix = numeric_cols.corr()
   sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", ax=ax)
   ax.set_title(f"Correlación de variables en {region}")

st.pyplot(fig)

# Información de cómo interpretar cada gráfico
st.subheader("Interpretación de los gráficos")

if chart_type == "Dispersión":
   st.write(
      f"El gráfico de dispersión muestra la relación entre {variable_x} y "
      f"{variable_y} para cada departamento en la región {region}. Puedes "
      f"observar la tendencia general de la relación, si hay una "
      f"correlación positiva o negativa, y si hay algún punto atípico."
   )
elif chart_type == "Histograma":
   st.write(
      f"El histograma muestra la distribución de {variable_x} para los "
      f"departamentos en la región {region}. Puedes observar la frecuencia "
      f"de cada valor de {variable_x} y la forma general de la "
      f"distribución (si es normal, sesgada, etc.)."
   )
elif chart_type == "Boxplot":
   st.write(
      f"El boxplot muestra la distribución de {variable_y} para cada "
      f"departamento en la región {region}. Puedes observar la mediana, "
      f"los cuartiles, los valores atípicos y la dispersión de los datos "
      f"para cada departamento."
   )
elif chart_type == "Heatmap":
   st.write(
      f"El mapa de calor muestra la correlación entre las variables "
      f"numéricas en la región {region}. Un color más rojo indica una "
      f"correlación positiva más fuerte, mientras que un color más azul "
      f"indica una correlación negativa más fuerte. Una correlación "
      f"cercana a 1 indica una fuerte correlación positiva, una "
      f"correlación cercana a -1 indica una fuerte correlación "
      f"negativa, y una correlación cercana a 0 indica que no hay "
      f"correlación."
   )

# Mostrar tabla de datos
st.subheader("Tabla de datos")
st.dataframe(filtered_df)

# Descripción de las variables
st.subheader("Descripción de las variables")
st.write("""
   * **Región:** Región geográfica de Colombia.
   * **Departamento:** Departamento de Colombia.
   * **Municipio:** Municipio de Colombia.
   * **Población:** Población total del municipio.
   * **Hogares con acceso a internet:** Número de hogares con acceso a internet.
   * **Penetración de internet (%):** Porcentaje de hogares con acceso a internet.
   * **Uso de internet:** Frecuencia de uso de internet.
   * **Dispositivos móviles:** Número de dispositivos móviles por hogar.
   * **Uso de teléfonos inteligentes (%):** Porcentaje de hogares que usan teléfonos inteligentes.
   * **Acceso a computadores (%):** Porcentaje de hogares con acceso a computadores.
   * **Uso de redes sociales (%):** Porcentaje de hogares que usan redes sociales.
   * **Compras online (%):** Porcentaje de hogares que realizan compras online.
   * **Nivel educativo:** Nivel educativo promedio de la población.
   * **Edad promedio:** Edad promedio de la población.
   * **Ingresos promedio:** Ingresos promedio de la población.
""")

# Añadir información adicional
st.subheader("Información adicional")
st.write("""
   * Los datos se basan en una encuesta realizada en 2023.
   * La penetración de internet se refiere al porcentaje de hogares con acceso a internet.
   * El uso de internet se refiere a la frecuencia de uso de internet por parte de los hogares.
""")