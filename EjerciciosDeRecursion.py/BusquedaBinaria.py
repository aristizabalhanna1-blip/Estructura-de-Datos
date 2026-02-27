def busqueda_while_segura(arr, target):
    if not arr or arr[0] > target or arr[-1] < target:
        return -1
    
    left, right = 0, len(arr) - 1
    while left <= right:
        medio = left + (right - left) // 2
        
        if arr[medio] == target:
            return medio
        elif target < arr[medio]:
            right = medio - 1
        else:
            left = medio + 1
    return -1

print(busqueda_while_segura([1,2,3,4,5,6,7,8,9], 9))  # 8


def busqueda_for_particiones(arr, objetivo):
    if len(arr) == 0:
        return -1
    
    izq, der = 0, len(arr) - 1
    pasos = 0
    max_pasos = len(arr).bit_length()  # log2(n) aprox
    
    for _ in range(max_pasos):
        if izq > der:
            return -1
        
        medio = (izq + der) // 2
        pasos += 1
        
        if arr[medio] == objetivo:
            print(f"Encontrado en {pasos} pasos")
            return medio
        elif objetivo < arr[medio]:
            der = medio - 1
        else:
            izq = medio + 1
    
    return -1

print(busqueda_for_particiones([1,2,3,4,5,6,7,8,9], 5)) 


def busqueda_recursiva_wrapper(arr, objetivo):
    def _recursiva(izq, der):
        if izq > der:
            return -1
        
        medio = izq + (der - izq) // 2
        
        if arr[medio] == objetivo:
            return medio
        elif objetivo < arr[medio]:
            return _recursiva(izq, medio - 1)
        else:
            return _recursiva(medio + 1, der)
    
    if not arr:
        return -1
    return _recursiva(0, len(arr) - 1)

print(busqueda_recursiva_wrapper([1,2,3,4,5,6,7,8,9], 7))  # 6
