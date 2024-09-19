import pandas as pd

df = pd.read_csv('ventas-por-factura.csv')
pd.set_option('display.max_columns', None) # Configurar pandas para mostrar todas las columnas

#============================================

df = df.rename(columns={'N° de factura': 'Numero de factura', 'País':'Pais'})
df_canceladas = df[df['Numero de factura'].str.startswith('C')] # Filtrar las facturas canceladas (que comienzan con 'C')
df_realizadas = df[~df['Numero de factura'].str.startswith('C')] # Filtrar las facturas realizadas (que no comienzan con 'C')

# O usar 'Desconocido' si es un campo de texto
df['ID Cliente'] = df['ID Cliente'].fillna(-1)

df['Fecha de factura'] = pd.to_datetime(df['Fecha de factura'])
df['ID Cliente'] = df['ID Cliente'].astype(int)

print(df.isnull().sum()) # Mostrar la cantidad de valores nulos en cada columna
print(df['ID Cliente'].unique())  # Ver los valores únicos en la columna

#============================================

# Establecer la fecha de referencia como el máximo valor en la columna de fechas
fecha_referencia = df['Fecha de factura'].max()

# Crear una columna de recencia, que es la diferencia en días entre la última compra y la fecha de referencia
rfm_df = df.groupby('ID Cliente').agg({'Fecha de factura': lambda x: (fecha_referencia - x.max()).days})

# Renombrar la columna a 'Recencia'
rfm_df.rename(columns={'Fecha de factura': 'Recencia'}, inplace=True)

# Ver las primeras filas para verificar
print(rfm_df.head())




