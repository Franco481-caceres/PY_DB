import unittest
from principal import Auto,Direccion,Cliente,GestorDB
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

    def test_Leer_Clientes(self):
        gestor=GestorDB()
        dir_aux= Direccion("Calle Cliente", "1234", "Zona Norte")
        gestor.guardar_direccion(dir_aux)
        Cliente_prueba=Cliente("Juan", "Perez", "1990-01-01", "123456", dir_aux)
        gestor.guardar_cliente(Cliente_prueba)
        Cliente_solicitado=Cliente_prueba.cliente_id
        cliente_devuelto=gestor.leer_cliente(Cliente_solicitado)
        direccion_recuperada=gestor.leer_direccion(cliente_devuelto[5])
        direccion_recuperada_aux=Direccion(direccion_recuperada[1],direccion_recuperada[2],direccion_recuperada[3])
        direccion_recuperada_aux.direccion_id=direccion_recuperada[0]
        cliente_objeto=Cliente(cliente_devuelto[1],cliente_devuelto[2],cliente_devuelto[3],cliente_devuelto[4],direccion_recuperada_aux)
        cliente_objeto.cliente_id=cliente_devuelto[0]    
        self.assertIsNotNone(cliente_objeto.cliente_id)
        self.assertEqual(Cliente_prueba.nombre,cliente_objeto.nombre)
        self.assertEqual(Cliente_prueba.direccion_id,cliente_objeto.direccion_id)
        self.assertEqual(cliente_objeto.direccion_id,dir_aux.direccion_id)


class TestAutos(unittest.TestCase):
    def test_Guardar_Autos(self):
        gestor=GestorDB()
        dir_aux= Direccion("Calle Cliente", "1234", "Zona Norte")
        gestor.guardar_direccion(dir_aux)
        cliente_aux=Cliente("Juan", "Perez", "1990-01-01", "123456", dir_aux)
        gestor.guardar_cliente(cliente_aux)
        Auto_prueba=Auto("AF123JK","9BWZZZ3112","EA888","Volkswagen","Golf","Hatchback","Gris Carbono",cliente_aux)
        gestor.guardar_auto(Auto_prueba)
        self.assertEqual(Auto_prueba.cliente_id,cliente_aux.cliente_id)
        self.assertEqual(Auto_prueba.patente,"AF123JK")

if __name__=="__main__":
    unittest.main()