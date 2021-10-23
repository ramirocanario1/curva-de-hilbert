# from typing_extensions import Required
import click
import turtle
from random import randrange

from click.types import INT, STRING, IntParamType, IntRange

colores = [
    'black',
    'white',
    'gray',
    'cornflower blue',
    'blue',
    'navy',
    'deep sky blue',
    'cyan',
    'teal',
    'pale green',
    'spring green',
    'lime green',
    'green',
    'green yellow',
    'yellow',
    'gold',
    'darkorange',
    'maroon',
    'red',
    'crimson',
    'deep pink',
    'violet',
    'purple',
    'magenta'
]

shapes = [
    'arrow',
    'turtle',
    'circle',
    'square',
    'triangle',
    'classic'
]

reglas = {
    'X':'+YF-XFX-FY+',
    'Y':'-XF+YFY+FX-'
}

# Recibe una cadena y la procesa, transformando cada caracter en su correspondiente valor del diccionario 'reglas'. Retorna la cadena resultante
def procesarCadena(cadena):

    resultado = ''

    for caracter in cadena:
        if caracter in reglas:
            resultado += reglas[caracter]
        else:
            resultado += caracter

    return resultado

def dibujar(cadena, tortuga, segmento, angulo):
    for simbolo in cadena:
        if simbolo == 'F':
            tortuga.forward(segmento)
        elif simbolo == '+':
            tortuga.left(angulo)
        elif simbolo == '-':
            tortuga.right(angulo)

# Al pulsar click en el dibujo, se incrementa su velocidad
def acelerar(x, y):
    ventana = turtle.Screen()
    tortuga = ventana.turtles()[0]

    tortuga.speed(0)
    ventana.tracer(10)

# Si la opción '-r' está activada, la línea va alternando entre los colores
def cambiar_colores():
    ventana = turtle.Screen()
    tortuga = ventana.turtles()[0]
    
    tortuga.color(colores[randrange(3, len(colores))])

    ventana.ontimer(cambiar_colores, 250)

@click.command()
@click.option('-i', '--iteraciones', required=True, type=click.IntRange(1, 10, clamp=True), help='Cantidad de iteraciones (1..10).')
@click.option('-s', '--segmento', default=10, show_default=True, type=int, help='Longitud en px de cada segmento.')
@click.option('-a', '--angulo', default=90, show_default=True, type=click.IntRange(1, 360, clamp=True), help='Angulo de cada giro (grados).')
@click.option('-v', '--velocidad', default=6, show_default=True, type=click.IntRange(1, 11), help='Velocidad del dibujo. 1: muy lento, 11: muy rapido.')
@click.option('-bg', '--background', default='white', show_default=True, type=click.Choice(colores), help='Color del fondo de la ventana.')
@click.option('-pc', '--pencolor', default='black', show_default=True, type=click.Choice(colores), help='Color de la linea.')
@click.option('-w', '--width', default=2, show_default=True, type=int, help='Grosor de la linea (px).')
@click.option('-o', '--ocultar', is_flag=True, help='Indica si desea mostrar el cursor mientras va dibujando')
@click.option('-sh', '--shape', default='arrow', show_default=True, type=click.Choice(shapes), help='Forma del cursor.')
@click.option('-t', '--tracer', default=1, show_default=True, type=click.IntRange(1, 5, clamp=True), help='Periodo de actualizacion de pantalla.')
@click.option('-ci', '--cadena-inicial', default='X', show_default=True, help='Cadena inicial.')
@click.option('-c', '--mostrar-cadena', is_flag=True, help='Indica que desea mostrar la cadena generada')
@click.option('-h', '--screen-size', default=2000, type=click.IntRange(500, 10000), help='Tamano de la hoja (NxN).')
@click.option('-ws', '--window-size', default=0.8, type=click.FloatRange(0.1, 1.0), help='Tamano de la ventana, en proporcion a la pantalla (%).')
@click.option('-pi', '--posicion-inicial', default=-400, type=click.INT, help='Posicion inicial del dibujo (0 es el centro de la hoja).')
@click.option('-r', '--rainbow', is_flag=True, help='La linea alterna entre los distintos colores')

def programa(iteraciones, segmento, angulo, velocidad, background, pencolor, width, ocultar, shape, tracer, cadena_inicial, mostrar_cadena, screen_size, window_size, posicion_inicial, rainbow):
    print('''Parametros de ejecucion: 
    -> Cantidad de iteraciones: {}
    -> Longitud de segmento: {} px
    -> Angulo de giro: {} grados
    -> Velocidad del dibujo: {}
    -> Color de fondo: {}
    -> Color de linea: {}
    -> Ancho de linea: {} px
    -> Ocultar cursor: {}
    -> Forma de cursor: {}
    -> Periodo de actualizacion: {}
    -> Cadena inicial: {}
    -> Mostrar cadena: {}  
    -> Tamano de ventana: {}%
    -> Tamano de hoja: {}x{}
    -> Posicion inicial: {}, {}'''
    .format(iteraciones, 
            segmento, 
            angulo, 
            velocidad, 
            background, 
            pencolor, 
            width, 
            ocultar, 
            shape, 
            tracer,
            cadena_inicial, 
            mostrar_cadena, 
            window_size*100, 
            screen_size, screen_size, 
            posicion_inicial, posicion_inicial))

    cadena = cadena_inicial

    for i in range(0, iteraciones):
        cadena = procesarCadena(cadena)

    if mostrar_cadena:
        input('\nPresione una tecla para mostrar la cadena.')
        print(cadena)

    # Creo una ventana y una tortuga
    input('\nPresione una tecla para comenzar a dibujar.')
    ventana = turtle.Screen()
    ventana.title('Curva de Hilbert')
    ventana.setup(window_size, window_size)
    ventana.screensize(screen_size, screen_size)
    tortuga = turtle.Turtle()

    # Posiciono la tortuga
    tortuga.penup()
    tortuga.setposition(posicion_inicial, posicion_inicial)
    tortuga.pendown()

    # Establezco los eventos
    ventana.onscreenclick(acelerar)
    if rainbow:
        ventana.ontimer(cambiar_colores, 500)

    # Configuro el dibujo a partir de los parametros
    tortuga.speed(velocidad)

    if rainbow:
        ventana.bgcolor('black')
    else:
        ventana.bgcolor(background)

    tortuga.pencolor(pencolor)
    tortuga.width(width)
    if ocultar:
        tortuga.hideturtle()
    tortuga.shape(shape)
    ventana.tracer(tracer)

    dibujar(cadena, tortuga, segmento, angulo)
    turtle.done()

if __name__ == '__main__':
    programa()