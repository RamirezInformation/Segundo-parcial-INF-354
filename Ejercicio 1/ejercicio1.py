import random
import math
from sklearn import datasets


iris = datasets.load_iris()

def ObtPesos(n):
    p = []
    for i in range(n):
        p.append(random.uniform(0, 1))
    return p

def productoPunto(x,y):
    sum = 0
    for (i, j) in zip(x,y):
        sum += i*j
    return sum

def sig(x):
    return 1 / math.exp(-x)

def prediccion(entradas, pesos, yd, bias = 1):
    for  i, entrada in enumerate(entradas):
        y = productoPunto(entrada, pesos) + bias #capa1
        capa2 = sig(y)
        print('y:',  y)
        print('sig:',  capa2)
        if y>=0:
            y = 1
        else:
            y = -1
        error = yd[i] - y
        print('error: ', error)


entradas = iris.data

pesos = ObtPesos(entradas[0].size)

punto = productoPunto(entradas, pesos)

prediccion(entradas, pesos, iris.target)
