from pizza_utils import *

def mostrar_menu():
    """Muestra el menú principal de opciones al usuario."""
    print("\n===== Menú de Personalización de Pizza =====")
    print("1. Cambiar tipo de masa")
    print("2. Cambiar tipo de salsa")
    print("3. Agregar ingrediente")
    print("4. Eliminar ingrediente")
    print("5. Mostrar mi pizza actual")
    print("6. Estimar tiempo y confirmar orden")
    print("7. Salir")
    print("============================================")

def main():
    """
    Función principal que ejecuta el programa del prototipo de Pizza JAT.
    """
    print("¡Bienvenido al prototipo de Pizza JAT!")
    

    while True:
        mostrar_menu()
        opcion = input("Ingrese su opción: ")

        if opcion == '1':
            seleccionar_masa(pizza_actual) 
        elif opcion == '2':
            seleccionar_salsa(pizza_actual) 
        elif opcion == '3':
            agregar_ingrediente(pizza_actual) 
        elif opcion == '4':
            eliminar_ingrediente(pizza_actual)  
        elif opcion == '5':
            mostrar_pizza_actual(pizza_actual)  
        elif opcion == '6':
            if estimar_tiempo_y_confirmar(pizza_actual): 
                print("¡Gracias por tu pedido!")
                break 
        elif opcion == '7':
            print("¡Gracias por usar el prototipo de Pizza JAT! ¡Hasta luego!")
            break 
        else:
            print("Opción inválida. Por favor, intente de nuevo.")

if __name__ == '__main__':
    main()