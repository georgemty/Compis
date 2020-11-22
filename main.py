import ply.lex as lex
import ply.yacc as yacc
from avail import Avail
from tablaDeFunciones import tablaFunc
from tablaDeVariables import tablaVar
from cube import Cube
from stack import Stack
from memoria import Memory
import sys
import json

#reserved words from the language
reserved = {
    'funcion' : 'FUNCION',
    'var': 'VAR',
    'program': 'PROGRAM',
    'main' :'MAIN',
    'void' : 'VOID',
    'int' : 'INT',
    'float': 'FLOAT',
    'char' : 'CHAR',
    'if' : 'IF',
    'else' : 'ELSE',
    'return': 'RETURN',
    'end' : 'END',
    'read': 'READ',
    'print': 'PRINT',
    'for' : 'FOR',
    'from' : 'FROM',
    'while': 'WHILE',
    'to': 'TO'
}

#tokens are declared
tokens =[
    'ID',
    'CTEI',#int
    'CTEF', #float
    'CTEC', #char
    'CTESTRING', #string
    'EQUALS',
    'COMPARE',
    'PLUS',
    'MINUS',
    'MUL',
    'DIV',
    'LT', #<
    'GT', #>
    'LTE', #<=
    'GTE', #>=
    'AND',
    'OR',
    'LPAREN',
    'RPAREN',
    'COMMA',
    'SEMICOLON',
    'NE', #NOT EQUAL
    'LBRACKET',
    'RBRACKET',
    'LCURLY',
    'RCURLY',
    'TRANSPUESTA',
    'INVERSA',
    'DETERMINANTE',
    'COMILLA'
] + list(reserved.values())


#equivalents in symbols
t_SEMICOLON = r'\;'
t_COMMA = r'\,'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LCURLY = r'\{'
t_RCURLY = r'\}'
t_EQUALS = r'\='
t_COMPARE = r'\=='
t_PLUS = r'\+'
t_MINUS = r'\-'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COMILLA = r'\"'
t_MUL = r'\*'
t_DIV = r'\/'
t_GT = r'\>'
t_LT = r'\<'
t_GTE = r'\=>'
t_LTE = r'\<='
t_NE = r'\!='
t_AND = r'\&&'
t_OR = r'\|'
t_TRANSPUESTA = r'\¡'
t_DETERMINANTE = r'\$'
t_INVERSA = r'\?'
t_ignore = ' \t\n'


#id tokens
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t

#float tokens
def t_CTEF(t):
    r'[-+]?\d*\.\d+'
    t.value = float(t.value)
    return t

#tokens de strings
def t_CTESTRING(t):
    r'\'[\w\d\s\,. ]*\'|\"[\w\d\s\,. ]*\"'
    return t

#int tokens
def t_CTEI(t):
    r'0|[-+]?[1-9][0-9]*'
    t.value = int(t.value)
    return t

#char tokens
def t_CTEC(t):
    r"\'[^']\'"
    t.value = t.value[1]
    return t

#if errors are detected it prints error message
def t_error(t):
    print("ERROR at '%s'" % t.value)
    t.lexer.skip(1)

#Variables globales
lexer = lex.lex()
tablaDeFunciones = tablaFunc()
tipoDeFuncionActual = ''
functionID = ''
variableID = ''
parametrosID = ''

#Declaracion de pilas/listas
pilaDeNombres = Stack()
pilaDeTipos = Stack()
pilaDeOperadores = Stack()
cuadruplos = []
array = []
funciones = []
pendiente = 0
end_proceso = []
salto_end_proceso = 0
avail = Avail()
cuentaParametros = 0

#Clases
cubo = Cube()
saltos = Stack()
saltoFuncion = Stack()

def p_prog(p):
        '''
        prog : PROGRAM ID SEMICOLON agregarProg prog_1
        '''
        global programId
        programId = p[2]
        # print ("Nombre programa es ––––––––––––––", programId)
        p[0] = 'PROGRAMA COMPILADO'

