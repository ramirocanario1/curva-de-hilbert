import turtle
import click

@click.command()
@click.option('--iter', default=1, help='Cantidad de iteraciones.', prompt='iteraciones: ')
@click.option('--segm', default=20, help='Pixeles de longitud de cada segmento.')
def programa(iter, segm):
    print('Se han escogido {} iteraciones, con segmentos de {}px de longitud'.format(iter, segm))

# -----------PARÁMETROS MODIFICABLES----------
cadena_inicial = 'X'
reglas = {
    'X':'+YF-XFX-FY+',
    'Y':'-XF+YFY+FX-'
}
angulo = 90
iteraciones = 6
longitud_segmento = 10
# --------------------------------------------

velocidades = {
    (1, 'muy lenta'),
    (3, 'lenta'),
    (6, 'normal'),
    (10, 'rápida'),
    (0, 'muy rápida')
}
i = 1

# Recibe una cadena y la procesa, transformando cada caracter en su correspondiente valor del diccionario 'reglas'. Retorna la cadena resultante
def procesarCadena(cadena):

    resultado = ''

    for caracter in cadena:
        if caracter in reglas:
            resultado += reglas[caracter]
        else:
            resultado += caracter

    return resultado

cadena = cadena_inicial

for i in range(0, iteraciones):
    cadena = procesarCadena(cadena)

print('La cadena inicial {} ha sido procesada {} veces. Resultado:\n{}'.format(cadena_inicial, iteraciones, cadena))

# def cambiar_velocidad(x, y):
#     global i
#     i += 1
#     print('Se hizo click en {} {}'.format(x, y))
#     skk.speed(velocidades[i][1])
#     print('La velocidad es: {}'.format(velocidades[i][2]))

wn = turtle.Screen()
wn.bgcolor("#EF0FFF")
wn.title("Curva de Hilbert")
skk = turtle.Turtle()
skk.speed(0)
skk.penup()
skk.setposition(-400,-400)
skk.pencolor("white")
skk.width(4)
skk.pendown()
skk.hideturtle()
# wn.onscreenclick(fun=cambiar_velocidad)

wn.setup(width=.8, height=.8)
for simbolo in cadena:
    if simbolo == 'F':
        skk.forward(longitud_segmento)
    elif simbolo == '+':
        skk.left(angulo)
    elif simbolo == '-':
        skk.right(angulo)
turtle.done()