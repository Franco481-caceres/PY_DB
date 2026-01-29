import mysql.connector

def conectar():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Pilates28",
            database="seguros"
        )
        if conexion.is_connected():
           return conexion
    except mysql.connector.Error as fallo:
        print (f"Error de conexion {fallo}")
        return None

def desconectar (conexion):
    if  conexion and conexion.is_connected():
        conexion.close()