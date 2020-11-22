import sys
from memoria import Memory

class tablaVar:
    def __init__(self):
        self.listaVariables  ={}

    def agregar(self, type, id, address):
        self.listaVariables [id] ={
            'type': type,
            'address': address
        }

    def buscarVar(self, id):
        return id in self.listaVariables.keys()

    def printVar(self):
        print(self.listaVariables.items())

    def getTipo(self, id):
        return self.listaVariables[id]['type']
