def suma_while_string(numero: int) -> int:
    if numero == 0:
        return 0
    cadena = str(numero)
    suma = 0
    indice = 0
    while indice < len(cadena):
        suma += int(cadena[indice])
        indice += 1
    return suma

print(suma_while_string(2345)) 


def suma_for_invertido(numero: int) -> int:
    suma = 0
    cadena = str(abs(numero))  
    for i in range(len(cadena) - 1, -1, -1):  
        suma += int(cadena[i])
    return suma

print(suma_for_invertido(1234))  



def suma_recursiva_cola(n: int, acumulado: int = 0) -> int:
    if n == 0:
        return acumulado
    digito = n % 10
    return suma_recursiva_cola(n // 10, acumulado + digito)

print(suma_recursiva_cola(5678))  



