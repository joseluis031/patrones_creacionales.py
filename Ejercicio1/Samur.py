import pandas as pd

 

URL = "https://datos.madrid.es/egob/catalogo/212504-0-emergencias-activaciones.csv"

 

# Leer CSV desde la URL

data = pd.read_csv(URL, sep=';', encoding='ISO-8859-1')

 

print(data.head())  # Mostrar las primeras filas para visualizar los datos


#print(datos.info())  # Mostrar información sobre el DataFrame

#print(datos.describe())  # Mostrar estadísticas básicas sobre el DataFrame

print(data.isnull().sum())  # Mostrar el número de valores nulos en cada columna
#aqui veo que hay 5 clumnas vacias que tengo que eliminar (precio,diasexcluidos,descripcion,audiencia y unenamed)

# Eliminar columnas que no aportan información

datos = data.drop(['PRECIO', 'DIAS-EXCLUIDOS', 'DESCRIPCION', 'AUDIENCIA', 'Unnamed: 29'], axis=1)

print(datos.info()) #vuelvo a mostrar la informacion para ver que se han eliminado las columnas

datos.to_csv('Ejercicio1/datoslimpios.csv', sep=';', encoding='ISO-8859-1')

