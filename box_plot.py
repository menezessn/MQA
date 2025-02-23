import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

pre = os.path.dirname(os.path.realpath(__file__))
fname = 'adult.xlsx'
path = os.path.join(pre, fname)

adult = pd.read_excel(path)

sns.set(style='whitegrid')
fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(18, 6))
variaveis_quantitativas = ['Idade', 'Anos de Estudo', 'Carga Horária Semanal']

for i, variavel in enumerate(variaveis_quantitativas):
    sns.boxplot(
        x='Sexo',
        y=variavel,
        data=adult,
        ax=axes[i],
        palette='Set3',
        medianprops={'color': 'red'},
    )
    axes[i].set_xlabel('Sexo')
    axes[i].set_ylabel(variavel)
    axes[i].set_title(variavel + ' por Sexo')

plt.tight_layout()
plt.show()
