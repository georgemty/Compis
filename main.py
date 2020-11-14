import ply.lex as lex
import ply.yacc as yacc
import sys
from tablaDeVariables import tablaVar
from tablaDeFunciones import tablaFunc
from stack import Stack
from cuboSemantico import *
from avail import Avail

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
    'then' : 'THEN',
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
    'COMILLA',
    'SEMICOLON',
    'NE', #NOT EQUAL
    'LBRACKET',
    'RBRACKET',
    'LCURLY',
    'RCURLY'
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
t_NE = r'\<>'
t_AND = r'\&&'
t_OR = r'\|'
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

lexer = lex.lex()

lexer.input("ab3 = 'a'")

"""while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)"""

tablaDeFunciones = tablaFunc()
tipoDeFuncionActual = ''
functionID = ''
variableID = ''
programId = ''

# pilas para los cuadruplos
pilaDeNombresDeVariables = Stack()
pilaDeTiposDeDato = Stack()
pilaDeOperadores = Stack()
pilaDeOperandos = Stack()
operandoDerecho = ''
operandoIzquierdo = ''
operandoDerechoTipo = ''
operandoIzquierdoTipo = ''
cuadruplos = []
tipoDeVariableActual = ''
end_proc = []
salto_end_proc = []

avail = Avail()

#instanciar Objetos de clases utilizadas

pilaDeSaltosCondicionales = Stack()

# parser
#reglas en minuscula
# palabrs resevadas en mayuscula
#estructura basica del programa
def p_prog(p):
    '''
    prog : PROGRAM ID SEMICOLON agregarProg prog_1 END
    '''
    global programId
    programId = p[2]
    p[0] = 'PROGRAMA COMPILADO'

# aux del prog para evitar ambiguedades
def p_prog_1(p):
    '''
    prog_1 : var cuadruploMain methods cuadruploMainEnd main_1
           | var cuadruploMain methods
           | main_1
    '''

def p_agregarProg(p):
    '''
    agregarProg :
    '''
    global tipoDeFuncionActual
    global functionID
    global tablaDeFunciones

    tipoDeFuncionActual = 'program'
    functionID = p[-2]

    if tablaDeFunciones.buscarFun(functionID):
        print("Funcion ya existe")
    else:
        tablaDeFunciones.agregarFuncion(tipoDeFuncionActual, functionID, 0, '', '', 0)
        #print('\nSe agrego funcion ', functionID, ' de tipo ', tipoDeFuncionActual)

#main del programa
def p_main_1(p):
    '''
    main_1 : MAIN LPAREN RPAREN LCURLY estatutos RCURLY 
    '''

def p_cuadruploMain(p):
    '''
    cuadruploMain : 
    '''

    global pilaDeSaltosCondicionales
    global cuadruplos

    cuadruplo = ('GOTOMAIN', 'main', -1, None)
    cuadruplos.append(cuadruplo)
    pilaDeSaltosCondicionales.push(len(cuadruplos)-1)

def p_cuadruploMainEnd(p):
    '''
    cuadruploMainEnd :
    '''
    
    global pilaDeSaltosCondicionales

    end = pilaDeSaltosCondicionales.pop()
    llenar_quad(end, -1)

def p_estatutos(p):
    '''
    estatutos : asignacion SEMICOLON estatutos
              | llamadaFun estatutos
              | lectura estatutos
              | escritura estatutos
              | for estatutos
              | while estatutos
              | if estatutos
              | empty
    '''

def p_for(p):
    '''
    for : FOR LPAREN asignacion TO CTEI RPAREN LCURLY estatutos RCURLY forOperador forCuadruplo
    '''

def p_forOperador(p):
    '''
    forOperador :
    '''
    global pilaDeOperadores
    global cuadruplos
    global pilaDeSaltosCondicionales

    pilaDeOperadores.push('for')
    print("FOR")
    pilaDeSaltosCondicionales.push(len(cuadruplos))

def p_forCuadruplo(p):
    '''
    forCuadruplo :
    '''
    global pilaDeNombresDeVariables, pilaDeTiposDeDato, cuadruplos, pilaDeSaltosCondicionales
    tipoDeResultado = pilaDeTiposDeDato.pop()
    print("Tipo de resultado ", tipoDeResultado)
    print("ENTRO EL CUADRUPLO FOR")
    if (tipoDeResultado == 'bool'):
        #pilaDeOperadores.pop()
        print("ENTRO AL IF BOOL")
        valor = pilaDeOperandos.pop()
        generadorQuad = ('GotoF', valor, None, -1)
        cuadruplos.append(generadorQuad)
        pilaDeSaltosCondicionales.push(len(cuadruplos)-1)
        print("EL CUADRUPLO ES ", generadorQuad)
    else:
        print('Error for quad....')
        SystemExit()

