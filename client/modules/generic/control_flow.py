from client.modules.generic.generic_menu import GenericMenu
from client.modules.provider.add_provider import AddProviderMenu
from client.modules.generic.system import SystemControl
from client.modules.provider.get_providers import FindAllProviders

class ControlFlow(SystemControl):
    def __init__(self):
        super().__init__()

        self.generic = GenericMenu()
        self.addProvider =  AddProviderMenu()
        self.findProvider = FindAllProviders()

    def flow(self):
        control = True
        while control:
            self.clearConsole()
            self.generic.print_generic_menu()
            option = self.generic.get_option()
            if (option == 1):
                self.clearConsole()
                self.addProvider.get_target()
                self.clearConsole()
                self.addProvider.tryAddProvider()
            elif option == 2:
                self.clearConsole()
                self.findProvider.getAllProviders()
            elif option == 3:
                self.clearConsole()
                self.findProvider.searchProvider()
            elif option == 4:
                self.exitProgram()
            else:
                continue
            self.controlFlow()
        

    def controlFlow(self):
        print("\n")
        process_control = self.generic.print_continue_process()
        if process_control == 'continue':
            return True
        elif process_control == 'exit':
            self.exitProgram()
        else:
            return self.controlFlow()