def Reservar(habitacion, disponible, reservada):
    if habitacion in disponible:
        disponible.remove(habitacion)
        reservada.add(habitacion)
        return True
    return False

def liberar(habitacion, disponible, reservada):
    if habitacion in reservada:
        reservada.remove(habitacion)
        disponible.add(habitacion)
        return True
    return False

def Estado(disponibles, reservadas):
    print("Disponibles:", sorted(disponibles))
    print("Reservadas :", sorted(reservadas))

if __name__ == "__main__":
    # Pruebas
    disponibles = {115, 109, 112, 205, 505}
    reservadas = set()

    Estado(disponibles, reservadas)
    print("=================================================================")
    print("Reservar 115:", Reservar(115, disponibles, reservadas))
    print("=================================================================")
    print("Reservar 109:", Reservar(109, disponibles, reservadas))
    print("=================================================================")
    #Reservar una inexistente
    print("Reservar 500:", Reservar(500, disponibles, reservadas))
    print("=================================================================")
    Estado(disponibles, reservadas)
    print("=================================================================")
    print("Liberar 109:", liberar(109, disponibles, reservadas))
    print("=================================================================")
    #Liberar una no ocupada
    print("Liberar 205:", liberar(205, disponibles, reservadas))
    print("=================================================================")
    Estado(disponibles, reservadas)
