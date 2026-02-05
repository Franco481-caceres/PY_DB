import mysql.connector

class conexion:
    def __init__(self):
        self.conexion= None
        self.cursor=None
        self.host="localhost"
        self.user="root"
        self.password="Pilates28"
        self.database="seguros"
    def conectar(self):
        try:
            self.conexion = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            if self.conexion.is_connected():
               return self.conexion
        except mysql.connector.Error as fallo:
            print (f"Error de conexion {fallo}")
            return None

    def desconectar (self):        
        if  self.conexion and self.conexion.is_connected():
            self.conexion.close()