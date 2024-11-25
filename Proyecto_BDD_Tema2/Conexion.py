import mysql.connector

class BaseDeDatos:
    def __init__(self, host, port, user, password, database):
        self.config = {
            "host": host,
            "port": port,
            "user": user,
            "password": password,
            "database": database
        }
        self.conexion = None
        self.cursor = None

    def conectar(self):
        try:
            self.conexion = mysql.connector.connect(**self.config)
            self.cursor = self.conexion.cursor()
            print("Conectado a la base de datos")
        except mysql.connector.Error as error:
            print(f"Error al conectar a la base de datos: {error}")

    def desconectar(self):
        if self.cursor:
            self.cursor.close()
        if self.conexion:
            self.conexion.close()
    
    def ejecutar(self, query, valores=None):
        self.cursor.execute(query, valores or ())
        self.conexion.commit()

    def obtener_datos(self, query, valores=None):
        self.cursor.execute(query, valores or ())
        return self.cursor.fetchall()
    
    def registrar_orden(self, id_cliente, id_producto, cantidad):
        try:
            stock_actual = self.verificar_stock(id_producto)
            if stock_actual is None:
                print("No hay stock del producto")
                return
            
            if cantidad > stock_actual:
                print("No hay stock suficiente para la cantidad solicitada")
                return
            
            self.cursor.callproc('RegistrarOrden', [id_cliente, id_producto, cantidad])
            self.conexion.commit()
        except mysql.connector.Error as error:
            print(f"Error al registrar la orden: {error}")
        except Exception as e:
            print(f"Error inesperado: {e}")
        
    def verificar_stock(self, id_producto):
        query = "SELECT cantidad_stock FROM Productos WHERE id_producto = %s"
        resultado = self.obtener_datos(query, (id_producto,))
        if resultado == []:
            return None
        return resultado[0][0]