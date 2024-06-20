import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('gasolina.csv')

plt.figure(figsize=(10, 6))
sns.lineplot(x='dia', y='venda', data=df)
plt.xlabel('Dia')
plt.ylabel('Preço da Gasolina')
plt.title('Preço da Gasolina ao Longo do Tempo')

plt.savefig('gasolina.png')
plt.show()
plt.close()