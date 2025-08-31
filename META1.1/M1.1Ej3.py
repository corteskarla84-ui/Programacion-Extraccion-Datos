def VerificarRecorrida(almacen, movimientos):
    filas = len(almacen)
    columnas = len(almacen[0]) if filas > 0 else 0

    #Productos iniciales
    ProdRestantes = sum(
        fila.count('P') for fila in almacen
    )

    #Inicio
    x, y = 0, 0

    #Si inicio es obstáculo = inválido
    if almacen[x][y] == '#':
        return False

    #Si inicia sobre producto, lo recoge
    if almacen[x][y] == 'P':
        almacen[x][y] = '.'
        ProdRestantes -= 1

    #Movimientos
    M = {
        'R': (0, 1),
        'D': (1, 0),
        'L': (0, -1),
        'U': (-1, 0),
    }

    # Simular movimientos
    for m in movimientos:
        if m not in M:
            return False

        dx, dy = M[m]
        nx, ny = x + dx, y + dy

        #Verificar límites
        if not (0 <= nx < filas and 0 <= ny < columnas):
            return False

        #Verificar obstáculo
        if almacen[nx][ny] == '#':
            return False

        #Mover
        x, y = nx, ny

        #Recoger producto
        if almacen[x][y] == 'P':
            almacen[x][y] = '.'
            ProdRestantes -= 1

    #Final: productos recogidos y de vuelta al inicio
    return (ProdRestantes == 0) and (x == 0 and y == 0)

if __name__ == "__main__":
    almacen = [
        ['.', '.', '#', 'P'],
        ['.', '#', '.', '.'],
        ['P', '.', 'P', '.'],
        ['#', '.', '#', '.']
    ]

    movimientos_correctos = ['D','D','R','R','U','R','U','D','L','D','L','L','U','U']

    print(VerificarRecorrida([fila[:] for fila in almacen], movimientos_correctos))

