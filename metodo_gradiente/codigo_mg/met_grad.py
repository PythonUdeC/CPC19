#! /usr/bin/python

import numpy as np
import sys
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy import stats
from func import funcion_costo, gradDecent, plot_linreg , plot_data
from plor_linreg import plot_linreg

data = np.genfromtxt(sys.argv[1], delimiter=',', names=['x', 'y'])

#Preprocesamiento de los datos
Y = data['y']
m = len(Y)
Y.shape = (m,1)
X_org = data['x']
X_org.shape = (m,1)

#El numero de puntos en el set de data
m = len(Y)
#Inicializar la matriz theta
theta = np.zeros((2,1))
#insertar una columna de unos al comienzo del array X
X = np.insert(X_org,0,1,axis=1)

#Graficar los datos:
plot_data(X_org,Y)

sys.exit(1)
#LLamo a la funcion de costo
funcion_costo(X,Y,m,theta) 
b, a = gradDecent(X,Y,m,theta)

#regresion lineal implementada en scipy
slope, intercept, r_value, p_value, slope_std_error = stats.linregress(X[:,1] ,Y[:,0])

print "a de scipy: " +str(slope)
print "b de scipy: " +str(intercept)

#plot_linreg(X[:,1],Y[:,0],a,b)


