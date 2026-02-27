def hanoi_while(n, origen="A", destino="C", aux="B"):
    movimientos = []
    
    def generar(n, o, d, a):
        if n > 0:
            generar(n-1, o, a, d)
            movimientos.append(f"Mover {n} de {o} → {d}")
            generar(n-1, a, d, o)
    
    generar(n, origen, destino, aux)
    
    i = 0
    while i < len(movimientos):
        print(movimientos[i])
        i += 1
    
    print(f"\n✓ {len(movimientos)} movimientos")

hanoi_while(3)


def hanoi_for(n, origen="A", destino="C", aux="B"):
    movimientos = []
    
    def generar(n, o, d, a):
        if n > 0:
            generar(n-1, o, a, d)
            movimientos.append(f"Mover {n} de {o} → {d}")
            generar(n-1, a, d, o)
    
    generar(n, origen, destino, aux)
    
    for mov in movimientos:
        print(mov)
    
    print(f"\n✓ {len(movimientos)} movimientos")

hanoi_for(3)


def hanoi_recursion(n, origen="A", destino="C", aux="B"):
    def mover(n, o, d, a):
        if n > 0:
            mover(n-1, o, a, d)
            print(f"Mover {n} de {o} → {d}")
            mover(n-1, a, d, o)
    
    mover(n, origen, destino, aux)
    print(f"\n✓ {2**n - 1} movimientos")

hanoi_recursion(3)
