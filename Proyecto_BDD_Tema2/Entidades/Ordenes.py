from Conexion import BaseDeDatos
from mysql.connector import IntegrityError
from Entidades.Clientes import Cliente
from Entidades.Producto import Producto
import datetime

class Ordenes:
    def __init__(self, db: BaseDeDatos):
        self.db = db

    def ver_ordenes_totales(self):
        try:
            query = "SELECT * FROM Ordenes"
            resultados = self.db.obtener_datos(query)
            print("ID Orden | ID Producto | ID Cliente | Fecha | Cantidad Unidades")
            for resultado in resultados:
                print(f"{resultado[0]}, {resultado[1]}, {resultado[2]}, {resultado[3]}, {resultado[4]}")
            
        except Exception as e:
            print("Error al ver las ordenes", e)

    def ver_ordenes_por_cliente(self, id_cliente):
        try:
            query = "SELECT * FROM Ordenes WHERE id_cliente = %s"
            resultados = self.db.obtener_datos(query, (id_cliente,))
            print("ID Orden | ID Producto | ID Cliente | Fecha | Cantidad Unidades")
            for resultado in resultados:
                print(f"{resultado[0]}, {resultado[1]}, {resultado[2]}, {resultado[3]}, {resultado[4]}")
            
        except Exception as e:
            print("Error al ver las ordenes por cliente", e)

    def registrar_orden(self):
        try:
            id_cliente = input("Ingrese el ID del Cliente: ")
            if not id_cliente.isdigit() or int(id_cliente) < 1:
                raise ValueError("El id del cliente debe ser un número entero positivo")
            
            id_producto = input("Ingrese el ID del Producto: ")
            if not id_producto.isdigit() or int(id_producto) < 1:
                raise ValueError("El id del producto debe ser un número entero positivo")
            
            cantidad_unidades = int(input("Ingrese la cantidad de unidades: "))
            if  cantidad_unidades < 1:
                raise ValueError("La cantidad de unidades debe ser un número entero positivo")
            
            fecha = datetime.date.today().strftime("%Y-%m-%d")

            cliente = Cliente(self.db)
            producto = Producto(self.db)
            try:
                self.db.registrar_orden(id_cliente, id_producto, cantidad_unidades)
                print("Orden registrada con éxito")
            except IntegrityError as e:
                print("Error al registrar la orden, ya existe una orden para este cliente y producto")
                return

        except Exception as e:
            print("Error al registrar la orden:", e)

    def buscar_productos_mas_vendidos(self):
        try:
            query = "SELECT Ordenes.id_producto, Productos.nombre_producto, SUM(cantidad_unidades) as total_vendidos FROM Ordenes INNER JOIN (Productos) ON Productos.id_producto = Ordenes.id_producto GROUP BY Ordenes.id_producto ORDER BY total_vendidos DESC"
            resultados = self.db.obtener_datos(query)
            print("ID Producto | Nombre | Total Vendidos")
            for resultado in resultados:
                print(f"{resultado[0]}, {resultado[1]}, {resultado[2]}")
            
        except Exception as e:
            print("Error al buscar los productos más vendidos", e)

    