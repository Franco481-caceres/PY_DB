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
    
    def test_Leer_Direcciones(self):
        gestor=GestorDB()
        dir_prueba= Direccion("Calle Cliente", "1234", "Zona Norte")
        gestor.guardar_direccion(dir_prueba)

        """Aca deberia ir un input"""
        direccion_solicitada= dir_prueba.direccion_id
        direccion_devuelta=gestor.leer_direccion(direccion_solicitada)
        direccion_devuelta_objeto=Direccion(direccion_devuelta[1],direccion_devuelta[2],direccion_devuelta[3],)
        direccion_devuelta_objeto.direccion_id=direccion_devuelta[0]
        self.assertEqual(direccion_devuelta_objeto.direccion_id, direccion_solicitada)
        self.assertEqual(direccion_devuelta_objeto.calle, dir_prueba.calle)
        self.assertEqual(direccion_devuelta_objeto.cp, dir_prueba.cp)
        self.assertEqual(direccion_devuelta_objeto.municipio, dir_prueba.municipio)
        
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