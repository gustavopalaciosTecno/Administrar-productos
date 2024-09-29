from db_manager import DBManager
from productos import Producto

def mostrar_menu():
    print("\n1. Agregar producto")
    print("2. Listar productos")
    print("3. Actualizar precio")
    print("4. Eliminar producto")
    print("5. Salir")

def agregar_producto(db):
    try:
        id_producto = int(input("ID del producto: "))
        nombre = input("Nombre del producto: ")
        tipo = input("Tipo de producto: ")
        precio = float(input("Precio del producto: "))
        nuevo_producto = Producto(id_producto, nombre, tipo, precio)
        db.agregar_producto(nuevo_producto)
    except ValueError:
        print("Error: Entrada inválida.")

def listar_productos(db):
    productos = db.listar_productos()
    if productos:
        for producto in productos:
            print(producto)
    else:
        print("No hay productos disponibles.")

def actualizar_precio(db):
    try:
        id_producto = int(input("ID del producto a actualizar: "))
        nuevo_precio = float(input("Nuevo precio: "))
        db.actualizar_precio_producto(id_producto, nuevo_precio)
    except ValueError:
        print("Error: Entrada inválida.")

def eliminar_producto(db):
    try:
        id_producto = int(input("ID del producto a eliminar: "))
        db.eliminar_producto(id_producto)
    except ValueError:
        print("Error: Entrada inválida.")

def main():
    db = DBManager()

    while True:
        mostrar_menu()
        opcion = input("\nSelecciona una opción: ")

        if opcion == '1':
            agregar_producto(db)
        elif opcion == '2':
            listar_productos(db)
        elif opcion == '3':
            actualizar_precio(db)
        elif opcion == '4':
            eliminar_producto(db)
        elif opcion == '5':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
