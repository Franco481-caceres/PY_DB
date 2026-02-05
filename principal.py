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
    
class Auto:
    def __init__ (self,patente,chasis_id,motor_id,marca,modelo,tipo,color,cliente:Cliente):
        self.patente=patente
        self.chasis_id=chasis_id
        self.motor_id=motor_id
        self.marca=marca
        self.modelo=modelo
        self.tipo=tipo
        self.color=color
        self.cliente_id=cliente.cliente_id


class GestorDB:
    def __init__(self):
        self.db=conexion()
    #Metodos relacionados a las DIRECCIONES

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
    """"Lo que hace el metodo leer direccion es devolver una tupla y mediante indice le indico al objeto que columna de la tabla
    va en cada atributo.
    primero en el constructor le paso indicie 1,2,3 y despues de la creacion le paso el id mediante objeto.direccion_id=tupla[0]"""
    def leer_direccion(self,direccion_solicitada):
        conexion_tabla=self.db.conectar()
        cursor=conexion_tabla.cursor()
        sql="Select * From direcciones where direccion_id=%s"
        
        cursor.execute(sql,(direccion_solicitada,))
        direccion_db=cursor.fetchone()
        
        print(f"SU direccion {direccion_db}")
        cursor.close()
        self.db.desconectar()
        return direccion_db
    
    
    # Metodos relacionados a los CLIENTES

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

    def leer_cliente(self,cliente_solicitado):
        conexion_tabla=self.db.conectar()
        cursor=conexion_tabla.cursor()
        sql="Select * from clientes where cliente_id = %s"
        valores=(cliente_solicitado,)
        cursor.execute(sql,valores)
        cliente_db=cursor.fetchone()
        print(f"Su cliente es : {cliente_db}")
        cursor.close()
        self.db.desconectar()
        return cliente_db
    
        #METODOS RELACIONADOS AL AUTO  
    def guardar_auto(self,auto_nuevo:Auto):
        conexion_tabla=self.db.conectar()
        cursor=conexion_tabla.cursor()
        sql="Insert into autos (patente,chasis_id,motor_id,marca,modelo,tipo,color,cliente_id) values (%s,%s,%s,%s,%s,%s,%s,%s)"
        valores=(auto_nuevo.patente,auto_nuevo.chasis_id,auto_nuevo.motor_id,auto_nuevo.marca,auto_nuevo.modelo,auto_nuevo.tipo,auto_nuevo.color,auto_nuevo.cliente_id) 
        cursor.execute(sql,valores)
        conexion_tabla.commit()
        return f"se agrego con exito el auto en la base de datos"