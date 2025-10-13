# Cortes Fregoso Karla Stephanie (2209422)
# Grupo 951 LNI | Fecha: 12/10/25
# Desarrollar una clase llamada ResultadosSQL que herede de  SQLConnect. Debe agregar los atributos correspondientes de la clase padre.
# Debe agregar los siguientes métodos:
# insertar(idOlimpiada, idPais, idGenero, oro, plata, bronce): Mét para insertar datos en la Tabla Resultados, debe recibir como parámetro las columnas de la tabla y debe retornar True si se inserta el dato o False en caso contrario.
# editar(idOlimpiada, idPais, idGenero, oro, plata, bronce): Mét para editar oro, plata, bronce en la Tabla Resultados. Validar que sean valores enteros positivos.
# eliminar(idOlimpiada, idPais, idGenero): Mét para eliminar un elemento de la Tabla Resultados. Debe tener como parámetro la llave primaria compuesta, retorna True si logró eliminarse y False en caso contrario.
# consultar(filter): Mét que recibe un filtro(cadena) y retorna una lista de tuplas con los resultados del filtro de la Tabla Resultados. Ejemplo: “idPais = 1” , “idPais = 1 and idOlimpiada=2”

from mysql.connector import Error
from SQLConnect import SQLConnect


class ResultadosMySQL(SQLConnect):
    def __init__(self, host, usuario, password, base_datos):
        super().__init__(host, usuario, password, base_datos)
        self.conn = self.conectar()
        if self.conn:
            self.cursor = self.conn.cursor()

    def insertar(self, idOlimpiada, idPais, idGenero, oro, plata, bronce):
       try:
           sql = """INSERT INTO Resultados (idOlimpiada, idPais, idGenero, oro, plata, bronce)
                    VALUES (%s, %s, %s, %s, %s, %s)"""
           valores = (idOlimpiada, idPais, idGenero, oro, plata, bronce)
           self.cursor.execute(sql, valores)
           self.conn.commit()
           print("Resultado insertado correctamente.")
           return True
       except Error as e:
           print(f"Error al insertar resultado: {e}")
           return False


    def editar(self, idOlimpiada, idPais, idGenero, oro, plata, bronce):
       if oro < 0 or plata < 0 or bronce < 0:
           print("Error: Las medallas deben ser valores enteros positivos.")
           return False


       try:
           sql = """UPDATE Resultados
                    SET oro = %s, plata = %s, bronce = %s
                    WHERE idOlimpiada = %s AND idPais = %s AND idGenero = %s"""
           valores = (oro, plata, bronce, idOlimpiada, idPais, idGenero)
           self.cursor.execute(sql, valores)
           self.conn.commit()


           if self.cursor.rowcount > 0:
               print("Resultado actualizado correctamente.")
               return True
           else:
               print("No se encontró el resultado para actualizar.")
               return False
       except Error as e:
           print(f"Error al editar resultado: {e}")
           return False


    def eliminar(self, idOlimpiada, idPais, idGenero):
       try:
           sql = """DELETE FROM Resultados WHERE idOlimpiada = %s AND idPais = %s AND idGenero = %s"""
           valores = (idOlimpiada, idPais, idGenero)
           self.cursor.execute(sql, valores)
           self.conn.commit()
           if self.cursor.rowcount > 0:
               print("Resultado eliminado correctamente.")
               return True
           else:
               print("No se encontró el resultado para eliminar.")
               return False
       except Error as e:
           print(f"Error al eliminar resultado: {e}")
           return False


    def consultar(self, filtro):
       try:
           sql = f"SELECT * FROM Resultados WHERE {filtro}"
           self.cursor.execute(sql)
           resultados = self.cursor.fetchall()
           return resultados
       except Error as e:
           print(f"Error al consultar resultados: {e}")
           return []


    def desconectar(self):
       if self.conn:
           self.cursor.close()
           self.conn.close()
           print("Conexion cerrada correctamente")

if __name__ == "__main__":
    db = ResultadosMySQL("localhost", "root", "Carro1406M.", "olimpiadas")
    db.insertar(1, 1, 1, 2, 1, 3)
    db.editar(1, 1, 1, 3, 2, 4)
    resultados = db.consultar("idPais = 1 AND oro > 0")
    print("Consulta:", resultados)
    db.eliminar(1, 1, 1)
    db.desconectar()

