# Cortes Fregoso Karla Stephanie (2209422)
# Grupo 951 LNI | Fecha: 12/10/25
# Desarrollar una clase llamada SQLConnect que tenga como atributos: host, user, password, database, driver (Caso SQL SERVER).
# Debe tener los siguientes métodos:
# conectar() : Debe conectarse a la base de datos usando los atributos, debe retornar el objeto de conexión.
# desconectar(): Debe desconectar la base de datos. No debe retornar nada Investigar M CLOSE.

from mysql.connector import connect, Error

class SQLConnect:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.conexion = None  #Objeto conexion

    def conectar(self):
        try:
            self.conexion = connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            print("Conexion exitosa")
            return self.conexion
        except Error as e:
            print("Error al conectar:", e)

    def desconectar(self):
        if self.conexion:
            self.conexion.close()
            print("Conexion cerrada correctamente")


if __name__ == "__main__":
    db = SQLConnect("localhost", "root", "Carro1406M.", "olimpiadas")
    conexion = db.conectar()
    db.desconectar()

