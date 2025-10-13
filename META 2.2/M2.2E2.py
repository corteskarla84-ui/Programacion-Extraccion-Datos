# Cortes Fregoso Karla Stephanie (2209422)
# Grupo 951 LNI | Fecha: 12/10/25
# Desarrollar una clase llamada PaisSQL que herede de  SQLConnect. Debe agregar los atributos correspondientes de la clase padre.
# Debe agregar los siguientes métodos:
# insertar(id, nombre): Mé para insertar datos en la Tabla Pais, debe recibir como parámetro las columnas de la tabla y debe retornar True si se inserta el dato o False en caso contrario.
# editar(id, nombre_nuevo): Mé para editar el nombre en la Tabla País. Validar que nombre no exista en la tabla.
# eliminar(id): Mét para eliminar un elemento de la Tabla País. Debe tener como parámetro la llave primaria, retorna True si logró eliminarse y False en caso contrario.
# consultar(filter): Mét que recibe un filtro(cadena) y retorna una lista de tuplas con los resultados del filtro de la Tabla País. Ejemplo: “id = 1” , “nombre like %A%”

from mysql.connector import Error
from SQLConnect import SQLConnect

class PaisSQL(SQLConnect):
    def __init__(self, host, usuario, password, base_datos):
        super().__init__(host, usuario, password, base_datos)


    def insertar(self, id_val, nombre):
        try:
            cnx = self.conectar()
            cur = cnx.cursor()
            cur.execute("INSERT INTO Pais (id, nombre) VALUES (%s, %s)", (id_val, nombre))
            cnx.commit() #Confirma cambios
            return True
        except Error as e:
            print("Error al insertar:", e)
            cnx.rollback() #Revierte cambios
            return False

    def editar(self, id_val, nombre_nuevo):
        try:
            cnx = self.conectar()
            cur = cnx.cursor()
            cur.execute("SELECT COUNT(*) FROM Pais WHERE nombre = %s AND id != %s", (nombre_nuevo, id_val))
            if cur.fetchone()[0] > 0:
                print("El nombre ya existe en otro pais")
                return False

            cur.execute("UPDATE Pais SET nombre = %s WHERE id = %s", (nombre_nuevo, id_val))
            cnx.commit()
            return cur.rowcount > 0
        except Error as e:
            print("Error al editar:", e)
            cnx.rollback()
            return False


    def eliminar(self, id_val):
        try:
            cnx = self.conectar()
            cur = cnx.cursor()
            cur.execute("DELETE FROM Pais WHERE id = %s", (id_val,))
            cnx.commit()
            return cur.rowcount > 0
        except Error as e:
            print("Error al eliminar:", e)
            cnx.rollback()
            return False

    def consultar(self, filtro=""):
        try:
            cnx = self.conectar()
            cur = cnx.cursor()
            if filtro:
                sql = f"SELECT * FROM Pais WHERE {filtro}"
            else:
                sql = "SELECT * FROM Pais"
            cur.execute(sql)
            return cur.fetchall()
        except Error as e:
            print("Error al consultar:", e)
            return []

    def desconectar(self):
        if self.conexion:
            self.conexion.close()
            print("Conexion cerrada correctamente")


if __name__ == "__main__":
    pais = PaisSQL("localhost", "root", "Carro1406M.", "olimpiadas")
    print("Insertar")
    pais.insertar(1, "Mexico")
    print("===================================")
    print("Editar")
    pais.editar(1, "Francia")
    print("===================================")
    print("Consulta")
    resultados = pais.consultar("id = 1")
    print(resultados)
    print("===================================")
    print("Eliminar")
    pais.eliminar(1)
    print("===================================")
    pais.desconectar()