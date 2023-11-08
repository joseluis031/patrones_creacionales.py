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

data['Hora Intervención'] = pd.to_datetime(data['Hora Intervención'])
data['Hora Solicitud'] = pd.to_datetime(data['Hora Solicitud'])

data['Tiempo de respuesta'] = data['Hora Intervención'] - data['Hora Solicitud']

data['Tiempo de respuesta'] = data['Tiempo de respuesta'].dt.total_seconds() / 60  # Convierte a minutos

print(data.head())

data.to_csv('Ejercicio1.1/datoslimpios_tiempo_respuesta.csv', sep=';', encoding='UTF-8')







