"""
    Aluno: Enzo Henrique Silva de Albquerque
    Matrícula: 21602649
    Disciplina: Organização de Computadores

"""


import matplotlib.pyplot as plt
import re
import statistics
import numpy as np
from pylab import *



variavel = 1
media = 0.0

x = [] # contém os intervalos
y = [] # contém as médias
z = [] #contém a variancia de cada ponto

porcentagem = []

while variavel < 1000:
    file = open('./Execucoes/execucao:'+ str(variavel), 'r')

    for line in file:
        line = line.strip()
        if '#' in line:
            texto = re.sub("\s", "", line) #retira os espaços da linha
            texto = re.sub(",", ".", texto) #substitui as virgulas por ponto
            result = re.search(r'#(.*?)%', texto) #estra os caracteres entre "#" e "%"
            porcentagem.append(float(result.group(1))) #seleciona apenas o valor convertendo de string para float
            media = sum(porcentagem)/len(porcentagem) #tira a media
            variancia = statistics.pvariance(porcentagem, media)  # calcula o desvio padrão populacional


    x.append(variavel)
    y.append(round(media, 3))
    z.append(round(variancia, 3))
    variavel = variavel + 10

file.close()

plt.style.use("ggplot")
plt.title('Gráfico das médias por intervalos')
plt.xlabel('Intervalos')
plt.ylabel('Médias')
#xticks(x, rotation=90, size='small')
#yticks(y)
plt.plot(x,y)
grid(True)
yerr = np.sqrt(z)
plt.errorbar(x,y, yerr=yerr, ecolor= "#4B0082",  fmt="o")
plt.show()
