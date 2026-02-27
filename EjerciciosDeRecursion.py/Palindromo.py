def palindromo_while(cadena: str) -> bool:
    limpia = ''.join(c.lower() for c in cadena if c.isalpha())
    if len(limpia) <= 1:
        return True
    
    inicio, fin = 0, len(limpia) - 1
    while inicio < fin:
        if limpia[inicio] != limpia[fin]:
            return False
        inicio += 1
        fin -= 1
    return True

print(palindromo_while("A man a plan a canal Panama"))  


def palindromo_for(texto: str) -> bool:
    texto_limpio = ''.join(c.lower() for c in texto if c.isalnum())
    
    for i in range(len(texto_limpio) // 2):
        if texto_limpio[i] != texto_limpio[len(texto_limpio) - 1 - i]:
            return False
    return True

print(palindromo_for("¿Era una raza?")) 


def palindromo_recursivo(cadena: str) -> bool:
    limpia = ''.join(c.lower() for c in cadena if c.isalpha())
    
    def _es_palindromo(texto: str) -> bool:
        if len(texto) <= 1:
            return True
        if texto[0] != texto[-1]:
            return False
        return _es_palindromo(texto[1:-1])
    
    return _es_palindromo(limpia)

print(palindromo_recursivo("reconocer")) 
