class GenericMenu():
    def __init__(self):
        super().__init__()

    def print_generic_menu(self):
        print("Seleccione una opción:")
        print("1. Ingreso de nuevo contacto")
        print("2. Mostrar todos los contactos")
        print("3. Encontrar contacto por aproximación en el nombre")
        print("4. Salir")
    
    def get_option(self):
        valid_option = False
        while not valid_option:
            try:
                option = int(input("\nIngrese el número de la opción: "))
                if option in [1,2,3,4]:
                    valid_option = True
                else:
                    print("Opción inválida. Por favor, seleccione una opción válida.")
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número válido.")
        return option
    
    def print_continue_process(self):
        control = input("Presione enter si desea continuar con un nuevo proceso de lo contrario escriba exit: ")
        if control == "":
            return "continue"
        elif control == "exit":
            return "exit"
        else: 
            return "invalid"