def p_agregarProg(p):
    'agregarProg :'

    global tipoDeFuncionActual, functionID
    tipoDeFuncionActual = 'programa'
    functionID = 'programa'
    tablaDeFunciones.agregarFuncion(tipoDeFuncionActual, functionID, 0, [], [], 0)

def p_prog_1(p):
    '''
	prog_1 : var cuadruploMain metodos mainEnd prog_2
	prog_1 : var cuadruploMain metodos
	       | prog_2
	'''

def p_prog2(p):
    '''
    prog_2 : main
    '''

def p_main(p):
    '''
	main : MAIN guardaFuncion LPAREN param2 RPAREN LCURLY var estatutos RCURLY END
	'''
    global tipoDeFuncionActual
    tipoDeFuncionActual = p[1]
    # asigna nombre
    global functionID
    functionID = p[1]

    global tablaDeFunciones
    tablaDeFunciones.agregarFuncion(tipoDeFuncionActual, functionID, 0, [], [], 0)

def p_cuadruploMain(p):
    'cuadruploMain : '
    global saltos, cuadruplos
    cuad = ('GOTOMAIN', 'main', -1, None)
    cuadruplos.append(cuad)
    saltos.push(len(cuadruplos)-1)

def p_mainEnd(p):
    'mainEnd : '
    end = saltos.pop()
    llenarCuadruplo(end, -1)

#--------------------------------AQUI termina codigo referente al MAIN---------------------------------

#--------------------------------AQUI inicia codigo referente a tipos de variables---------------------

def p_type(p):
    '''
    type : INT guardaTipoDeVariable
         | FLOAT guardaTipoDeVariable
         | CHAR guardaTipoDeVariable
    '''

def p_guardaTipoDeVariable(p):
    'guardaTipoDeVariable : '
    global tipoDeVariableActual
    tipoDeVariableActual = p[-1]

def p_var(p):
    '''
    var : vars
        | empty
    '''

def p_vars(p):
    '''
    vars : VAR var_2
    '''

def p_var_2(p):
    # Recursividad
    '''
        var_2 : var_2 type var1 SEMICOLON agregarVar
              | empty
    '''

def p_var1(p):
    '''
    var1 : ID
         | ID COMMA var1 agregarVar
         | ID arr
         | ID arr COMMA var1 agregarVar
         | ID mat COMMA var1 agregarVar
         | ID mat
         | ID mat especial
         | empty
    '''
    global variableID
    variableID = p[1]

def p_agregarVar(p):
    'agregarVar :'
    global tablaDeFunciones
    global variableID
    global tipoDeVariableActual
    if not variableID == None:

        if tablaDeFunciones.buscarFun(functionID):
          tablaDeFunciones.agregarVariable(functionID, tipoDeVariableActual, variableID)
        else:
          SystemExit()

def p_especial(p):
    '''
    especial : TRANSPUESTA
             | INVERSA
             | DETERMINANTE
    '''

def p_arr(p):
    '''
    arr : LBRACKET CTEI RBRACKET
        | LBRACKET exp RBRACKET

    '''

def p_mat(p):
    '''
    mat : LBRACKET CTEI RBRACKET LBRACKET CTEI RBRACKET
        | LBRACKET exp RBRACKET LBRACKET exp RBRACKET
        | LBRACKET exp RBRACKET LBRACKET CTEI RBRACKET
        | LBRACKET CTEI RBRACKET LBRACKET exp RBRACKET
    '''

#--------------------------------AQUI termina codigo referente a variables---------------------------------

#--------------------------------AQUI inicia codigo referente a funciones-----------=-----------------------

def p_metodos(p):
    '''
    metodos : funcion metodos
            | empty

    '''

def p_funcion(p):
    '''
    funcion : FUNCION VOID funcion_1
            | FUNCION INT funcion_2
            | FUNCION CHAR funcion_2
            | FUNCION FLOAT funcion_2
    '''

