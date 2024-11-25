from Conexion import BaseDeDatos 
from Entidades.Producto import Producto
from Menu import MenuVentas


def main():
    MenuVentas(db)

if __name__ == "__main__":
    db = BaseDeDatos("localhost", 3306, "root", "123456", "VentasOnline")
    db.conectar()
    menu_ventas = MenuVentas(db)
    menu_ventas.mostrar_menu()