from modules.provider_services import ProviderServices

class AddProviderMenu:
    def __init__(self):
        self.service = ProviderServices()
        self.name = None
        self.phone = None
        self.email = None
        self.address = None

    def get_target(self):
        self.name = input("Ingrese el nombre del proveedor: ")
        self.phone = input("Ingrese el teléfono del proveedor: ")
        self.email = input("Ingrese el email del proveedor: ")
        self.address = input("Ingrese la dirección del proveedor: ")
        if not self.address or not self.name or not self.email or not self.phone:
             raise ValueError("Datos inválidos.")
        
    def tryAddProvider(self):
        try:
            self.service.addProvider({
                "name": self.name,
                "phone": self.phone,
                "email": self.email,
                "address": self.address,
            })
            print(f"Contacto crado correctamente.")
        except Exception as e:
            print(f"Error al intentar agregar un nuevo contacto: {e}")