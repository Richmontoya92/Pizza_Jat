MASAS_DISPONIBLES = ["Masa Tradicional", "Masa Delgada", "Masa con Bordes de Queso"]

SALSAS_DISPONIBLES = ["Salsa de Tomate", "Salsa Alfredo", "Salsa Barbecue", "Salsa Pesto"]

INGREDIENTES_DISPONIBLES = [
    "Tomate", "Champiñones", "Aceituna", "Cebolla", "Pollo",
    "Jamón", "Carne", "Tocino", "Queso"
]

TIEMPO_BASE = 20

TIEMPO_POR_INGREDIENTE = 2

PIZZA_POR_DEFECTO = {
    "masa": None,
    "salsa": None,
    "ingredientes": []
}


pizza_actual = PIZZA_POR_DEFECTO.copy()

def seleccionar_masa(pizza):
    print("\n--- Seleccionar Tipo de Masa ---")
    for i, masa in enumerate(MASAS_DISPONIBLES):
        print(f"{i + 1}. {masa}") 
    
    while True: 
        try:
            opcion = int(input(f"Seleccione una masa (1-{len(MASAS_DISPONIBLES)}): "))
            if 1 <= opcion <= len(MASAS_DISPONIBLES):
                pizza["masa"] = MASAS_DISPONIBLES[opcion - 1] 
                print(f"Masa '{pizza['masa']}' seleccionada.")
                return True
            else:
                print("Opción inválida. Por favor, ingrese un número dentro del rango.")
        except ValueError: 
            print("Entrada inválida. Por favor, ingrese un número.")

def seleccionar_salsa(pizza):
    print("\n--- Seleccionar Tipo de Salsa ---")
    for i, salsa in enumerate(SALSAS_DISPONIBLES):
        print(f"{i + 1}. {salsa}")
    
    while True:
        try:
            opcion = int(input(f"Seleccione una salsa (1-{len(SALSAS_DISPONIBLES)}): "))
            if 1 <= opcion <= len(SALSAS_DISPONIBLES):
                pizza["salsa"] = SALSAS_DISPONIBLES[opcion - 1]
                print(f"Salsa '{pizza['salsa']}' seleccionada.")
                return True
            else:
                print("Opción inválida. Por favor, ingrese un número dentro del rango.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número.")

def agregar_ingrediente(pizza):
    print("\n--- Agregar Ingrediente ---")
    print("Ingredientes disponibles:")
    for i, ingrediente in enumerate(INGREDIENTES_DISPONIBLES):
        print(f"{i + 1}. {ingrediente}")
    
    while True:
        try:
            opcion = int(input(f"Seleccione un ingrediente para agregar (1-{len(INGREDIENTES_DISPONIBLES)}): "))
            if 1 <= opcion <= len(INGREDIENTES_DISPONIBLES):
                ingrediente_a_agregar = INGREDIENTES_DISPONIBLES[opcion - 1]
                if ingrediente_a_agregar not in pizza["ingredientes"]:
                    pizza["ingredientes"].append(ingrediente_a_agregar)
                    print(f"Ingrediente '{ingrediente_a_agregar}' agregado.")
                    return True
                else:
                    print(f"El ingrediente '{ingrediente_a_agregar}' ya está en tu pizza.")
                    return False 
            else:
                print("Opción inválida. Por favor, ingrese un número dentro del rango.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número.")

def eliminar_ingrediente(pizza):
    print("\n--- Eliminar Ingrediente ---")
    if not pizza["ingredientes"]: 
        print("Tu pizza no tiene ingredientes para eliminar.")
        return False
    
    print("Ingredientes actuales en tu pizza:")
    for i, ingrediente in enumerate(pizza["ingredientes"]):
        print(f"{i + 1}. {ingrediente}")
    
    while True:
        try:
            opcion = int(input(f"Seleccione un ingrediente para eliminar (1-{len(pizza['ingredientes'])}): "))
            if 1 <= opcion <= len(pizza["ingredientes"]):
                ingrediente_a_eliminar = pizza["ingredientes"].pop(opcion - 1)
                print(f"Ingrediente '{ingrediente_a_eliminar}' eliminado.")
                return True
            else:
                print("Opción inválida. Por favor, ingrese un número dentro del rango.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número.")

def estimar_tiempo_y_confirmar(pizza):
    
    if pizza["masa"] is None or pizza["salsa"] is None:
        print("\n¡Atención! Para estimar el tiempo, debes seleccionar al menos la masa y la salsa.")
        return False
    
    tiempo_total = TIEMPO_BASE
    tiempo_total += len(pizza["ingredientes"]) * TIEMPO_POR_INGREDIENTE 
    
    print(f"\n--- Estimación de Tiempo ---")
    print(f"Tu pizza tomará aproximadamente {tiempo_total} minutos en estar lista.")
    
    while True:
        confirmar = input("¿Deseas confirmar tu orden? (si/no): ").lower()
        if confirmar == 'si':
            print("¡Orden confirmada! Tu pizza estará lista pronto.")
            return True
        elif confirmar == 'no':
            print("Orden cancelada. Puedes preparar nueva pizza ñam ñam.")
            return False
        else:
            print("Respuesta inválida. Por favor, ingresa 'si' para sí o 'no' para no.")

def mostrar_pizza_actual(pizza):
    print("\n--- Tu Pizza Actual ---")
    print(f"Masa: {pizza['masa'] if pizza['masa'] else 'No seleccionada'}")
    print(f"Salsa: {pizza['salsa'] if pizza['salsa'] else 'No seleccionada'}")
    
    if pizza["ingredientes"]:
        print("Ingredientes:")
        for ingrediente in pizza["ingredientes"]:
            print(f"  - {ingrediente}")
    else:
        print("Ingredientes: Ninguno")


if __name__ == '__main__':
   
    print("Ejecutando pizza_utils.py directamente para pruebas.")
    