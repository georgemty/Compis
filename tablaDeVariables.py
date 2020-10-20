import sys

# table of variables, symbols
class tablaVar:
    def __init__(self): #whith self we can access the atributes of the class
        self.listaVariables = { }
        

    # function to add var to var table
    def agregar(self, type, id): 
        self. listaVariables[id ] = {
            'type': type 
        }

    def buscarVar(self, id):
        return id in self.listaVariables #.keys() # contains the keys of the dictionary, as a list
    
    def printVar(self): #para vr si esta guardada la variable en la tabla
        print(self.listaVariables.items())

    def getTipo(self, id):
        return self.listaVariables[id]['type']


#test

# vari = tablaVar()
# vari.agregar("int", "a")
# vari.agregar("float", "b")
# vari.agregar("char", "c")
# print(vari.buscarVar("b"))
# vari.printVar()


