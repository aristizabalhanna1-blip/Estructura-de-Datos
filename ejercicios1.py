def factorial_while(n)->int:
    while n > 1: 
        resultado = n * factorial_while(n-1)
        return resultado
print(factorial_while(9)) 

    
