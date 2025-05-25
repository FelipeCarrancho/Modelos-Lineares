import matplotlib.pyplot as plt  # Usando 'plt' em vez de 'fig'
import pandas as leitor
import numpy as np

# Carrega os dados do CSV


# Obtendo as colunas necessárias
dadosusados = leitor.DataFrame(df, columns=['time_study'])
dadosusados1 = leitor.DataFrame(df, columns=['Marks'])
quantidade = len(dadosusados)

# Inicializando listas
x = [0] * quantidade
y = [0] * quantidade
e = [0] * quantidade

xsoma = 0
ysoma = 0

# Calculando somas de x e y
for cont in range(quantidade):
    x[cont] = float(dadosusados.loc[cont])
    y[cont] = float(dadosusados1.loc[cont])
    xsoma = float(xsoma + x[cont])
    ysoma = float(ysoma + y[cont])

xmed = float(xsoma / quantidade)
ymed = float(ysoma / quantidade)

# Inicializando variáveis de soma
sxy = 0
syy = 0
sxx = 0
sqreg = 0
sqe = 0

# Calculando correlação e parâmetros
for cont1 in range(quantidade):
    somx = float(x[cont1] - xmed)
    somy = float(y[cont1] - ymed)
    sxy = float(somx * somy + sxy)
    sxx = float(somx**2 + sxx)
    syy = float(somy**2 + syy)

correlacao = float(sxy / (pow(sxx * syy, 1/2)))
b = float(sxy / sxx)
a = float(ymed - (b * xmed))

for cont2 in range(quantidade):
    sqe = float(((y[cont2] - (a + (b * x[cont2])))**2 + sqe))
    sqreg = float((a + (x[cont2] * b) - ymed)**2 + sqreg)

fo = float((sqreg) / ((sqe) / (quantidade - 2)))

# Preparando gráfico de função
X = np.arange(0, 10, 0.1)
Y = []

print('\n')
print('Respostas do trabalho:')

# a) Gráfico em relação aos valores de x
plt.title('Gráfico em relação a X')
plt.ylabel('Notas[Y]')
plt.xlabel('Tempo de Estudo[X]')
plt.hist(x, bins=40, ec="k", rwidth=0.7)
plt.show()
print('\n')

# a) Gráfico em relação aos valores de y
plt.title('Gráfico em relação a Y')
plt.ylabel('Notas[Y]')
plt.xlabel('Tempo de Estudo[X]')
plt.hist(y, bins=40, ec="k", rwidth=0.7, alpha=0.7)
plt.show()
print('\n')

# Gráfico da função
plt.title('Gráfico da função')
plt.ylabel('Notas[Y]')
plt.xlabel('Tempo de Estudo[X]')
plt.plot(x, y, "o")
plt.show()
print('\n')

print('\n')
print('b) A partir da distribuição, identificamos pontos influentes, que são observações capazes de impactar a linha de regressão de mínimos quadrados, alterando os valores de y.')
print('\n')
print('c) A partir do gráfico é possível identificar uma correlação se aproximando do 1.')
print('\n')
print('d) O coeficiente de correlação é: %.3f' % correlacao)
print('O coeficiente de correlação se aproximando do 1 diz que a reta dos mínimos quadrados tende a crescer.')
print('\n')
print('e) A reta é: Y = {} + {}X '.format(a, b))
print('  B1 = {}; B0 = {} e a variância = {}'.format(a, b, (syy / quantidade)))

for cont3 in range(len(X)):
    Y.append(a + b * X[cont3])

# f) Gráfico xy
plt.title('Gráfico xy')
plt.ylabel('Notas[Y]')
plt.xlabel('Tempo de Estudo[X]')
plt.plot(x, y, "o")
plt.plot(X, Y, color='orange')
plt.show()
print('f) A análise de regressão indica que a variável tempo de estudo tem um impacto significativa sobre a variável notas. Além disso, a conexão entre essas variáveis é bem capturada pela reta ajustada no modelo.')

# g) Cálculo dos resíduos
print('\n')
print('g) Os resíduos são:')
for cont3 in range(quantidade):
    e[cont3] = float(y[cont3] - (a + (b * x[cont3])))
    print('e{} = {}'.format((cont3 + 1), e[cont3]))

print('\n')
print('h) A análise dos resultados revela a presença de vários resíduos com valores extremamente altos e negativos. Isso sugere que algumas observações podem estar influenciando o modelo de forma desproporcional. Resíduos muito grandes indicam que essas observações podem estar afetando substancialmente a estimativa dos parâmetros no modelo de regressão.')


print('\n')
print('i) Montando a tabela ANOVA:')
print('  FV     |    GL      |         SQ           |         QM        |  Fo')
print('Regressão|    1       |   {:.2f}  | {:.2f} | {:.2f}'.format((sqreg), (sqreg), fo))
print('Erro     |  {:.2f}    |   {:.2f}   | {:.2f}'.format((quantidade - 2), (sqe), (sqe / (quantidade - 2))))
print('Total    |  {:.2f}    |   {:.2f}'.format((quantidade - 1), (ysoma**2)))

if (sqreg / (sqe / (quantidade - 2))) < 5.59:
    print('i) Rejeitamos H0!')
else:
    print('i) Rejeitamos h1!')

# j) Gráfico xy (sem pontos influentes)
plt.title('Gráfico xy (s/ pontos influentes)')
plt.ylabel('Notas[Y]')
plt.xlabel('Tempo de Estudo[X]')
plt.xlim(0, 10)
plt.plot(x, y, "o")
plt.plot(X, Y, color='orange')
plt.show()