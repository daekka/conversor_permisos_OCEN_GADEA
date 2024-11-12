import pandas as pd

# Leer el archivo Excel PT's
df_PTs_gen_2020 = pd.read_excel('Datos_Origen\PTs con descargo importados de OCEN\PTS genéricos 2020.XLS')
df_PTs_gen_2021 = pd.read_excel('Datos_Origen\PTs con descargo importados de OCEN\PTs genéricos 2021.XLS')
df_PTs_marzo2020_marzo2021 =  pd.read_excel('Datos_Origen\PTs con descargo importados de OCEN\PTs marzo2020-marzo2021.XLS')


# Filtrar columnas 
columnas = ['Tipo Pt', 'Cod  PT', 'Item', 'Elemento', 'Alcance del Trabajo']
df_PTs_gen_2020 = df_PTs_gen_2020[columnas]
df_PTs_gen_2021 = df_PTs_gen_2021[columnas]
df_PTs_marzo2020_marzo2021 = df_PTs_marzo2020_marzo2021[columnas]

# Mostrar las primeras filas del DataFrame
df_PTs = pd.concat ([df_PTs_gen_2020, df_PTs_gen_2021, df_PTs_marzo2020_marzo2021], ignore_index = True)

# Lista de pares (nombre antiguo, nombre nuevo)
columnas_renombradas = [
    ('Tipo Pt', 'Tipo'),
    ('Cod  PT', 'PT'),
    ('Item', 'KKS_OCEN'),
    ('Elemento', 'Elemento'),
    ('Alcance del Trabajo', 'Alcance')
]
# Convertir la lista de pares en un diccionario
diccionario_renombres = dict(columnas_renombradas)
# Renombrar las columnas usando el diccionario
df_PTs = df_PTs.rename(columns=diccionario_renombres)
# Supón que quieres mover la columna 'columna_a_mover' al inicio
columna_a_mover = 'PT'
# Crear una lista de columnas donde la columna deseada está en primer lugar
columnas = [columna_a_mover] + [col for col in df_PTs.columns if col != columna_a_mover]
# Reordenar el DataFrame
df_PTs = df_PTs[columnas]

# Llenar los NaN de una columna específica con un valor (por ejemplo, 0)
df_PTs['KKS_OCEN'] = df_PTs['KKS_OCEN'].fillna("TS")


# Lee tabla conversion OCEN - GADEA
df_KKS = pd.read_excel(r'Datos_Origen\actualizada_mas_reciente_BDI_Unida_KKS_descripcion_corta.xlsx')
# Hacemos un merge para añadir 'Elemento' de DF 2 en DF 1 basado en 'KKS_OCEN' y 'COD_FUNCIONAL'
# Realizamos el merge basado en la coincidencia de 'KKS_OCEN' en df1 y 'COD_FUNCIONAL' en df2
merged_df = pd.merge(df_PTs, df_KKS, left_on='KKS_OCEN', right_on='ITEM_F (KKS)', how='left')
merged_df = merged_df.drop_duplicates(subset='PT', keep='first')

#print(df_PTs.head())

# Leer el archivo Excel PT's
df_plantilla_acciones = pd.read_excel(r'Datos_Origen\PTs con descargo importados de OCEN\acciones aislamiento\TS-00024-2022.xls')


