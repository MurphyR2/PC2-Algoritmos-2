# -*- coding: utf-8 -*-
"""
Created on Mon May  1 22:12:12 2023

@author: jesus
"""

import pandas as pd
import matplotlib.pyplot as plt
# Leer el archivo CSV
import numpy as np
def graficar(archivo):
    
    df = pd.read_csv(archivo)
    
    # fecha en datatime
    df["FECHA"] = pd.to_datetime(df["FECHA"])
    
    # nueva columna sin hora
    df["FECHA_DIA"] = df["FECHA"].dt.date
    #print(df["FECHA_DIA"])
    # agrupar los datos por dia y hallar el valor maximo
    df_temp_max = df.groupby("FECHA_DIA")["TEMPERATURA (°C)"].mean()
    #print(df_temp_max)

    fechas = df_temp_max.index.tolist()
    temperaturas = df_temp_max.values.tolist()
    return df_temp_max

#Graficamos
df1=graficar("01-04-2019.csv")
df2=graficar("01-04-2023.csv")
f1=[str(f)[5:] for f in df1.index.to_list()]
f2=[str(f)[5:] for f in df2.index.to_list()]
#print(f1)
num_elementos=len(f1)

plt.plot(f1, df1, label = "2018-2019")

ubicaciones = [i for i in range(0, len(f1), 50)]
etiquetas_mostradas = [f1[i] for i in ubicaciones]
plt.xticks(ubicaciones,etiquetas_mostradas)
plt.plot(f2,df2,label="2022-2023")
plt.legend(loc = "upper left")
#plt.plot(f2, df2)
plt.xlabel("Fecha")
plt.ylabel("Temperatura (°C)")
plt.title("Temperaturas máximas diarias")
plt.show()

