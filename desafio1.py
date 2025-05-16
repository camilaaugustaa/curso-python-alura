import matplotlib.pyplot as plt #essa biblioteca é para fazer gráficos
import numpy as np #essa biblioteca é para fazer cálculos matemáticos
import pandas as pd #essa biblioteca é para fazer manipulação de dados
import seaborn as sns #essa biblioteca é para fazer gráficos mais bonitos


#estudantes = ["Ana", "Bruno", "Carlos"]
#notas = [8.5, 9, 6.5]
#plt.bar(x = estudantes, height = notas)#x é o eixo x e height é o eixo y. o eixo x esta na horizontal e o eixo y esta na vertical
#plt.show()#essa função mostra o gráfico

from random import choice #essa biblioteca é para fazer escolhas aleatórias
estudantes_2 = ["Helena", "Higor", "Juliana"]
estudantes = choice(estudantes_2)
print(estudantes)