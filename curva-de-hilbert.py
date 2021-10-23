# from typing_extensions import Required
import click
import turtle

from click.types import INT, STRING, IntRange

colores = [
    'white',
    'black',
    'red',
    'green',
    'blue',
    'yellow',
    'orange',
    'maroon',
    'violet',
    'purple',
    'navy',
    'skyblue',
    'cyan',
    'gray',
    'gold',
]

shapes = [
    'arrow',
    'turtle',
    'circle',
    'square',
    'triangle',
    'classic'
]

# cadena_inicial = 'X'    # TODO puede ser parametro?
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

@click.command()
@click.option('-i', '--iteraciones', required=True, type=click.IntRange(1, 10, clamp=True), help='Cantidad de iteraciones (1..10).')
@click.option('-s', '--segmento', default=10, show_default=True, type=int, help='Longitud en px de cada segmento.')
@click.option('-a', '--angulo', default=90, show_default=True, type=click.IntRange(1, 360, clamp=True), help='Angulo de cada giro (grados).')
@click.option('-v', '--velocidad', default=6, show_default=True, type=click.IntRange(1, 11), help='Velocidad del dibujo. 1: muy lento, 11: muy rapido.')
@click.option('-bg', '--background', default='white', show_default=True, type=click.Choice(colores), help='Color del fondo de la ventana.')
@click.option('-pc', '--pencolor', default='black', show_default=True, type=click.Choice(colores), help='Color de la linea.')
@click.option('-w', '--width', default=2, show_default=True, type=int, help='Grosor de la linea (px).')
@click.option('--ocultar/--no-ocultar', default=False, show_default=True, help='Ocultar o mostrar cursor.')
@click.option('-sh', '--shape', default='arrow', show_default=True, type=click.Choice(shapes), help='Forma del cursor.')
@click.option('-t', '--tracer', default=1, show_default=True, type=click.IntRange(1, 5, clamp=True), help='Periodo de actualizacion de pantalla')
@click.option('-ci', '--cadena-inicial', default='X', show_default=True, help='Cadena inicial')
@click.option('-c', '--mostrar-cadena', default=False, show_default=True, type=bool, help='Mostrar cadena de simbolos.')

def programa(iteraciones, segmento, angulo, velocidad, background, pencolor, width, ocultar, shape, tracer, cadena_inicial, mostrar_cadena):
    print('''Parametros de ejecucion: 
    -> Cantidad de iteraciones: {}
    -> Longitud de segmento: {} px
    -> Angulo de giro: {} grados
    -> Velocidad del dibujo: {}
    -> Color de fondo: {}
    -> Color de linea: {}
    -> Ancho de linea: {} px
    -> Mostrar cursor: {}
    -> Forma de cursor: {}
    -> Periodo de actualizacion: {}
    -> Cadena inicial: {}
    -> Mostrar cadena: {}  '''
    .format(iteraciones, segmento, angulo, velocidad, background, pencolor, width, ocultar, shape, tracer,cadena_inicial, mostrar_cadena))

    cadena = cadena_inicial

    for i in range(0, iteraciones):
        cadena = procesarCadena(cadena)

    if mostrar_cadena:
        input('\nPresione una tecla para mostrar la cadena.')
        print(cadena)
    else:
        input('\nPresione una tecla para comenzar a dibujar.')

    # Creo una ventana y una tortuga
    ventana = turtle.Screen()
    ventana.title('Curva de Hilbert')
    ventana.setup(width=.8, height=.8)  # TODO parametros?
    tortuga = turtle.Turtle()

    # Posiciono la tortuga
    tortuga.penup()
    tortuga.setposition(-400, -400) #TODO hardcodeado!
    tortuga.pendown()

    # Configuro el dibujo a partir de los parametros
    tortuga.speed(velocidad)
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