#pequeña base de datos
productos = []
ventas = []

# Funcion para registrar productos
def registrar_producto():
    print("\n--- REGISTRAR PRODUCTO ---")

    codigo = input("Ingrese codigo: ")
    nombre = input("Ingrese nombre: ")

    try:
        precio = float(input("Ingrese precio: "))
        stock = int(input("Ingrese stock: "))

        if precio <= 0 or stock < 0:
            print("El precio debe ser positivo y el stock no negativo.")
            return

        # Verificar si el codigo ya existe
        for producto in productos:
            if producto["codigo"] == codigo:
                print("El codigo ya esta registrado.")
                return

        producto = {
            "codigo": codigo,
            "nombre": nombre,
            "precio": precio,
            "stock": stock
        }

        productos.append(producto)
        print("Producto registrado correctamente.")

    except ValueError:
        print("Error: ingrese valores numericos validos.")


# Funcion para mostrar productos
def mostrar_productos():
    print("\n--- LISTA DE PRODUCTOS ---")

    if not productos:
        print("No hay productos registrados.")
        return

    for producto in productos:
        print("--------------------------------")
        print("Codigo:", producto["codigo"])
        print("Nombre:", producto["nombre"])
        print("Precio: S/", producto["precio"])
        print("Stock:", producto["stock"])


# Funcion para buscar productos
def buscar_producto():
    print("\n--- BUSCAR PRODUCTO ---")

    codigo = input("Ingrese el codigo del producto: ")

    for producto in productos:
        if producto["codigo"] == codigo:
            print("Producto encontrado:")
            print("Nombre:", producto["nombre"])
            print("Precio: S/", producto["precio"])
            print("Stock:", producto["stock"])
            return

    print("Producto no encontrado.")


# Funcion para registrar ventas
def registrar_venta():
    print("\n--- REGISTRAR VENTA ---")

    codigo = input("Ingrese codigo del producto: ")

    for producto in productos:
        if producto["codigo"] == codigo:

            try:
                cantidad = int(input("Ingrese cantidad: "))

                if cantidad <= 0:
                    print("La cantidad debe ser mayor que cero.")
                    return

                if cantidad > producto["stock"]:
                    print("Stock insuficiente.")
                    return

                total = producto["precio"] * cantidad

                producto["stock"] -= cantidad
                ventas.append({
                    "producto": producto["nombre"],
                    "cantidad": cantidad,
                    "total": total
                })

                print("\nVenta registrada correctamente.")
                print("Producto:", producto["nombre"])
                print("Cantidad:", cantidad)
                print("Total: S/", round(total, 2))
                return

            except ValueError:
                print("Ingrese una cantidad numerica valida.")
                return

    print("Producto no encontrado.")


# Funcion para mostrar ventas
def mostrar_ventas():
    print("\n--- HISTORIAL DE VENTAS ---")

    if not ventas:
        print("No existen ventas registradas.")
        return

    total_general = 0

    for venta in ventas:
        print("--------------------------------")
        print("Producto:", venta["producto"])
        print("Cantidad:", venta["cantidad"])
        print("Total: S/", round(venta["total"], 2))

        total_general += venta["total"]

    print("--------------------------------")
    print("TOTAL DE VENTAS: S/", round(total_general, 2))


# Menu principal
def menu_principal():

    while True:
        print("\n================================")
        print(" SISTEMA DE GESTION DE VENTAS")
        print("================================")
        print("1. Registrar producto")
        print("2. Mostrar productos")
        print("3. Buscar producto")
        print("4. Registrar venta")
        print("5. Mostrar ventas")
        print("6. Salir")
        print("================================")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            registrar_producto()

        elif opcion == "2":
            mostrar_productos()

        elif opcion == "3":
            buscar_producto()

        elif opcion == "4":
            registrar_venta()

        elif opcion == "5":
            mostrar_ventas()

        elif opcion == "6":
            print("Gracias por utilizar el sistema.")
            break

        else:
            print("Opcion incorrecta. Intente nuevamente.")


# Ejecutar aplicacion
if __name__ == "__main__":
    menu_principal()

