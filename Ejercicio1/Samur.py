import pandas as pd


# Leer CSV activaciones_samur_2023.csv

data = pd.read_csv( "Ejercicio1/activaciones_samur_2023.csv", sep=";" )

 

print(data.head())  # Mostrar las primeras filas para visualizar los datos