def p_while(p):
    '''
    while : WHILE LPAREN exp RPAREN LCURLY estatutos RCURLY
    '''
    
def p_whileOperator(p):
	''' 
    whileOperator : 
    '''
    
	global pilaDeOperadores, pilaDeSaltosCondicionales, cuadruplos
	pilaDeOperadores.push('while')
	pilaDeSaltosCondicionales.push(len(cuadruplos)) 
    #print("Agrega el while ", pilaDeOperadores.top())

def p_whileCuadruplo(p):
    '''
    whileCuadruplo :
    '''

    global pilaDeNombresDeVariables
    global pilaDeTiposDeDato
    global cuadruplos
    global pilaDeSaltosCondicionales

    tipoResultado = pilaDeTiposDeDato.pop()

    if tipoResultado == 'bool':
        valor = pilaDeNombresDeVariables.pop()
        cuadruplo = ('GotoF', valor, None, -1)
        print('Cuadruplo WHILE --- ', str(cuadruplo))
        cuadruplos.push(cuadruplo)
        pilaDeSaltosCondicionales.push(len(cuadruplos)-1)
    else:
        print('Error while quad...')
        SystemExit()

def p_loopEnd(p):
    '''
    loopEnd :
    '''

    global pilaDeNombresDeVariables
    global pilaDeTiposDeDato
    global cuadruplos
    global pilaDeSaltosCondicionales
    global llenarCuadruplo

    end = pilaDeSaltosCondicionales.pop()
    retrocede = pilaDeSaltosCondicionales.pop()
    cuadruplo = ('Goto', None, None, retrocede)
    llenarCuadruplo(end, -1)


def llenar_quad(end, cont):
    global cuadruplos

    variableAux = list(cuadruplos[end])
    variableAux[3] = len(cuadruplos)
    quadruples[end] = tuple(variableAux)

def p_llenar_endproc(p):
    '''
    llenar_endproc :
    '''

    global end_proc
    global salto_end_proc
    global cuadruplos

    end = end_proc.pop()
    temp = list(cuadruplos[end])
    temp[3] = salto_end_proc
    cuadruplos[end] = tuple(temp)

def p_if(p):
    '''
    if : IF LPAREN exp RPAREN THEN LCURLY estatutos RCURLY else
    '''

def p_else(p):
    '''
    else : ELSE LCURLY estatutos RCURLY
         | empty
    '''

def p_return(p):
    '''
    return : RETURN expresion SEMICOLON
    '''

def p_expresion(p):
    '''
    expresion : CTEI operandoConstante
              | CTEF operandoConstante
    '''

def p_escritura(p):
    '''
    escritura : PRINT LPAREN escrituraAux RPAREN SEMICOLON
    '''

def p_escrituraAux(p):
    '''
    escrituraAux : ID
                 | COMILLA CTESTRING COMILLA
                 | COMILLA CTESTRING COMILLA COMMA ID
    '''

def p_lectura(p):
    '''
    lectura : READ LPAREN lecturaAux RPAREN SEMICOLON
    '''

def p_lecturaAux(p):
    '''
    lecturaAux : ID guardaIdDeVariable lecturaAux2
    '''

def p_lecturaAux2(p):
    '''
    lecturaAux2 : COMMA lecturaAux
                | empty
    '''

def p_asignacion(p):
    '''
    asignacion : ID guardaIdDeVariable funcionAsignacion EQUALS tipoDeOperador exp quadruploAsignacion
    '''

