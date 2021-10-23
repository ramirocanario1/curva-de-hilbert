
# -----------PARÁMETROS MODIFICABLES----------
cadena_inicial = 'X'
reglas = {
    'X':'+YF-XFX-FY+',
    'Y':'-XF+YFY+FX-'
}
angulo = 90
iteraciones = 3
# --------------------------------------------

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

print('La cadena inicial {} ha sido procesada {} veces.Resultado:\n{}'.format(cadena_inicial, iteraciones, cadena))

