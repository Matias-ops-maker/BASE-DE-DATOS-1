from Conexion import BaseDeDatos
from mysql.connector import IntegrityError

class Producto:
    def __init__(self, db: BaseDeDatos):
        self.db = db

    def obtener_id_categorias(self):
        query = "SELECT id_categoria FROM Categorias"
        resultados = self.db.obtener_datos(query)
        return [result[0] for result in resultados]

    def registrar_producto(self):
        try:

            categorias_validas = self.obtener_id_categorias()

            nombre_producto = input("Nombre del Producto: ")
            if not isinstance(nombre_producto, str) or nombre_producto.isspace() or nombre_producto == "":
                raise ValueError("Ingrese un nombre válido")                
            
            precio = float(input("Precio del Producto: "))
            if not isinstance(precio, (int, float)) or precio <= 0:
                raise ValueError("El precio debe ser un número positivo")               
            
            id_categoria = int(input("ID categoría: "))
            if id_categoria not in categorias_validas:
                raise ValueError(f"El id de categoria no se encuentra entre las categorias válidas: {categorias_validas}")
            
            cantidad_stock = int(input("Cantidad en stock: "))
            if not isinstance(cantidad_stock, int) or cantidad_stock < 0:
                raise ValueError("La cantidad de stock debe ser un número positivo")
            
            query = "INSERT INTO Productos (nombre_producto, precio, id_categoria, cantidad_stock) VALUES (%s, %s, %s, %s)"
            valores = (nombre_producto, precio, id_categoria, cantidad_stock)
            self.db.ejecutar(query, valores)

            print("Producto registrado con exito")
        except Exception as e:
            print(f"Error al registrar el producto: {e}")
        
    def eliminar_producto(self, id_producto):
        query_select = "SELECT * FROM Productos WHERE id_producto = %s"
        resultado = self.db.obtener_datos(query_select, (id_producto,))
        if resultado == []:
            print("El producto con ese id no existe")
            return
        try:
            query = "DELETE FROM Productos WHERE id_producto = %s"
            self.db.ejecutar(query, (id_producto,))

            print("Producto eliminado con exito")
        except IntegrityError as e:
            print("No se puede eliminar el producto porque está asociado a una venta")
        except Exception as e:
            print(f"Error al eliminar el producto: {e}")
        
    def ver_productos(self):
        try:
            query = "SELECT * FROM Productos"
            resultados = self.db.obtener_datos(query)
            print("ID Producto | Nombre Producto | Precio | ID Categoria | Cantidad Stock")
            for resultado in resultados:
                print(f"{resultado[0]}, {resultado[1]}, {resultado[2]}, {resultado[3]}, {resultado[4]}")
        except Exception as e:
            print(f"Error al ver los productos: {e}")

    def editar_producto(self, id_producto):

        categorias_validas = self.obtener_id_categorias()

        query_select = "SELECT * FROM Productos WHERE id_producto = %s"
        resultado = self.db.obtener_datos(query_select, (id_producto,))
        if resultado == []:
            print("El producto con ese id no existe")
            return
        try:
            nombre_producto = input("Nuevo nombre del producto: ")
            if not isinstance(nombre_producto, str) or nombre_producto.isspace() or nombre_producto == "":
                raise ValueError("Ingrese un nombre válido")
            
            precio = float(input("Nuevo precio del producto: "))
            if not isinstance(precio, (int, float)) or precio <= 0:
                raise ValueError("El precio debe ser un número positivo")
            
            id_categoria = int(input("Nuevo ID categoría: "))
            if id_categoria not in categorias_validas:
                raise ValueError(f"El id de categoria no se encuentra entre las categorias válidas: {categorias_validas}")
            
            cantidad_stock = int(input("Nueva cantidad en stock: "))
            if not isinstance(cantidad_stock, int) or cantidad_stock < 0:
                raise ValueError("La cantidad de stock debe ser un número positivo")
            
            query = "UPDATE Productos SET nombre_producto=%s, precio=%s, id_categoria=%s, cantidad_stock=%s WHERE id_producto=%s"
            valores = (nombre_producto, precio, id_categoria, cantidad_stock, id_producto)
            self.db.ejecutar(query, valores)

            print("Producto actualizado con exito")
        except Exception as e:
            print(f"Error al editar el producto: {e}")


    def buscar_producto_por_nombre(self, nombre_producto):
        try:
            query = "SELECT * FROM Productos WHERE nombre_producto LIKE %s"
            patron = f"%{nombre_producto}%"
            resultados = self.db.obtener_datos(query, (patron,))
            if resultados == []:
                print("El producto no se encuentra en la base de datos")
                return
            print("ID Producto | Nombre Producto | Precio | ID Categoria | Cantidad Stock")
            for resultado in resultados:
                print(f"{resultado[0]}, {resultado[1]}, {resultado[2]}, {resultado[3]}, {resultado[4]}")
        except Exception as e:
            print(f"Error al buscar el producto: {e}")

    def buscar_producto_por_id(self, id_producto):
        try:
            query = "SELECT * FROM Productos WHERE id_producto = %s"
            resultado = self.db.obtener_datos(query, (id_producto,))
            if resultado == []:
                print("El producto con ese id no existe")
                return
            print("ID Producto | Nombre Producto | Precio | ID Categoria | Cantidad Stock")
            for resultado in resultado:
                print(f"{resultado[0]}, {resultado[1]}, {resultado[2]}, {resultado[3]}, {resultado[4]}")
        except Exception as e:
            print(f"Error al buscar el producto: {e}")

    
    def ver_categorias(self):
        try:
            query = "SELECT * FROM Categorias"
            resultados = self.db.obtener_datos(query)
            print("ID Categoria | Nombre Categoria")
            for resultado in resultados:
                print(f"{resultado[0]}, {resultado[1]}")
        except Exception as e:
            print(f"Error al ver las categorías: {e}")