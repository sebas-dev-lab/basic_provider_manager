import sys
import os

class SystemControl:
    def exitProgram(self):
        sys.exit()
    
    def clearConsole(self):
        print("\n")
        os.system("cls" if os.name == "nt" else "clear")
    