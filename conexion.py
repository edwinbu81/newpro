import mysql.connector
from mysql.connector import Error

class DAO:
    def _init_(self):
        try:
            self.conexion = mysql.connector.connect(
                host='localhost',
                port=3306,
                user='root',
                password='',
                db='biblioteca'
            )
        except Error as ex:
            print("Error al intentar la conexión: {0}".format(ex))

    def listarCursos(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("SELECT * FROM curso ORDER BY id ASC")
                resultados = cursor.fetchall()
                return resultados
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))
                
    def registrarCurso(self, curso):  
        if self.conexion.is_connected():
            try:
                cursor= self.conexion.cursor()
                sql= "INSERT INTO curso (codigo, nombre, creditos) VALUES ('{0}','{1}',{2})"
                cursor.execute (sql.format(curso[0],curso[1], curso [2]))
                self.conexion.comit()
                print("Curso Registrado\n")
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))
                
    def eliminarCurso(self, codigoCursoEliminar):
         if self.conexion.is_connected():
            try:
                cursor= self.conexion.cursor()
                sql= "DELETE FROM curso where codigo= '{0}'"
                cursor.execute (sql.format(codigoCursoEliminar))
                self.conexion.comit()
                print("Curso Registrado\n")
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))
