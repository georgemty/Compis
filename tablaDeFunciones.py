from tablaDeVariables import tablaVar
import sys

# function table
class tablaFunc():
    def __init__(self): #create dictionary
        self.functions = { }


    def agregarFuncion(self, type, fid, numberParams, paramType, paramsID, numberVars):
        if fid not in self.functions.keys(): #params to save in the table
            self.functions[fid] = {
                'type' : type,
                'numberParams' : numberParams,
                'paramType' : paramType,
                'paramsID' : paramsID,
                'variables' : tablaVar(), #it is done separatly, too many vars
                'numberVars' : numberVars
            }
            print('Funcion anadida: ',fid, ' ', type)
        else:
            print(id , 'ya existe')


    def buscarFun(self, id):
        return id in self.functions


    def buscarVariableEnTablaFunciones(self, fid, id):
        if self.functions[fid]['variables'].buscarVar(id):
            return True
        else:
            print('La variable', id, 'no existe...')


    def getTipoDeVariable(self, id, fid):
        if self.functions[fid]['variables'].buscarVar(id):
            return self.functions[fid]['variables'].getTipo(id)
        else:
            print('La variable', id, 'no existe...')


    # function to add variable to table function
    # to associate certain variables to certain functions
    def agregarVariable(self, fid, type, id):
        if self.functions[fid]['variables'].buscarVar(id):
            print(id, 'ya existe')
        else:
            self.functions[fid]['variables'].agregar(type, id)
            print("variable agregada ", id)
        #else:
        #    self.functions[fid]['variables'].agregar(type, id)
        #    print(id, 'fue anadida exitosamente')

    def agregarCteiAFuncTab(self, fid, type, value):
        if(self.function[fid]['variables'].)

    def printFun(self, fid):
        if id in self.functions:
            self.functions[fid]['variables'].printVar()


#test

# funcion = tablaFunc()
# funcion.agregarFuncion("void", "factores", 2, ["int", "float"], ["a", "b"], 2)
# print(funcion.buscarFun("factores"))
# funcion.printFun("factores")


# var = tablaFunc()
# var.agregarFuncion('void', 'ImprimeParametros', 3,
# ['int', 'float', 'char'],['uno','dos', 'tres'], 0)
# var.agregarVariable('ImprimeParametros','int', 'i')
# var.agregarVariable('ImprimeParametros', 'float', 'o')
# var.agregarVariable('ImprimeParametros', 'char', 'p')
# print(var.buscarFun('ImprimeParametros'))
# print(var.buscarFun('hgrughurhgu'))
# var.printFun('hola')
