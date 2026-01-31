import unittest
from principal import Direccion,Cliente,GestorDB
from conexiones_db import conexion

class TestInfraestructura (unittest.TestCase):
    def test_conexion_db_mysql (self):
        db_prueba=conexion()
        conn=db_prueba.conectar()
        self.assertIsNotNone(conn)

class TestDIrecciones(unittest.TestCase):
    def test_Guardar_Direcciones(self):
        gestor=GestorDB()
        dir_prueba= Direccion("Calle Cliente", "1234", "Zona Norte")
        gestor.guardar_direccion(dir_prueba)
        self.assertIsNotNone(dir_prueba.direccion_id)
        

class TestClientes(unittest.TestCase):
    def test_Guardar_Clientes(self):
        gestor=GestorDB()
        dir_aux = Direccion("Calle Cliente", "1234", "Zona Norte")
        gestor.guardar_direccion(dir_aux)
        cliente_prueba=Cliente("Juan", "Perez", "1990-01-01", "123456", dir_aux)
        gestor.guardar_cliente(cliente_prueba)
        self.assertIsNotNone(cliente_prueba.cliente_id)
if __name__=="__main__":
    unittest.main()