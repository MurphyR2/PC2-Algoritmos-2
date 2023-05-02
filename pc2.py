# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import matplotlib.pyplot as plt
# Leer el archivo CSV
import numpy as np
def graficar(archivo):
    
    df = pd.read_csv(archivo)
    
    # columna fecha en datatime
    df["FECHA"] = pd.to_datetime(df["FECHA"])
    
    # Crear una nueva con la fecha sin hora
    df["FECHA_DIA"] = df["FECHA"].dt.date
    print(df["FECHA_DIA"])
    # obtenemos la temp maxima
    df_temp_max = df.groupby("FECHA_DIA")["TEMPERATURA (°C)"].max()
    print(df_temp_max)
    
    fechas = df_temp_max.index.tolist()
    temperaturas = df_temp_max.values.tolist()
    return df_temp_max

#Graficamos
df1=graficar("01-04-2019.csv")
df2=graficar("01-04-2023.csv")

#df2_interpolado = np.interp(df1.index, df2.index, df2.values)



plt.plot(df2.index, df2.values,"orange")
plt.xlabel("Fecha")
plt.ylabel("Temperatura (°C)")
plt.title("Temperaturas máximas diarias")
plt.show()


##-----------------------------

