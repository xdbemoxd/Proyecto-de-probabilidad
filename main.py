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




