from modules.provider_services import ProviderServices
from client.helpers.table import Table
from client.helpers.csv_downlaod import ExportToCsv

class FindAllProviders:
    def __init__(self):
        self.service = ProviderServices()
        self.table = Table()
        self.exportCsv = ExportToCsv()
        self.headers = ["position", "id", "name", "phone", "email", "address"]

    def getAllProviders(self):
        print("¿Desea exportar a csv la búsqueda?")
        opt = None
        filename = None
        try:
            opt = int(input("1 = Si, 2 = No: "))
            if not opt == 1 and not opt == 2:
                print("\nDebe seleccionar opcion 1 o 2")
                self.getAllProviders()
            elif opt == 1:
                filename = input("\nIngrese el nombre de archivo: ")
        except ValueError as e:
            print("Valor inválido.")
            print(e)
            self.getAllProviders()
        providers = self.service.getProvidersList()
        self.table.setTableHeaders(self.headers)
        self.table.setTableContent(providers)
        self.table.printTable()
        if providers and opt == 1:
            self.exportCsv.setFilename(filename)
            self.exportCsv.setContent(providers)
            self.exportCsv.exportCsv()

    def searchProvider(self):
        print("\nSeleccione la forma en que desea buscar el proveedor\n")
        field = None
        printedField = None
        print("Opciones:\n")
        print("1 = Busqueda por Nombre")
        print("2 = Busqueda por Email")
        print("3 = Busqueda por Teléfono")
        try:
            option = int(input("\nIngrese la opción de búsqueda: "))
            if option == 1:
                field = "name"
                printedField = "Nombre"
            elif option == 2:
                field = "email"
                printedField = "Email"
            elif option == 3:
                field = "phone"
                printedField = "Teléfono"
            else:
                print("\nDebe ingresar un dato válido")
                self.searchProvider()
        except ValueError as e:
            print("Valor inválido.")
            print(e)
            self.searchProvider()
        search = input(f"Busqueda por {printedField} de proveedor: ")
        provider = self.service.searchProvider(search, field)
        self.table.setTableHeaders(self.headers)
        self.table.setTableContent(provider)
        self.table.printTable()