def p_funcion_1(p):
    '''
    funcion_1 : ID guardaFuncion LPAREN param2 RPAREN SEMICOLON LCURLY var funcionGOTO estatutos RCURLY endFuncion
    '''

def p_funcion_2(p):
    '''
    funcion_2 : ID guardaFuncion LPAREN param2 RPAREN SEMICOLON LCURLY var funcionGOTO estatutos RETURN operadorReturn exp cuadruploReturn SEMICOLON RCURLY endFuncion
    '''

def p_guardaFuncion(p):
    ' guardaFuncion : '
    global tipoDeFuncionActual
    global functionID
    global tablaDeFunciones

    if p[-1] == 'main':
        tipoDeFuncionActual = 'main'
        functionID = p[-1]
        tablaDeFunciones.agregarFuncion(tipoDeFuncionActual, functionID, 0, [], [], 0)
    else:
        tipoDeFuncionActual = p[-2]
        functionID = p[-1]
        tablaDeFunciones.agregarFuncion(tipoDeFuncionActual, functionID, 0, [], [], 0)

def p_funcionGOTO(p):
    'funcionGOTO : '
    global funciones
    nombre = p[-8]
    salto = (nombre, len(cuadruplos))
    funciones.append(salto)

def p_endFuncion(p):
    'endFuncion : '
    global cuadruplos, tablaDeFunciones

    cuad = ('ENDFUNC', None, None, -1)
    cuadruplos.append(cuad)
    end_proceso.append(len(cuadruplos)-1)
    tablaDeFunciones.reset_temp_add()

def p_operadorReturn(p):
    'operadorReturn : '
    global pilaDeOperadores
    pilaDeOperadores.push('return')

def p_cuadruploReturn(p):
    '''
    cuadruploReturn :
    '''
    global cuadruplos, pilaDeNombres, pilaDeTipos, pilaDeOperadores, tipoDeFuncionActual

    if pilaDeOperadores.size() > 0:
        if pilaDeOperadores.peek() == 'return':
            operadores2 = pilaDeOperadores.pop()
            result = pilaDeNombres.pop()
            cuad = (operadores2, -1, -1, result)
            cuadruplos.append(cuad)
        else:
            print('Type Dissmatch')
            sys.exit()

def p_estatutos(p):
    '''
    estatutos : estatutos_2 estatutos
              | empty
    '''


def p_estatutos_2(p):
    '''
    estatutos_2 : asignacion SEMICOLON
                | llamada SEMICOLON
                | lectura SEMICOLON
                | escritura SEMICOLON
                | for
                | if
                | while
    '''

#--------------------------------AQUI termina codigo referente a funciones----------------------------------

#--------------------------------AQUI inicia codigo referente al metodo ASIGNACION--------------------------

def p_asignacion(p):
     '''
    asignacion : ID guardaVariable_2 EQUALS addOperadorName exp cuadruploAsignacion
               | ID guardaVariable_2 arr EQUALS addOperadorName exp cuadruploAsignacion
               | ID guardaVariable_2 mat EQUALS addOperadorName exp cuadruploAsignacion
    '''

def p_guardaVariable_2(p):
    '''guardaVariable_2 : '''
    global variableID, tablaDeFunciones, functionID, pilaDeNombres, pilaDeTipos
    variableID = p[-1]

    if tablaDeFunciones.buscarVariableEnTablaFunciones(functionID, variableID):
        tipos = tablaDeFunciones.getTipoDeVariable(variableID, functionID)
        tablaDeFunciones.add_var_mem(tipos, variableID, functionID)
        memVar = tablaDeFunciones.get_var_mem(variableID)

        pilaDeTipos.push(tipos)
        pilaDeNombres.push(memVar)

    else:
        SystemExit()

def p_addOperadorName(p):
    'addOperadorName : '
    global pilaDeOperadores
    aux = p[-1]
    pilaDeOperadores.push(aux)

