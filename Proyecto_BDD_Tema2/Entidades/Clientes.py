from Conexion import BaseDeDatos
from mysql.connector import IntegrityError

class Cliente:
    def __init__(self, db: BaseDeDatos):
        self.db = db

    def registrar_cliente(self):
        nombre = input("Nombre del Cliente: ") 
        if not isinstance(nombre, str) or nombre.isspace() or nombre == "":
            raise ValueError("El nombre del cliente no puede estar vacío")
    
        apellido = input("Apellidos del Cliente: ")
        if not isinstance(apellido, str) or apellido.isspace() or apellido == "":
            raise ValueError("Los apellidos del cliente no pueden estar vacíos")
    
        direccion = input("Direccion del Cliente: ")
        if not isinstance(direccion, str) or direccion.isspace() or direccion == "":
            raise ValueError("La dirección del cliente no puede estar vacía")
        
        query = "INSERT INTO Clientes (nombre_cliente, apellido_cliente, direccion) VALUES (%s, %s, %s)"
        values = (nombre, apellido, direccion)
        self.db.ejecutar(query, values)
        print("Cliente registrado correctamente")

    def ver_clientes(self):
        try:
            query = "SELECT * FROM Clientes"
            resultados = self.db.obtener_datos(query)
            print("id_cliente | nombre_cliente | apellido_cliente | direccion")
            for resultado in resultados:
                print(f"{resultado[0]}, {resultado[1]}, {resultado[2]}, {resultado[3]}")
            
        except Exception as e:
            print("Error al ver los clientes", e)

    def editar_cliente(self, id_cliente):
        query_select = "SELECT * FROM Clientes WHERE id_cliente = %s"
        resultado = self.db.obtener_datos(query_select, (id_cliente,))
        if resultado == []:
            print("El cliente con ese id no existe")
            return
        try:
            nombre = input("Nuevo nombre del cliente: ")
            if not isinstance(nombre, str) or nombre.isspace() or nombre == "":
                raise ValueError("Ingrese un nombre válido")
        
            apellido = input("Nuevos apellidos del cliente: ")
            if not isinstance(apellido, str) or apellido.isspace() or apellido == "":
                raise ValueError("Ingrese un apellido válido")
        
            direccion = input("Nueva dirección del cliente: ")
            if not isinstance(direccion, str) or direccion.isspace() or direccion == "":
                raise ValueError("Ingrese una dirección válida")


            query = "UPDATE Clientes SET nombre_cliente=%s, apellido_cliente=%s, direccion=%s WHERE id_cliente = %s"
            valores = (nombre, apellido, direccion, id_cliente)
            self.db.ejecutar(query, valores)
            print("Cliente editado correctamente")
        except Exception as e:
            print("Error al editar el cliente:", e)

    def eliminar_cliente(self, id_cliente):
        try:
            query_select = "SELECT * FROM Clientes WHERE id_cliente = %s"
            resultado = self.db.obtener_datos(query_select, (id_cliente,))
            if resultado:
                query = "DELETE FROM Clientes WHERE id_cliente = %s"
                self.db.ejecutar(query, (id_cliente,))
                print("Cliente eliminado con exito")
            else:
                print("El cliente con ese id no existe")
        except IntegrityError as e:
            print("No se puede eliminar el cliente porque dependencias en otras tablas")
        except Exception as e:
            print(f"Error al eliminar el cliente: {e}")

    def buscar_cliente_por_id(self, id_cliente: int) -> bool:
        try:
            query = "SELECT * FROM Clientes WHERE id_cliente = %s"
            resultado = self.db.obtener_datos(query, (id_cliente,))
            if resultado:
                print("ID Cliente | Nombre Cliente | Apellido Cliente | Dirección")
                print(f"{resultado[0][0]}, {resultado[0][1]}, {resultado[0][2]}, {resultado[0][3]}")
                return True
            else:
                print("El cliente con ese id no existe")
                return False

        except Exception as e:
            print("Error al buscar el cliente", e)