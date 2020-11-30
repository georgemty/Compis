from tablaDeVariables import tablaVar
from memoria import Memory
import sys
import numpy as np
from numpy.linalg import inv

class tablaFunc():

    def __init__(self):
        self.funciones = {}
        self.m = Memory()
        self.contexto = "global"
        self.tablaDeVariablesGlobal = tablaVar()
        self.tablaDeVariablesLocal = tablaVar()
        self.tipoActual = ""
        self.arreglosMatrices = {
            'valorArreglo': None,
            'pilaDeDimensiones':    []
        }
        self.memoriaGlobal = 1000
        self.memoriaLocal = 8000

    def agregarFuncion(self, type, id, numberParams, paramType, paramsID, numberVars):
        if self.funciones.get(id) == None:
            self.funciones[id] = {
                'type' : type, # tipo de funcion
                'numberParams' : numberParams, # numero de parametros
                'paramType' : paramType, # tipo de parametros
                'paramsID' : paramsID, # nombre de parametros
                'variables' : tablaVar(),
                'numberVars' : numberVars # numero de variables
            }
            print('Funcion anadida: ',id, ' ', type)
        else:
            print(id , 'ya existe')

    def buscarFun(self, id):
        return id in self.funciones


    def buscarVariableEnTablaFunciones(self, fid, id):
        print(id + " buscar")
        if self.funciones[fid]['variables'].buscarVar(id) or self.funciones['programa']['variables'].buscarVar(id):
            return True
        else:
            print('La variable', id, 'no existe...')


    def getTipoDeVariable(self, id, fid):
        if self.funciones[fid]['variables'].buscarVar(id):
            return self.funciones[fid]['variables'].getTipo(id)
        else:
            print('La variable', id, 'no existe...')

    #Arreglos y matrices

    def agregarVariable(self, fid, type, id):
        #si ya existe en local no lo agrega
        if self.funciones[fid]['variables'].buscarVar(id):
            print('La variable', id, 'ya existe en el scope', fid)


        # si no existe en el local aun lo agrego
        elif not self.funciones[fid]['variables'].buscarVar(id):
            ad = self.m.set_var_direction(type, id, fid)
            self.funciones[fid]['variables'].agregar(type, id, ad)
            self.funciones[fid]['numberVars'] = self.funciones[fid]['numberVars'] + 1
            #print("no existe en local aun se va a agregar")


        # si existe como global no lo agrego
        elif self.funciones['programa']['variables'].buscarVar(id):
            print('La variable', id, 'ya existe en el programa como global')


        # si no existe como global lo agrego como global
        elif self.funciones['programa']['variables'].buscarVar(id):
            ad = self.m.set_var_direction('programa', id, fid)
            self.funciones['programa']['variables'].add(tipo, id, ad)
            self.funciones['programa']['numberVars'] = self.funciones[fid]['numberVars'] + 1

    def add_var_mem(self, tipo, vid, funId):
        self.m.set_var_address(tipo, vid, funId)


    def get_var_mem(self, var):
        return self.m.get_var_address(var)

    def get_arr_size(self, fid, varTipo):
        return self.m.get_var_address(var)

    def get_mat_size(self, var):
        return self.m.get_var_address(var)

    def getNumeroParametros(self, fid):
        return self.funciones[fid]['numberParams']

    def add_parametros_tabFun(self, fid, nameVar, varTipo):
        self.funciones[fid]['numberParams'] = self.funciones[fid]['numberParams'] + 1
        self.funciones[fid]['paramsID'].append(nameVar)
        self.funciones[fid]['paramType'].append(varTipo)


    def add_temp_mem(self, tipo, vid, funId):
       self.m.set_temp_address(tipo, vid, funId)


    def get_temp_mem(self, temp):
        return self.m.get_temp_address(temp)


    def add_cte_mem(self, val):
        self.m.set_cte_address(val)


    def get_cte_mem(self, val):
        return self.m.get_cte_address(val)


    def get_op_mem(self, op):
        return self.m.get_operator_address(op)

    def reset_temp_add(self):
        self.m.reset_temp_vals()

    def print_fun_vars(self, fid):
        if fid in self.funciones:
            self.funciones[fid]['variables'].printVar()

    def registraArreglo(self, value):
        self.arreglosMatrices['valorArreglo'] = value

    def registraDimension(self, value):
        self.arreglosMatrices['pilaDeDimensiones'].append(value)

    def generaArregloMatriz(self):
        e = None
        memoriaArreglosMatrices = self.getMemoriaArreglosMatrices()
        if self.contexto == "global":
            if((self.memoriaGlobal + memoriaArreglosMatrices) <= 7999):
                e = self.tablaDeVariablesGlobal.newVariable(self.arreglosMatrices['valorArreglo'], self.tipoActual + '_arr', self.memoriaGlobal, self.arreglosMatrices['pilaDeDimensiones'])
                self.memoriaGlobal += memoriaArreglosMatrices
            else:
                e = "Memory Error"
        elif self.contexto == "local":
            if((self.memoriaLocal + memoriaArreglosMatrices) <= 14999):
                e = self.tablaDeVariablesLocal.newVariable(self.arreglosMatrices['valorArreglo'], self.tipoActual + '_arr', self.memoriaLocal, self.arreglosMatrices['pilaDeDimensiones'])
                self.memoriaLocal += memoriaArreglosMatrices
            else:
                e = "Memory Error"
        return e

    def getMemoriaArreglosMatrices(self):
        if(len(self.arreglosMatrices['pilaDeDimensiones']) == 1):
            return self.arreglosMatrices['pilaDeDimensiones'][0]['u_limit']
        else:
            offsetDeDimensiones = self.arreglosMatrices['pilaDeDimensiones'][0]['limiteSuperior'] * self.arreglosMatrices['pilaDeDimensiones'][1]['limiteSuperior']
            return offsetDeDimensiones

    def transpose():
        result = [[X[j][i] for j in range(len(X))] for i in range(len(X[0]))]
        for r in result.getMemoriaArreglosMatrices():
            return result

    def sum():
        rows, cols = (len(X),len(Y[0]))
        result = [[0 for i in range(cols)] for j in range(rows)]

        for q in range(len(X)):
            for m in range(len(X[0])):
                result.getMemoriaArreglosMatrices()[q][m] = X[q][m] + Y[q][m]

                return result

    def subtraction():
        rows, cols = (len(X),len(Y[0]))
        result = [[0 for i in range(cols)] for j in range(rows)]

        for q in range(len(X)):
            for m in range(len(X[0])):
                result.getMemoriaArreglosMatrices()[q][m] = X[q][m] - Y[q][m]

                return result

    def multiplication(X,Y):
        rows, cols = (len(X),len(Y[0]))
        result = [[0 for i in range(cols)] for j in range(rows)]

        for i in range(len(X)):
            for j in range(len(Y[0])):
                for k in range(len(Y)):
                    result.getMemoriaArreglosMatrices()[i][j] += X[i][k] * Y[k][j]

                    return result

    def borrarArregloMatriz(self):
        self.arreglosMatrices['valorArreglo'] = ''
        self.arreglosMatrices['pilaDeDimensiones'] = []

    def obtenerDimensiones(self, name):
        if(self.contexto == "local"):
            variableDimensiones, e = self.tablaDeVariablesLocal.obtenerDimensiones(name)
            if variableDimensiones == None:
                return self.tablaDeVariablesGlobal.obtenerDimensiones(name)
            return variableDimensiones, e
        return self.tablaDeVariablesGlobal.obtenerDimensiones(name)