def p_cuadruploAsignacion(p):
    'cuadruploAsignacion : '
    global pilaDeTipos, pilaDeNombres, pilaDeOperadores, cuadruplos

    if pilaDeOperadores.size() > 0:
        # sacar la direccion de memoria del operador
        op = tablaDeFunciones.get_op_mem(pilaDeOperadores.peek())
        operadores2 = pilaDeOperadores.pop()
        operando_derecho = pilaDeNombres.pop()
        operando_derecho_tipo = pilaDeTipos.pop()
        operando_izquierdo = pilaDeNombres.pop()
        operando_izquierdo_tipo = pilaDeTipos.pop()
        result = cubo.getTipo(operando_izquierdo_tipo, operando_derecho_tipo, operadores2)

        if result != 'ERROR':
            cuad = (op, operando_derecho, None, operando_izquierdo)
            cuadruplos.append(cuad)

    else:
        print('Vacio....')
        sys.exit()

#--------------------------------AQUI termina codigo referente al metodo ASIGNACION----------------------

#--------------------------------AQUI inicia codigo referente a parametros-------------------------------

def p_param(p):
    '''
    param   : ID agregarParametro
            | ID COMMA param agregarParametro
            | ID arr
            | ID arr COMMA param
            | ID mat COMMA param
            | ID mat
            | ID mat especial
            | empty
    '''
    global primerParametro
    primerParametro = p[1]


def p_agregarParametro(p):
    'agregarParametro :'
    global tablaDeFunciones, parametrosID, primerParametro, tipoDeVariableActual
    parametrosID = p[-1]
    print("a meter en parms", parametrosID)
    print("leyendo... extra", primerParametro)
    if not parametrosID == None and primerParametro is not None:
        if tablaDeFunciones.buscarFun(functionID):
          tablaDeFunciones.add_parametros_tabFun(functionID, tipoDeVariableActual, primerParametro)
          tablaDeFunciones.agregarVariable(functionID, tipoDeVariableActual, primerParametro)
          tablaDeFunciones.add_parametros_tabFun(functionID, tipoDeVariableActual, parametrosID)
          tablaDeFunciones.agregarVariable(functionID, tipoDeVariableActual, parametrosID)
          print(parametrosID, "----------param ID listo en", functionID)
          print(primerParametro, "param ID listo en", functionID)
        else:
          SystemExit()
    # else:
    #     print("no se puede agregar")

def p_param2(p):
    '''
    param2 : param2 type param
           | empty
    '''

#--------------------------------AQUI termina codigo referente a parametros----------------------

#--------------------------------AQUI inicia codigo referente al metodo LLAMADA--------------------------

def p_llamada(p):
    '''
    llamada : ID llamadaEra LPAREN auxiliarExp cuadruploParametros RPAREN cuadruploGoSub endProcesoLlena

    '''

def p_llamadaEra(p):
    'llamadaEra : '
    global cuadruplos, cuentaParametros, nombreVariable
    nombreVariable = p[-1]
    cuentaParametros = 0
    cuad = ('ERA', None, None, nombreVariable)
    cuadruplos.append(cuad)
    saltos.push(len(cuadruplos)-1)

def p_auxiliarExp(p):
    '''
    auxiliarExp : exp
                | exp  COMMA  auxiliarExp
                | empty
    '''

def p_cuadruploParametros(p):
    '''cuadruploParametros : '''
    global cuadruplos , cuentaParametros, nombreVariable, llamadaID, pendiente
    llamadaID  = p[-4]
    print("llamadaID", llamadaID)
    totalParams = tablaDeFunciones.getNumeroParametros(llamadaID)
    print("total params", totalParams)

    if not pilaDeNombres.isEmpty():
        val = pilaDeNombres.pop()
        print("value PARAM", val)
        if not cuentaParametros == totalParams:
            print("parametro actualizado numero ", cuentaParametros)
            cuad = ('PARAM', val, None, pendiente)
            pilaDeOperadores.push('PARAM')
            print("PARAM-----------------", nombreVariable, str(cuad))
            cuadruplos.append(cuad)
            pilaDeNombres.pop()
            cuentaParametros +=1
        else:
            print("params exceeded")

