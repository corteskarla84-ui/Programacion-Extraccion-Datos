Historial = []
Hoja = {"A1":15,"B2":9,"C3":5}


def RegistrarCambio(celda,NuevoValor):
    #Valor anterior
    Anterior = Hoja.get(celda,None)

    #Guardar
    Historial.append((celda,Anterior))

    #Actualizar
    Hoja[celda] = NuevoValor

def DeshacerCambio():
    if not Historial:
        print("No hay cambios para que deshagas")
        return

    #Ultimo cambio
    celda, Anterior = Historial.pop()

    #Restaurar valor anterior
    Hoja[celda] = Anterior


if __name__ == "__main__":
    # Simulación
    RegistrarCambio("A1", 19)
    RegistrarCambio("B2", 20)
    RegistrarCambio("C3", 2)

    print("Hoja actual:", Hoja)
    print("Historial:", Historial)
    print("======================================")

    DeshacerCambio()
    print("Despues de deshacer 1 cambio")
    print("Hoja actual:", Hoja)
    print("Historial:", Historial)
    print("======================================")

    DeshacerCambio()
    print("Despues de deshacer 2 cambios")
    print("Hoja actual:", Hoja)
    print("Historial:", Historial)
    print("======================================")

    DeshacerCambio()
    print("Despues de deshacer 3 cambios")
    print("Hoja actual:", Hoja)
    print("Historial:", Historial)
