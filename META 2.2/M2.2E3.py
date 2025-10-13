# Cortes Fregoso Karla Stephanie (2209422)
# Grupo 951 LNI | Fecha: 12/10/25
# Desarrollar una clase llamada OlimpiadaSQL que herede de  SQLConnect. Debe agregar los atributos correspondientes de la clase padre.
# Debe agregar los siguientes métodos:
# insertar(id, year): Mét para insertar datos en la Tabla Olimpiada, debe recibir como parámetro las columnas de la tabla y debe retornar True si se inserta el dato o False en caso contrario.
# editar(id, year_nuevo): Mét para editar el año en la Tabla Olimpiada. Validar que el año no exista en la tabla.
# eliminar(id): Mét para eliminar un elemento de la Tabla Olimpiada. Debe tener como parámetro la llave primaria, retorna True si logró eliminarse y False en caso contrario.
# consultar(filter): Mét que recibe un filtro(cadena) y retorna una lista de tuplas con los resultados del filtro de la Tabla Olimpiada. Ejemplo: “id = 1” , “year > 1990”

from mysql.connector import Error
from SQLConnect import SQLConnect

class OlimpiadaSQL(SQLConnect):
    def __init__(self, host, usuario, password, base_datos):
        super().__init__(host, usuario, password, base_datos)

    def insertar(self, id, year_olimpiada):
        try:
            conexion = self.conectar()
            cursor = conexion.cursor()
            cursor.execute("INSERT INTO Olimpiada (id, year_olimpiada) VALUES (%s, %s)", (id, year_olimpiada))
            conexion.commit()
            cursor.close()
            return True
        except Error as e:
            print("Error al insertar:", e)
            conexion.rollback()
            return False

    def editar(self, id, year_nuevo):
        try:
            conexion = self.conectar()
            cursor = conexion.cursor()

            # Validar que no exista ese año en otra fila
            cursor.execute("SELECT COUNT(*) FROM Olimpiada WHERE year_olimpiada = %s AND id <> %s", (year_nuevo, id))
            if cursor.fetchone()[0] > 0:
                print("Ese año ya existe, no se puede actualizar")
                return False

            cursor.execute("UPDATE Olimpiada SET year_olimpiada = %s WHERE id = %s", (year_nuevo, id))
            conexion.commit()
            actualizado = cursor.rowcount > 0
            cursor.close()
            return actualizado
        except Error as e:
            print("Error al editar:", e)
            conexion.rollback()
            return False

    def eliminar(self, id):
        try:
            conexion = self.conectar()
            cursor = conexion.cursor()
            cursor.execute("DELETE FROM Olimpiada WHERE id = %s", (id,))
            conexion.commit()
            eliminado = cursor.rowcount > 0
            cursor.close()
            return eliminado
        except Error as e:
            print("Error al eliminar:", e)
            conexion.rollback()
            return False

    def consultar(self, filtro):
        try:
            conexion = self.conectar()
            cursor = conexion.cursor()
            consulta = "SELECT id, year_olimpiada FROM Olimpiada"
            cursor.execute(consulta)
            resultados = cursor.fetchall()
            cursor.close()
            return resultados
        except Error as e:
            print("Error al consultar:", e)
            return []

    def desconectar(self):
        if self.conexion:
            self.conexion.close()
            print("Conexion cerrada correctamente")

if __name__ == "__main__":
    olimpiada = OlimpiadaSQL("localhost", "root", "Carro1406M.", "olimpiadas")
    print("Insertar")
    olimpiada.insertar(1, 2000)
    print("===================================")
    print("Editar")
    olimpiada.editar(1, 2005)
    print("===================================")
    print("Eliminar")
    olimpiada.eliminar(1)
    print("===================================")
    print("Consulta")
    resultados = olimpiada.consultar("year_olimpiada > 1990")
    print(resultados)
    print("===================================")
    olimpiada.desconectar()
