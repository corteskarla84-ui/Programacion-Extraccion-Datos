Inventario = {}

def AgregarP(inv,codigo,nombre,precio,cantidad):
    if codigo in inv:
        return False

    inv[codigo]= {"Nombre":nombre,
                  "Precio":float(precio),
                  "Cantidad":int(cantidad)}
    return True

def EditarP(inv,codigo,nombre=None,precio=None,cantidad=None):
    if codigo not in inv:
        return False

    if nombre is not None:
        inv[codigo]["Nombre"]=nombre

    if precio is not None:
        inv[codigo]["Precio"]=float(precio)

    if cantidad is not None:
        inv[codigo]["Cantidad"]=int(cantidad)
    return True

def EliminarP(inv,codigo):
    if codigo in inv:
        del inv[codigo]
        return True
    return False

def Venta(inv,codigo,cantidad):
    if codigo not in inv:
        return False

    if inv[codigo]["Cantidad"] < cantidad:
        return False

    inv[codigo]["Cantidad"] -= cantidad
    return True

def ImprimirInv(inv):
    print("=== INVENTARIO ===")

    if not inv:
        print("Vacio")
        return

    for codigo,info in inv.items():
        print(f"Codigo: {codigo} | Nombre: {info["Nombre"]} | Precio: {info["Precio"]} | "
              f"Cantidad: {info["Cantidad"]}")


if __name__ == "__main__":
    # Agregar
    print("\nAgregar A1:", AgregarP(Inventario, "A1", "Lapiz", 5.5, 100))
    print("\nAgregar A2:", AgregarP(Inventario, "A2", "Cuaderno", 25.0, 50))
    print("==============================================")
    ImprimirInv(Inventario)

    # Editar
    print("==============================================")
    print("Editar Precio y Cantidad de A2:", EditarP(Inventario, "A2", precio=27.0, cantidad=60))
    print("==============================================")
    ImprimirInv(Inventario)

    # Vender
    print("==============================================")
    print("Vender A1:", Venta(Inventario, "A1", 20))
    #Vender para provocar error
    print("\nVender A2:", Venta(Inventario, "A2", 100))
    print("==============================================")
    ImprimirInv(Inventario)

    # Eliminar
    print("==============================================")
    print("Eliminar A2:", EliminarP(Inventario, "A2"))
    print("==============================================")
    ImprimirInv(Inventario)