def p_cuadruploGoSub(p):
    'cuadruploGoSub : '
    global cuadruplos, funciones, salto_end_proceso
    gosub_call = p[-6]

    for i in funciones:
        if i[0] == gosub_call:
            end = i[1]
    cuad = ('GOSUB', gosub_call, None, end )
    cuadruplos.append(cuad)
    salto_end_proceso = len(cuadruplos)

def p_endProcesoLlena(p):
    ' endProcesoLlena : '
    global end_proceso, salto_end_proceso
    end = end_proceso.pop()
    temp = list(cuadruplos[end])
    temp[3] = salto_end_proceso
    cuadruplos[end] = tuple(temp)

#--------------------------------AQUI termina codigo referente al metodo LLAMADA----------------------

#--------------------------------AQUI inicia codigo referente al metodo LECTURA-----------------------

def p_lectura(p):
    '''
    lectura : READ operadorRead LPAREN exp cuadruploRead RPAREN
    '''

def p_operadorRead(p):
    'operadorRead : '
    global pilaDeOperadores
    pilaDeOperadores.push('read')

def p_cuadruploRead(p):
    'cuadruploRead : '
    global pilaDeOperadores
    if pilaDeOperadores.size() > 0:
        if pilaDeOperadores.peek() == 'read':
            op = tablaDeFunciones.get_op_mem('read')
            operator_aux = pilaDeOperadores.pop()
            valor = pilaDeNombres.pop()
            pilaDeTipos.pop()
            cuad = (op, None, None, valor)
            cuadruplos.append(cuad)

#--------------------------------AQUI termina codigo referente al metodo LECTURA----------------------

#--------------------------------AQUI inicia codigo referente al metodo ESCRITURA---------------------

def p_escritura(p):
     '''
    escritura : PRINT LPAREN operadorPrint escritura1 cuadruploPrint RPAREN
    '''

def p_escritura1(p):
     '''
    escritura1 : escritura2 COMMA escritura2
               | escritura2
    '''

def p_escritura2(p):
     '''
    escritura2 : COMILLA CTESTRING COMILLA
               | CTEI guardaCTE cuadruploPrint
               | CTEF guardaCTE cuadruploPrint
               | exp
    '''

def p_operadorPrint(p):
    'operadorPrint : '
    global pilaDeOperadores
    pilaDeOperadores.push('print')

def p_cuadruploPrint(p):
    'cuadruploPrint : '
    global pilaDeOperadores
    if pilaDeOperadores.size() > 0:
        if pilaDeOperadores.peek() == 'print':
            op = tablaDeFunciones.get_op_mem('print')
            operator_aux = pilaDeOperadores.pop()
            valor = pilaDeNombres.pop()
            pilaDeTipos.pop()
            cuad = (op, None, None, valor)
            # print('Cuadruplo:', str(cuad))
            cuadruplos.append(cuad)

def p_guardaCTE(p):
    '''guardaCTE : '''
    global cte, t, cteA, array
    cte = p[-1]
    t = type(cte)

    tablaDeFunciones.add_cte_mem(cte)

    cte_address = tablaDeFunciones.get_cte_mem(cte)
    cteA = (cte, cte_address)

    if not cteA in array:
        array.append(cteA)
    else:
        "cte existe ya"


    if (t == int):
        pilaDeTipos.push('int')
        pilaDeNombres.push(cte_address)

    elif (t == float):
        pilaDeTipos.push('float')
        pilaDeNombres.push(cte_address)


    else:
        pilaDeTipos.push('char')
        pilaDeNombres.push(cte_address)

