import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import poisson, expon

"""
--------------------------- FASE 1 ----------------------
"""

df = pd.read_csv("new_data.csv")

df['Timestamp'] = pd.to_datetime(df['Timestamp'],dayfirst=True)

df['second'] = df['Timestamp'].dt.second

df_aux = df.groupby('second')['Timestamp'].count()

# 1. Convertir la serie a un DataFrame
df_alineado = df_aux.reset_index()

# Opcionalmente, renombra las columnas para mayor claridad
df_alineado.columns = ['Segundo', 'Conteo_Timestamp']

"""
--------------------------- FASE 2 ----------------------
"""

"""
--------------------- Análisis de Variable Discreta -------------------------
"""

#promedio por segundos
print(df_alineado)

#generando la distribucion de poisson
mu = df_alineado['Conteo_Timestamp'].mean()

print(mu)

random_vars = poisson.rvs(mu=mu, size=len(df_alineado))

plt.bar(df_alineado['Segundo'], df_alineado['Conteo_Timestamp'], color='skyblue')
plt.bar(df_alineado['Segundo'],random_vars, color='salmon')
plt.show()


"""
----------------------------------------- Análisis de Variable Continua -------------------------- 
"""

random_vars_2 = expon.rvs( scale = mu, size= len( df_alineado ) )

plt.bar(df_alineado['Segundo'], df_alineado['Conteo_Timestamp'], color='skyblue')
plt.bar(df_alineado['Segundo'],random_vars_2, color='salmon')
plt.show()


"""
--------------------------------------------- Análisis de Variables Conjuntas -----------------------------------
"""

def categorize_size(x, small, big):
    categorize = ''
    if x >= big:
        categorize = 'Big'
    elif small < x < big:
        categorize = 'Mean'
    else:
        categorize = 'Small'

    return categorize

mean = df['Packet_Size'].mean()

o = df['Packet_Size'].std()

df['SizeCategory'] = df['Packet_Size'].apply(lambda x: categorize_size(x, mean - o, mean + o))

contingencia =  pd.crosstab(df['Protocol'], df['SizeCategory'])

print(contingencia)

prob_TCP= contingencia.loc[6].sum()/contingencia.values.sum()
print(prob_TCP)

prob_big= contingencia['Big'].sum()/contingencia.values.sum()
print(prob_big)

prob_big_dado_6 = contingencia.loc[6, 'Big'] / contingencia.loc[6].sum()
print(prob_big_dado_6)

"""
no es que los paquetes tcp y grande sean independientes,
es que casualmente en ese intervalo de tiempo no llego ningun paquete tcp grande
"""

tabla_prob = contingencia / contingencia.values.sum()

print(tabla_prob)