def p_quadruploAsignacion(p):
    '''
    quadruploAsignacion :
    '''
    global pilaDeTiposDeDato
    global pilaDeNombresDeVariables
    global pilaDeOperadores
    global cuadruplos
    

    if pilaDeOperadores.size() > 0:
        #print("PASA IF 311")
        if(pilaDeOperadores.pop() == '='):
            #print("PASA IF 313")
            #print("++++++++++++++++++++++")
            operator = pilaDeOperadores.pop()
            operator = '='
            #print("OPERATOR ", operator)
            operandoIzquierdo = pilaDeOperandos.pop()
            print("OPERANDO IZQ ", operandoIzquierdo)
            
            operandoIzquierdoTipo = pilaDeTiposDeDato.pop()
            print("TIPO IZQUIERDO---", operandoIzquierdoTipo)
            
            operandoDerecho = pilaDeOperandos.pop()
            print("OPERANDO DER ", operandoDerecho)
            operandoDerechoTipo = pilaDeTiposDeDato.pop()
            
            print("Tipo DERECHO", operandoDerechoTipo)
            resultado = getType(operandoIzquierdoTipo, operandoDerechoTipo, operator)
            print("GET TYPE RESULTADO DE CUBO", resultado)

            if resultado != 'Error':
                print("GET TYPE RESULTADO DE CUBO", resultado)
                #print("PASA IF 323")
                cuadruplosAux = (operator, operandoIzquierdo, None, operandoDerecho)
                #print("OPERATOR ", operator)
                print('cuadruplo: ' + str(cuadruplosAux))
                cuadruplos.append(cuadruplosAux)
            else:
                print('Type mismatch')
                SystemExit()

def p_guardaIdDeVariable(p):
    '''
    guardaIdDeVariable :
    '''
    global variableID
    global tablaDeFunciones
    global functionID
    global pilaDeNombresDeVariables
    global pilaDeTiposDeDato

    variableID = p[-1]

    if(tablaDeFunciones.buscarFun(functionID) == True):
        tablaDeFunciones.agregarVariable(functionID, pilaDeTiposDeDato.pop(), variableID)
    else:
        print("Funcion no encontrada")

def p_funcionAsignacion(p):
    '''
    funcionAsignacion :
    '''
    global tablaDeFunciones
    global variableID

    variableID = p[-2]
    
    print("FUnCTION ID", functionID)
    print("VARIABLE ID", variableID)
    print("HOLIS", tablaDeFunciones.getTipoDeVariable(variableID, functionID))

    if(tablaDeFunciones.buscarVariableEnTablaFunciones(functionID, variableID)):
        pilaDeTiposDeDato.push(tablaDeFunciones.getTipoDeVariable(variableID, functionID))
        print("PILA DE TIPO DE DATO ASIGNADO", pilaDeTiposDeDato.top())
        pilaDeOperandos.push(variableID)
    else:
        SystemExit()

def p_llamadaFun(p):
    '''
    llamadaFun : ID LPAREN expresion RPAREN SEMICOLON
    '''

def p_var(p):
    '''
    var : VAR var1
        | empty
    '''
#aux de var para agregar variables de otros tipos
def p_var1(p):
    '''
    var1 : type ID guardaIdDeVariable agregarVariable varMulti SEMICOLON var2
    '''

# para agregar mas de un tipo de variablea; solo puede ser empty la segunda que entra
def p_var2(p):
    '''
    var2 : var1
         | empty
    '''

def p_varMulti(p):
    '''
    varMulti : COMMA ID guardaIdDeVariable  agregarVariable varMulti
             | empty
    '''
    
def p_agregarVariable(p):
    '''
    agregarVariable :
    '''

    global tablaDeFunciones
    global variableID
    global tipoDeVariableActual
    global functionID

    if not variableID == None:
        if tablaDeFunciones.buscarFun(functionID):
            tablaDeFunciones.agregarVariable(functionID, tipoDeVariableActual, variableID)
            print("FUNCION ", functionID)
            print("VARIABLE ", variableID)
        else:
            print('La funcion no existe')
            #SystemExit()

'''
def p_agregarVariableAux(p):
    
    agregarVariableAux :
    

    global variableID
    global tablaDeFunciones
    global functionID
    global pilaDeNombresDeVariables
    global pilaDeTiposDeDato

    variableID = p[-3]
    
    if tablaDeFunciones.buscarVariableEnTablaFunciones(functionID, variableID):
        tipos = tablaDeFunciones.getTipoDeVariable(variableID, functionID)
        pilaDeTiposDeDato.push(tipos)
    else:
        SystemExit()
'''

def p_type(p):
    '''
    type : INT guardarTipoDeVariable
         | FLOAT guardarTipoDeVariable
         | CHAR guardarTipoDeVariable
    '''

def p_guardarTipoDeVariable(p):
    '''
    guardarTipoDeVariable :
    '''

    global tipoDeVariableActual
    tipoDeVariableActual = p[-1]