#--------------------------------AQUI termina codigo referente al metodo ESCRITURA--------------

#--------------------------------AQUI inicia codigo referente al metodo FOR---------------------

def p_for(p):
    '''
    for : FOR operadorFor LPAREN for1 RPAREN cuadruploFor LCURLY estatutos RCURLY endFor
    '''

def p_for1(p):
    '''
    for1 : FROM asignacion TO exp
    '''

def p_operadorFor(p):
    'operadorFor :'
    global pilaDeOperadores, cuadruplos, saltos

    op = tablaDeFunciones.get_op_mem('for')
    pilaDeOperadores.push(op)
    saltos.push(len(cuadruplos))

def p_cuadruploFor(p):
    'cuadruploFor : '
    global pilaDeNombres, pilaDeTipos, cuadruplos, saltos
    resultado = pilaDeTipos.pop()

    if resultado == 'bool':
        valor = pilaDeNombres.pop()
        cuad = ('GOTOV', valor, None, -1)
        # print('quad:', str(cuad))
        cuadruplos.append(cuad)
        saltos.push(len(cuadruplos)-1)
    else:
        print('Error for quad....')
        sys.exit()

def p_endFor(p):
    'endFor : '
    global pilaDeNombres, pilaDeTipos, cuadruplos, saltos
    end = saltos.pop()
    retroceso = saltos.pop()
    retroceso = int(retroceso) + 1
    cuad = ('GOTO', None, None, retroceso)
    cuadruplos.append(cuad)
    llenarCuadruplo(end, retroceso)

def llenarCuadruplo(end, cont):
    global cuadruplos
    temp = list(cuadruplos[end])
    temp[3] = len(cuadruplos)
    cuadruplos[end] = tuple(temp)

#--------------------------------AQUI termina codigo referente al metodo FOR-------------------

#--------------------------------AQUI inicia codigo referente al metodo IF-ELSEs-----------------

def p_if(p):
    '''
    if : IF LPAREN exp RPAREN cuadruploIf LCURLY estatutos RCURLY else endIf
    '''

def p_cuadruploIf(p):
    'cuadruploIf : '
    global pilaDeNombres, pilaDeTipos, cuadruplos, saltos
    resultado = pilaDeTipos.pop()

    if resultado == 'bool':
        valor = pilaDeNombres.pop()
        cuad = ('GOTOF', valor, None, -1)
        # print('cuad:', str(cuad))
        cuadruplos.append(cuad)
        saltos.push(len(cuadruplos)-1)
    else:
        print('Error if quad....')
        sys.exit()

def p_endIf(p):
    'endIf : '
    global saltos
    end = saltos.pop()
    llenarCuadruplo(end, -1)

def p_else(p):
    '''
    else : ELSE cuadruploElse LCURLY estatutos RCURLY
         | empty
    '''

def p_cuadruploElse(p):
    'cuadruploElse : '
    global cuadruplos, saltos
    cuad = ('GOTO', None, None, -1)
    cuadruplos.append(cuad)
    fAux = saltos.pop()
    saltos.push(len(cuadruplos)-1)
    llenarCuadruplo(fAux, -1)
    # print('cuad:', str(cuad))

#--------------------------------AQUI termina codigo referente al metodo IF-ELSE--------------

#--------------------------------AQUI inicia codigo referente al metodo WHILE-----------------

def p_while(p):
    '''
    while : WHILE operadorWhile LPAREN exp RPAREN cuadruploWhile LCURLY estatutos RCURLY endWhile
    '''

def p_operadorWhile(p):
    'operadorWhile :'
    global pilaDeOperadores, cuadruplos, saltos
    op = tablaDeFunciones.get_op_mem('while')
    pilaDeOperadores.push(op)
    saltos.push(len(cuadruplos))

