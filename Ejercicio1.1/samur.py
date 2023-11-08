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

#print(mediana)


'''
moda = datos['Código'].value_counts().idxmax()  # Obtén el código más frecuente
print(moda)
import matplotlib.pyplot as plt

# Obtén las 10 categorías más comunes
top_10 = datos['Código'].value_counts().nlargest(10)

# Crea un gráfico de barras para las 10 categorías más comunes
top_10.plot(kind='bar', figsize=(10, 5))
plt.xlabel('Código')
plt.ylabel('Frecuencia')
plt.show()
'''
'''
import pandas as pd
import matplotlib.pyplot as plt

# Ejemplo de datos
data = {'Mes': ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo'],
        'Código': ['A', 'B', 'A', 'B', 'C'],
        'Frecuencia': [10, 15, 12, 8, 20]}

df = pd.DataFrame(data)

# Filtrar las 10 categorías más comunes
top_10 = df['Código'].value_counts().nlargest(10).index

# Filtrar el DataFrame original para incluir solo las 10 categorías más comunes
df_filtered = df[df['Código'].isin(top_10)]

# Pivotar los datos para que el índice sea el Mes, las columnas sean las categorías y los valores sean las frecuencias
pivot_table = df_filtered.pivot_table(index='Mes', columns='Código', values='Frecuencia', aggfunc='sum', fill_value=0)

# Crear un gráfico de barras apiladas
ax = pivot_table.plot(kind='bar', stacked=True, figsize=(10, 5))
plt.xlabel('Mes')
plt.ylabel('Frecuencia')
plt.title('Frecuencia de las 10 categorías más comunes por mes')
plt.legend(title='Código', loc='center left', bbox_to_anchor=(1.0, 0.5))
plt.show()
'''

'''
import matplotlib.pyplot as plt
moda = datos.groupby('Código')['Mes'].apply(lambda x: x.mode().iloc[0] if not x.mode().empty else None)
print(moda)

moda.plot(kind='bar', figsize=(10,5))
plt.show()
'''
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

media = data.groupby('Distrito')['Tiempo de respuesta'].mean()
print(media)

#quiero un histograma con la columna de Tiempo de respuesta

import matplotlib.pyplot as plt

#hazme un grafico de barras de esa media con plt

media.plot(kind='bar', figsize=(10,5))
plt.show()

'''

#quiero ver datos nulos de columnas

#print(data.isnull().sum())  # Mostrar el número de valores nulos en cada columna

#quitar filas con datos nulos en Hora Intervencion y Hora Solicitud

datos = data.dropna(subset=['Hora Intervención', 'Hora Solicitud', 'Código', 'Distrito'])

#quitar columna hospital

datos = datos.drop(['Hospital'], axis=1)
#print(datos.isnull().sum())  # Mostrar el número de valores nulos en cada columna

'''
'''
import pandas as pd

# Lee tu archivo CSV
df = pd.read_csv('Ejercicio1.1/datoslimpios.csv', sep=';', encoding='UTF-8')

import pandas as pd

# Lee tu archivo CSV
from datetime import datetime# Función para calcular la diferencia entre las horas
def calcular_diferencia(hora_solicitud, hora_intervencion):
    formato = '%H:%M:%S'
    solicitud = datetime.strptime(hora_solicitud, formato)
    intervencion = datetime.strptime(hora_intervencion, formato)

    # Asegura que la hora de intervención sea posterior o igual a la hora de solicitud
    if intervencion < solicitud:
        intervencion += pd.DateOffset(days=1)

    # Calcula la diferencia en minutos
    diferencia = (intervencion - solicitud).total_seconds() / 60
    return diferencia

# Aplica la función para calcular la diferencia en minutos
df['Tiempo de Respuesta'] = df.apply(lambda row: calcular_diferencia(row['Hora Solicitud'], row['Hora Intervención']), axis=1)

# Guarda el DataFrame actualizado en un nuevo archivo CSV
df.to_csv('datoslimpios_tiemporespt.csv', index=False)

#quitame todas las filas en las que el Distrito sea LEGANES






media = df.groupby('Distrito')['Tiempo de Respuesta'].mean()

#424

print(media)

#quiero un histograma con la columna de Tiempo de respuesta

import matplotlib.pyplot as plt

#hazme un grafico de barras de esa media con plt

media.plot(kind='bar', figsize=(40,5))
plt.show()

'''
