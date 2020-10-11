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
        return id in self.listaVariables
    

    def printVar(self): #para vr si esta guardada la variable en la tabla
        for i in self.listaVariables:
            print( i, 'se encuentra en la tabla de variables')

#test

vari = tablaVar()
vari.agregar("int", "a")
vari.agregar("float", "b")
vari.agregar("char", "c")
print(vari.buscarVar("b"))
vari.printVar()


