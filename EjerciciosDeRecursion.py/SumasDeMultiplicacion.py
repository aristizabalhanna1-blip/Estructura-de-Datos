def multi_while(a, b):
    resultado = 0
    i = 0
    while i < b:
        resultado += a
        i += 1
    return resultado

print(multi_while(5, 3)) 


def multi_for(a, b):
    resultado = 0
    for _ in range(b):
        resultado += a
    return resultado

print(multi_for(5, 4))  


def multi_recursiva(a, b):
    if b == 0:
        return 0
    return a + multi_recursiva(a, b - 1)

print(multi_recursiva(2, 6))  
