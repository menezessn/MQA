import pandas as pd
from scipy.stats import pointbiserialr
import matplotlib.pyplot as plt
import os

pre = os.path.dirname(os.path.realpath(__file__))
fname = 'adult.xlsx'
path = os.path.join(pre, fname)

adult = pd.read_excel(path)

adult['Sexo'] = adult['Sexo'].map({'Feminino': 0, 'Masculino': 1})

variaveis_quantitativas = ['Idade', 'Anos de Estudo', 'Ganho de Capital', 'Perca de Capital', 'Carga Horária Semanal']

resultado_correlacao = []

for var in variaveis_quantitativas:
    correlacao = pointbiserialr(adult[var], adult['Sexo'])
    resultado_correlacao.append((var, correlacao.correlation, correlacao.pvalue))

variaveis = [resultado[0] for resultado in resultado_correlacao]
correlacoes = [resultado[1] for resultado in resultado_correlacao]

plt.bar(variaveis, correlacoes)
plt.xlabel('Variáveis Quantitativas')
plt.ylabel('Correlação Point-Biserial')
plt.title('Correlação entre Variáveis Quantitativas e Sexo')
plt.xticks(rotation=45)
plt.tight_layout()

for i, corr in enumerate(correlacoes):
    plt.text(i, corr, f'{corr:.2f}', ha='center', va='bottom')

plt.show()
