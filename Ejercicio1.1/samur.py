import pandas as pd

 

URL = "https://datos.madrid.es/egob/catalogo/300178-12-samur-activaciones.csv"

 

# Leer CSV desde la URL

data = pd.read_csv(URL, sep=';', encoding='UTF-8')

 

#print(data.head())  # Mostrar las primeras filas para visualizar los datos

#print(data.info())  # Mostrar información sobre el DataFrame

#print(data.describe())  # Mostrar estadísticas básicas sobre el DataFrame

#print(data.isnull().sum())  # Mostrar el número de valores nulos en cada columna  

#como mas de la mitad en la columna de Hospital no tienen valor, la elimino

datos = data.drop(['Hospital'], axis=1) 

#print(datos.info())

#para operar mejor paso la hora de solicitud a minutos

#datos['Hora Solicitud'] = pd.to_datetime(datos['Hora Solicitud'])

#datos['Hora Solicitud'] = datos['Hora Solicitud'].dt.hour * 60 + datos['Hora Solicitud'].dt.minute

#print(datos.head()) #no tiene mucho sentido pasar la hora de solicitud a minutos

#print(datos.head())

#quiero ver cuantos distritos diferentes hay

#print(datos['Distrito'].unique())

#print(datos['Código'].unique()) #hay demasiados tiene mas sentido distrito

datos.to_csv('Ejercicio1.1/datoslimpios.csv', sep=';', encoding='UTF-8')

#quiero un grafico de barras con el mes y el distrito

#hazme un grafico de barras con plt
#para ello pasame la columna de Mes a valores numericos, enero = 1, febrero = 2, etc
import csv
meses_a_numeros = {
    'ENERO': 1,
    'FEBRERO': 2,
    'MARZO': 3,
    'ABRIL': 4,
    'MAYO': 5,
    'JUNIO': 6,
    'JULIO': 7,
    'AGOSTO': 8,
    'SEPTIEMBRE': 9,
    'OCTUBRE': 10,
    'NOVIEMBRE': 11,
    'DICIEMBRE': 12
}

datos['Mes'] = datos['Mes'].map(meses_a_numeros)

#print(datos.head())

#datos.to_csv('Ejercicio1.1/datoslimpiosnumericos.csv', sep=';', encoding='UTF-8')


#quiero que a la columna de Hora Intervencion le restes la columna de Hora Solicitud y me pases el resultado a minutos

import datetime as dt
import numpy as np
data['Hora Intervención'] = pd.to_datetime(data['Hora Intervención'])
data['Hora Solicitud'] = pd.to_datetime(data['Hora Solicitud'])

data['Tiempo de respuesta'] = data['Hora Intervención'] - data['Hora Solicitud']

data['Tiempo de respuesta'] = np.where(data['Hora Intervención']< data['Hora Solicitud'], data['Tiempo de respuesta'] + pd.Timedelta(days=1), data['Tiempo de respuesta'])
#corrigeme para que tenga en cuenta cuando es media noche


data['Tiempo de respuesta'] = data['Tiempo de respuesta'].dt.total_seconds() / 60  # Convierte a minutos

#print(data.head())
data = data.dropna()
data.to_csv('Ejercicio1.1/datoslimpios_tiempo_respuesta.csv', sep=';', encoding='UTF-8')


#quiero ver datos nulos de columnas

#print(data.isnull().sum())  # Mostrar el número de valores nulos en cada columna

#quitar filas con datos nulos en Hora Intervencion y Hora Solicitud

datos = data.dropna(subset=['Hora Intervención', 'Hora Solicitud', 'Código', 'Distrito'])

#quitar columna hospital

datos = datos.drop(['Hospital'], axis=1)
#print(datos.isnull().sum())  # Mostrar el número de valores nulos en cada columna