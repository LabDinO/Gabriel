import pandas as pd
import matplotlib.pyplot as plt
import time
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
import numpy as np

local='ostras'

# Carregar os dados do arquivo CSV
df_medido = pd.read_csv(f'maregrafo{local}_medido_processado.csv')
df_modelo = pd.read_csv(f'maregrafo{local}_processado.csv')

nome_arquivo_final = f'validação_maregrafo{local}_janeiro_1'


df_medido['data'] = pd.to_datetime(df_medido['data'])
df_modelo['data'] = pd.to_datetime(df_modelo['data'])

print(df_modelo['data'])

#tirando as médias 


df_modelo['nivel'] =  df_modelo['nivel'] - df_modelo['nivel'].mean()
df_medido['nivel'] =  df_medido['nivel'] - df_medido['nivel'].mean()


#fazendo analises lineares
x, y= df_modelo['nivel'], df_medido['nivel']

#regressão linear
model = LinearRegression()
model.fit([[xi] for xi in x], y)

# Calcule o R-quadrado
r2 = r2_score(y, model.predict([[xi] for xi in x]))
correlation = np.corrcoef(x, y)[0, 1]
rmse = mean_squared_error(y, model.predict([[xi] for xi in x]), squared=False)

#salvando em um txt
with open(f'{nome_arquivo_final}.txt', 'w') as saida:
    saida.write(f'r_square = {round(r2, 4)}\n correlação= {round(correlation,4)}\n rmse= {round(rmse,4)}')

plt.figure(figsize=(12, 8)) #figsize

# Criar o gráfico de linha para o segundo conjunto de dados
plt.plot(df_medido['data'], df_medido['nivel'], label='Medido em situ', linestyle='-', marker='o', color='blue')
plt.plot(df_modelo['data'], df_modelo['nivel'], label='Modelado', linestyle='--', marker='x', color='red')
# Personalizar o gráfico
plt.xlabel('data')
plt.ylabel('Nivel(m)')
plt.title(f'Local: {local}\n Comparação entre Modelado e Medido (r_square = {round(r2, 2)} - correlação= {round(correlation,2)}- rmse= {round(rmse,2)})')
plt.legend()  # Adicionar legenda com os nomes dos conjuntos de dados
plt.grid(True)# Adicionar grade  
plt.savefig(f'../imagens/{nome_arquivo_final}.png')
plt.show()