def p_methods(p):
    '''
    methods : FUNCION VOID voidMethod
            | FUNCION INT funcionQueRetorna
            | FUNCION CHAR funcionQueRetorna
            | FUNCION FLOAT funcionQueRetorna
            | empty
    '''

def p_voidMethod(p):
    '''
    voidMethod : ID guardarFuncion LPAREN argumentos RPAREN var LCURLY estatutos RCURLY methods
    '''

def p_funcionQueRetorna(p):
    '''
    funcionQueRetorna : ID guardarFuncion LPAREN argumentos RPAREN var LCURLY estatutos return RCURLY methods
    '''

def p_guardarFuncion(p):
    '''
    guardarFuncion :
    '''

    global tipoDeFuncionActual
    global functionID
    global tablaDeFunciones

    tipoDeFuncionActual = p[-2]
    functionID = p[-1]

    if p[-2] == 'void':
        tipoDeFuncionActual = 'void'

    tablaDeFunciones.agregarFuncion(tipoDeFuncionActual, functionID, 0, [], [], 0)

def p_argumentos(p):
    '''
    argumentos : type ID guardaIdDeVariable multiArg
               | empty
    '''

def p_multiArg(p):
    '''
    multiArg : COMMA argumentos guardaIdDeVariable
             | empty
    '''

def p_error(p):
    print("Syntax Error in input!", p)

def p_llamada(p):
    '''
    llamada : ID LPAREN exp RPAREN
    '''

def p_empty(p):
    '''
    empty :
    '''
#Expresiones

def p_tipoDeOperador(p):
    '''
    tipoDeOperador :
    '''
    global pilaDeOperadores

    aux = p[-1]
    pilaDeOperadores.push(aux)

def p_exp(p):
    '''
    exp : nexp exp1
    '''

def p_exp1(p):
    '''
    exp1 : OR tipoDeOperador exp
         | empty
    '''

def p_nexp(p):
    '''
    nexp : compexp nexp1
    '''

def p_nexp1(p):
    '''
    nexp1 : AND nexp
          | empty
    '''

def p_compexp(p):
    '''
    compexp : sumexp compexp1
    '''

def p_compexp1(p):
    '''
    compexp1 : GT tipoDeOperador sumexp
             | LT tipoDeOperador sumexp
             | GTE tipoDeOperador sumexp
             | LTE tipoDeOperador sumexp
             | NE tipoDeOperador sumexp
             | EQUALS tipoDeOperador sumexp
             | empty
    '''

def p_sumexp(p):
    '''
    sumexp : mulexp sumexp1
    '''

def p_sumexp1(p):
    '''
    sumexp1 : PLUS tipoDeOperador sumexp
            | MINUS tipoDeOperador sumexp
            | empty
    '''

def p_mulexp(p):
    '''
    mulexp : pexp mulexp1
    '''

def p_mulexp1(p):
    '''
    mulexp1 : MUL tipoDeOperador mulexp
            | DIV tipoDeOperador mulexp
            | empty
    '''

def p_pexp(p):
    '''
    pexp : CTEI
         | CTEF
         | CTEC
         | CTESTRING
         | llamada
         | ID
         | LPAREN exp RPAREN
    '''

def p_operandoConstante(p):
    '''
    operandoConstante :
    '''

    global pilaDeOperandos
    global pilaDeOperadores
    global tablaDeFunciones

    resultado = type(p[-1])
    if resultado == int:
        pilaDeTiposDeDato.push('int')
    elif resultado == float:
        pilaDeTiposDeDato.push('float')
    elif resultado == str:
        if(len(p[-1]) > 1):
            pilaDeTiposDeDato.push('string')
        else:
            pilaDeTiposDeDato.push('char')
    pilaDeOperandos.push(p[-1])

parser = yacc.yacc()

def main():
    try:
        #nombreArchivo = 'test1.txt'
        nombreArchivo = 'test1.txt'
        arch = open(nombreArchivo, 'r')
        print("El archivo a leer es: " + nombreArchivo)
        informacion = arch.read()
        arch.close()
        lexer.input(informacion)
        while True:
            tok = lexer.token()
            if not tok:
                break
            print(tok)
        if (parser.parse(informacion, tracking = True) == 'PROGRAMA COMPILADO'):
            print ("Correct Syntax")
        else:
            print("Syntax error")
    except EOFError:
        # print("ERROREOF")
        print(EOFError)
main()
