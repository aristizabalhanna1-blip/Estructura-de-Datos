numeros = [3, 5, 8, 9, 12]

def sumar_numeros(numeros: list) -> int:
    resultado = 0
    for numero in numeros:
        resultado += numero
    return resultado

def sumar_numeros_while(numero: list) -> int:
    resultado = 0
    i = 0
    while i < len(numeros):
        resultado += numero[i]
        i += 1
    return resultado

def sumar_numeros_recursivo(numeros: list) -> int:
    if not numeros:
        return 0  
    else:
        return numeros[0] + sumar_numeros_recursivo(numeros[1:])
    
print(list(range(1, 5)))