def p_cuadruploWhile(p):
    'cuadruploWhile : '
    global pilaDeNombres, pilaDeTipos, cuadruplos, saltos
    resultado = pilaDeTipos.pop()

    if resultado == 'bool':
        valor = pilaDeNombres.pop()
        cuad = ('GOTOF', valor, None, -1)
        print('quad:', str(cuad))
        cuadruplos.append(cuad)
        saltos.push(len(cuadruplos)-1)
    else:
        print('Error while quad....')
        sys.exit()

def p_endWhile(p):
    'endWhile : '
    global pilaDeNombres, pilaDeTipos, cuadruplos, saltos
    end = saltos.pop()
    retroceso = saltos.pop()
    cuad = ('GOTO', None, None, retroceso)
    cuadruplos.append(cuad)
    llenarCuadruplo(end, retroceso)

#--------------------------------AQUI termina codigo referente al metodo WHILE--------------

#--------------------------------AQUI inicia codigo referente a EXPRESIONES-----------------

def p_exp(p):
    '''
    exp : nexp
        | nexp OR addOperadorName nexp cuadruploOr
    '''

def p_cuadruploOr(p):
    'cuadruploOr : '
    global pilaDeOperadores
    if pilaDeOperadores.size() > 0:
        if pilaDeOperadores.peek() == '|':
            generaCuadruplo()

def p_nexp(p):
    '''
    nexp : compexp
         | compexp AND addOperadorName compexp cuadruploAnd
    '''

def p_cuadruploAnd(p):
    'cuadruploAnd : '
    global pilaDeOperadores
    if pilaDeOperadores.size() > 0:
        if pilaDeOperadores.peek() == '&&':
            generaCuadruplo()

def p_compexp(p):
    '''
    compexp : sumexp
            | compexp1 sumexp
    '''

def p_compexp1(p):
    '''
    compexp1 : sumexp GT addOperadorName sumexp cuadruploComparacion
             | sumexp LT addOperadorName sumexp cuadruploComparacion
             | sumexp GTE addOperadorName sumexp cuadruploComparacion
             | sumexp LTE addOperadorName sumexp cuadruploComparacion
             | sumexp NE addOperadorName sumexp cuadruploComparacion
             | sumexp COMPARE addOperadorName sumexp cuadruploComparacion
    '''

def p_cuadruploComparacion(p):
    'cuadruploComparacion : '
    global pilaDeOperadores
    if pilaDeOperadores.size() > 0:
        if pilaDeOperadores.peek() == '<' or pilaDeOperadores.peek() == '>' or pilaDeOperadores.peek() == '<=' or pilaDeOperadores.peek() == '>=' or pilaDeOperadores.peek() == '==' or pilaDeOperadores.peek() == '!=':
            generaCuadruplo()

def p_sumexp(p):
    '''
    sumexp : mulexp
           | mulexp PLUS addOperadorName mulexp cuadruploSuma
           | mulexp MINUS addOperadorName mulexp cuadruploSuma
    '''

def p_cuadruploSuma(p):
    'cuadruploSuma : '
    global pilaDeOperadores
    if pilaDeOperadores.size() > 0:
        if pilaDeOperadores.peek() == '+' or pilaDeOperadores.peek() == '-':
            generaCuadruplo()

def p_mulexp(p):
    '''
    mulexp : pexp
           | pexp MUL addOperadorName pexp cuadruploMultiplicacion
           | pexp DIV addOperadorName pexp cuadruploMultiplicacion
    '''

def p_cuadruploMultiplicacion(p):
    'cuadruploMultiplicacion : '
    global pilaDeOperadores
    if pilaDeOperadores.size() > 0:
        if pilaDeOperadores.peek() == '*' or pilaDeOperadores.peek() == '/':
            generaCuadruplo()

def p_pexp(p):
    '''
    pexp : var1 guardaID
         | CTEI guardaCTE
         | CTEF guardaCTE
         | CTEC guardaCTE
         | CTESTRING guardaCTE
         | llamada
         | LPAREN exp RPAREN
    '''

