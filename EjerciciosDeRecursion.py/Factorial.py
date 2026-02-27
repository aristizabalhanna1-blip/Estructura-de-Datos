def factorial_usando_while(num) -> int:
    if num < 0:
        return 0  # O lanza error si prefieres
    producto = 1
    contador = 2
    while contador <= num:
        producto *= contador
        contador += 1
    return producto

print(factorial_usando_while(5))  


from functools import reduce

def factorial_for(numero: int) -> int:
    if numero < 2:
        return 1
    numeros = list(range(2, numero + 1))
    return reduce(lambda x, y: x * y, numeros, 1)

print(factorial_for(4))  


def factorial_tail_rec(n: int, acumulado=1) -> int:
    if n < 2:
        return acumulado
    return factorial_tail_rec(n - 1, n * acumulado)

print(factorial_tail_rec(6))  
