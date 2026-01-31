from conexiones_db import conexion

class Direccion:
    def __init__(self,calle,cp,municipio):
        self.direccion_id=None
        self.calle=calle
        self.cp=cp
        self.municipio=municipio
        

class Cliente:
    def __init__ (self,nombre,apellido,fecha_nacimiento,nro_licencia,direccion:Direccion):
        self.cliente_id=None
        self.nombre=nombre
        self.apellido=apellido
        self.fecha_nacimiento=fecha_nacimiento
        self.nro_licencia=nro_licencia
        self.direccion_id=direccion.direccion_id


class GestorDB:
    def __init__(self):
        self.db=conexion()
    
    
    def guardar_direccion(self,direccion_nueva:Direccion):
        conn=self.db.conectar()
        cursor=conn.cursor()
        sql="INSERT INTO direcciones(calle,cp,municipio) VALUES (%s,%s,%s)"
        valores=(direccion_nueva.calle,direccion_nueva.cp,direccion_nueva.municipio)
        cursor.execute(sql,valores)
        conn.commit()
        nuevo_id=cursor.lastrowid
        direccion_nueva.direccion_id=nuevo_id
        print(f"Nueva direccion creada su id es {nuevo_id}")
        cursor.close()
        self.db.desconectar()
    
    def guardar_cliente(self,cliente_nuevo:Cliente):
        conexion_tabla=self.db.conectar()
        cursor=conexion_tabla.cursor()
        sql="Insert into clientes (nombre,apellido,fecha_nacimiento,nro_licencia,direccion_id)VALUES(%s,%s,%s,%s,%s)"
        valores=(cliente_nuevo.nombre,cliente_nuevo.apellido,cliente_nuevo.fecha_nacimiento,cliente_nuevo.nro_licencia,cliente_nuevo.direccion_id)
        cursor.execute(sql,valores)
        conexion_tabla.commit()
        nuevo_id_cliente=cursor.lastrowid
        cliente_nuevo.cliente_id=nuevo_id_cliente
        print(f"Se agrego el cliente a la base de datos, su id es: {cliente_nuevo.cliente_id}")
        cursor.close()
        self.db.desconectar()


    