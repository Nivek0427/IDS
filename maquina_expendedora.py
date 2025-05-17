"""programa que simula una maquina expendedora de productos"""

productos = ["Lay's", "Doritos", "choclitos", "cheetoss", "mani", "mani moto","mani con pasas", "mani mixto","gala",
             "chocorramo","gansito","brwoni","pepsi","manzana","colombiana","uva"]
precios = [1000, 1500, 500, 900, 500, 700, 600, 800, 1000, 1800, 900, 2500, 1500, 1500, 1500, 1500]

cantidades = [5,5,5,5,
              5,5,5,5,
              5,5,5,5,
              5,5,5,4]

def mostrar_menu():
    #función que muestra el menú de la maquina expendedora
    
    print("------------ Bienvenido a la máquina expendedora ----------")
    print("Seleccione una opción:")
    print("1. comprar producto")
    print("2. inventario")
    print("3. informes")
    print("4. configuración")
    print("0. salir")
    
def comprar_producto():
    #función que permite comprar un producto
    
    print("Productos disponibles:")
    for i, producto in enumerate(productos):
        print(f"{i + 1}. {producto} - ${precios[i]} (Cantidad: {cantidades[i]})")
    
    while True:
        try:
            opcion = int(input("Seleccione el número del producto que desea comprar (0 para cancelar): "))
            if opcion == 0:
                print("Compra cancelada.")
                return
            elif 1 <= opcion <= len(productos):
                if cantidades[opcion - 1] > 0:
                    cantidades[opcion - 1] -= 1
                    print(f"Ha comprado un(a) {productos[opcion - 1]}.")
                else:
                    print(f"Lo siento, {productos[opcion - 1]} no está disponible.")
            else:
                print("Opción no válida. Intente nuevamente.")
        except ValueError:
            print("Por favor, ingrese un número válido.")

def inventario():
    #función que muestra el inventario de la maquina expendedora
    print("Inventario:")
    i = 0 #indice
    for producto in productos:
        print(f"{producto} - Cantidad: {cantidades[i]}")
        i += 1 #incrementar el indice

def modificar_inventario():
    #función que permite cambiar las cantidades de los productos
    print("Cambiar cantidades:")
    for i, producto in enumerate(productos):
        while True:
            try:
                nueva_cantidad = int(input(f"Ingrese la nueva cantidad para {producto} (actual: {cantidades[i]}): "))
                cantidades[i] = nueva_cantidad
                print(f"Cantidad de {producto} cambiada a {nueva_cantidad}.")
                break
            except ValueError:
                print("Por favor, ingrese un número válido.")
                
def agregar_productos():
    #función que permite agregar productos al inventario
    print("Agregar productos:")
    while True:
        producto = input("Ingrese el nombre del nuevo producto (0 para cancelar): ")
        if producto == '0':
            print("Agregando productos cancelado.")
            return
        try:
            precio = float(input(f"Ingrese el precio para {producto}: "))
            cantidad = int(input(f"Ingrese la cantidad para {producto}: "))
            productos.append(producto)
            precios.append(precio)
            cantidades.append(cantidad)
            print(f"Producto {producto} agregado con éxito.")
        except ValueError:
            print("Por favor, ingrese valores válidos.")
            
def eliminar_productos():
    #función que permite eliminar productos del inventario
    print("Eliminar productos:")
    while True:
        producto = input("Ingrese el nombre del producto a eliminar (0 para cancelar): ")
        if producto == '0':
            print("Eliminando productos cancelado.")
            return
        if producto in productos:
            index = productos.index(producto)
            productos.pop(index)
            precios.pop(index)
            cantidades.pop(index)
            print(f"Producto {producto} eliminado con éxito.")
        else:
            print(f"Producto {producto} no encontrado en el inventario.")
            
def funciones_inventario():
    #función con las opciones del inventario
    #mostrar submenú inventario
    print("------------ Submenú Inventario ----------")
    print("Seleccione una opción:")
    print("1. mostrar inventario actual")
    print("2. modificar inventario")
    print("3. agregar productos")
    print("4. eliminar productos")
    print("0. volver al menú principal")
    
    while True:
        try:
            opcion = int(input("Seleccione una opción (0 para cancelar): "))
            if opcion == 0:
                print("Inventario cancelado.")
                return
            elif opcion == 1:
                inventario()
            elif opcion == 2:
                modificar_inventario()
            elif opcion == 3:
                agregar_productos()
            elif opcion == 4:
                eliminar_productos()
            else:
                print("Opción no válida. Intente nuevamente.")
        except ValueError:
            print("Por favor, ingrese un número válido.")
    
def informe_ganancias():
    #función que muestra los informes de ganancias
    print("Informe de ganancias:")
    total_ganancias = sum(precios[i] * (cantidades[i] - cantidades[i]) for i in range(len(productos)))
    print(f"Total de ganancias: ${total_ganancias}")
    
def informe_ventas():
    #función que muestra los informes de ventas
    print("Informe de ventas:")
    total_ventas = sum(precios[i] * (cantidades[i] - cantidades[i]) for i in range(len(productos)))
    print(f"Total de ventas: ${total_ventas}")
    
def funciones_informes():
    #funcion con las opciones de informes
    print("------------ Submenú Informes ----------")
    print("Seleccione una opción:")
    print("1. mostrar informes de ganancias")
    print("2. mostrar informes de ventas")
    print("0. volver al menú principal")
    
    while True:
        try:
            opcion = int(input("Seleccione una opción (0 para cancelar): "))
            if opcion == 0:
                print("Informes cancelado.")
                return
            elif opcion == 1:
                print("Mostrando informes de ganancias...")
                informe_ganancias()
            elif opcion == 2:
                print("Mostrando informes de ventas...")
                informe_ventas()
            else:
                print("Opción no válida. Intente nuevamente.")
        except ValueError:
            print("Por favor, ingrese un número válido.") 

def restaurar_fabricar():
    #función que restaura los valores de fábrica
    global productos, precios, cantidades
    
    productos = ["Lay's", "Doritos", "choclitos", "cheetoss", "mani", "mani moto","mani con pasas", "mani mixto","gala",
                 "chocorramo","gansito","brwoni","pepsi","manzana","colombiana","uva"]
    precios = [1000, 1500, 500, 900, 500, 700, 600, 800, 1000, 1800, 900, 2500, 1500, 1500, 1500, 1500]
    cantidades = [5,5,5,5,
                    5,5,5,5,
                    5,5,5,5,
                    5,5,5,4]
    print("Valores restaurados a los valores de fábrica.")
    
def configuracion():
    #función que permite cambiar la configuración de la máquina expendedora
    print("------------ Submenú Configuración ----------")
    print("Seleccione una opción:")
    print("1. restaurar valores de fábrica")
    print("0. volver al menú principal")
    
    while True:
        try:
            opcion = int(input("Seleccione una opción (0 para cancelar): "))
            if opcion == 0:
                print("Configuración cancelada.")
                return
            elif opcion == 1:
                restaurar_fabricar()
            else:
                print("Opción no válida. Intente nuevamente.")
        except ValueError:
            print("Por favor, ingrese un número válido.")                   
            
def main():
    #función principal que ejecuta el programa
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (0 para salir): ")
        
        if opcion == '0':
            print("¡Gracias por usar la máquina expendedora!")
            break
        elif opcion == '1':
            comprar_producto()
        elif opcion == '2':
            funciones_inventario()
        elif opcion == '3':
            funciones_informes()
        elif opcion == '4':
            configuracion()
        else:
            print("Opción no válida. Intente nuevamente.")
            
if __name__ == "__main__":
    main()
# Ejecutar el programa
# main()
