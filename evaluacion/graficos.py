# -*- coding: UTF-8 -*-
from matplotlib.pyplot import *
from numpy import *

preguntas =['La calidad con que los profesores explican la materia', 
            'El nivel de profundidad con que los profesores han entregado los contenidos', 
            u'¿Cómo es la relación entre el nivel y cantidad de los contenidos entregados?',
            u'La capacidad de los profesores para estimular el interés y atención de los participantes',
            u'La disposición del profesor a estar accesible para acoger consultas de parte de los participantes',
            'El aporte del curso a su desarrollo personal y profesional',
            'Se utilizan los materiales y recursos disponibles en el aula',
            u'La preparación de las clases',
            'El aporte de la asistencia a clase para comprender los contenidos del curso',
            u'El entusiasmo que demuestra el profesor al enseñar esta materia',
            u'El uso de tecnologías de apoyo al curso (sitio web, internet, etc.) como un complemento de clase presencial',
            u'El aporte de las prácticas al curso']

data = genfromtxt('respuestas.txt', skip_header=2)

for p in range(12):
    figure()
    r = data[p,1:]
    hist(r,range(7), align='left')
    xlim(-1,6)
    ylim(0,len(r)+1)
    title(preguntas[p])
    xticks([0,1,2,3,4,5], ['Muy mal', 'Mal', 'Bueno', 'Muy bueno', 'No Aplic.', 'No Resp.'], fontsize=8)
    grid()
    savefig('pregunta '+str(p+1)+ '.pdf')
