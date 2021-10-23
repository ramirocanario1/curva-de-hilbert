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

cadena_inicial = 'X'    # TODO puede ser parametro?
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
@click.option('-c', '--mostrar-cadena', default=False, show_default=True, type=bool, help='Mostrar cadena de simbolos.')

def programa(iteraciones, segmento, angulo, velocidad, background, pencolor, width, ocultar, shape, mostrar_cadena):
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
    -> Mostrar cadena: {}  '''
    .format(iteraciones, segmento, angulo, velocidad, background, pencolor, width, ocultar, shape, mostrar_cadena))

    cadena = cadena_inicial

    for i in range(0, iteraciones):
        cadena = procesarCadena(cadena)

    if mostrar_cadena:
        input('\nPresione una tecla para mostrar la cadena')
        print(cadena)

    

if __name__ == '__main__':
    programa()