def p_guardaID(p):
    '''guardaID : '''
    global variableID, tablaDeFunciones, functionID, pilaDeNombres, pilaDeTipos, pendiente
    if not variableID == None:
        if tablaDeFunciones.buscarVariableEnTablaFunciones(functionID, variableID):
            tipos = tablaDeFunciones.getTipoDeVariable(variableID, functionID)

            tablaDeFunciones.add_var_mem(tipos, variableID, functionID)
            varMem = tablaDeFunciones.get_var_mem(variableID)
            print("variable", variableID, varMem)

            if parametrosID == variableID:
                print("same")
                pendiente = varMem


            if tipos:
                pilaDeTipos.push(tipos)
                pilaDeNombres.push(varMem)
                print('Direccion de', variableID, 'es', varMem)

            else:
                 SystemExit()

def p_empty(p):
    '''
    empty :
    '''
    p[0] = None

def generaCuadruplo():
    global pilaDeOperadores, pilaDeNombres, pilaDeTipos, cuadruplos

    if pilaDeOperadores.size() > 0:
        # Sacar direccion operador
        op = tablaDeFunciones.get_op_mem(pilaDeOperadores.peek())
        operando2 = pilaDeOperadores.pop()
        operando_derecho = pilaDeNombres.pop()
        operando_derecho_tipo = pilaDeTipos.pop()
        operando_izquierdo = pilaDeNombres.pop()
        operando_izquierdo_tipo = pilaDeTipos.pop()


        result_type = cubo.getTipo(operando_izquierdo_tipo, operando_derecho_tipo, operando2)
        if result_type != 'ERROR':
            result = avail.next()

            tablaDeFunciones.add_temp_mem(result_type, result, functionID)
            var_temp = tablaDeFunciones.get_temp_mem(result)

            cuad = (op, operando_izquierdo, operando_derecho, var_temp)
           # print('Cuadruplo: ' + str(cuad))

            cuadruplos.append(cuad)

            pilaDeNombres.push(var_temp)
            pilaDeTipos.push(result_type)

        else:
            print('No se ha generado quad')
            sys.exit()
    else:
        print('PILA DE OPERANDOS VACIA....')

#--------------------------------AQUI termina codigo referente a EXPRESIONES--------------

#--------------------------------AQUI inicia codigo referente a errores-------------------

def p_error(p):
    if p is not None:

        parser.errok()
        print('Syntax Error in input!', p)
        sys.exit()

    else:
        print('Unexpected end of input....')

#--------------------------------AQUI termina codigo referente a errores--------------

#--------------------------------AQUI inicia codigo referente al MAIN-------------------

parser = yacc.yacc()

if __name__ == '__main__':
    try:
        nombreArchivo = 'prueba.txt'
        arch = open(nombreArchivo, 'r')
        print("El archivo a leer es: " + nombreArchivo)
        informacion = arch.read()
        arch.close()
        lexer.input(informacion)
        while True:
            tok = lexer.token()
            if not tok:
                break

        if (parser.parse(informacion, tracking = True) == 'PROGRAMA COMPILADO'):
            print("Correct Syntax")

            #------------------------------Archivo de cuadruplos----------------------------------
            f = open ('cuadruplos.txt','w')
            for i in cuadruplos:
                f.write(str(i) + '\n')
            f.close()

            #------------------------------Archivo de constantes----------------------------------
            c = open("constantes.txt", 'w')
            for i in array:
                c.write(str(i) + '\n')
            c.close()

            #------------------------------Archivo de funciones----------------------------------
            d = open('funciones.txt', 'w')
            for i in tablaDeFunciones.funciones.keys():
               for j in tablaDeFunciones.funciones[i]['variables'].listaVariables.items():
                   quadFunciones = (i, j[1]['type'], j[0], j[1]['address'])
                   d.write(str(quadFunciones) + '\n')
            d.close()

        else:
            print("Syntax error")

    except EOFError:
        print(EOFError)
