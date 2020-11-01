import ply.lex as lex
import ply.yacc as yacc
from tablaDeVariables import tablaVar
from tablaDeFunciones import tablaFunc
from stack import Stack
from cuboSemantico import cuboSemantico as Cube
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
tipoDeVariableActual = ''
functionID = ''
variableID = ''

# pilas para los cuadruplos
pilaDeNombresDeVariables = Stack()
pilaDeTiposDeDato = Stack()
pilaDeOperadores = Stack()
quadruplos = []

#avail = Avail()

#instanciar Objetos de clases utilizadas
cuboSemantico = Cube
pilaDeSaltosCondicionales = Stack()

# parser
#reglas en minuscula
# palabrs resevadas en mayuscula

#estructura basica del programa
def p_prog(p):
    '''
    prog : PROGRAM ID agregarProg SEMICOLON prog_1 END
    '''
    global programId
    programId = p[2]
    p[0] = 'PROGRAMA COMPILADO'

# aux del prog para evitar ambiguedades
def p_prog_1(p):
    '''
    prog_1 : var methods main_1
    '''

def p_agregarProg(p):
    '''
    agregarProg :
    '''
    global tipoDeFuncionActual
    tipoDeFuncionActual = 'programa'

    global functionID
    functionID = p[-1]
    # print('---------', functionID, p[-1])
    global tablaDeFunciones
    if tablaDeFunciones.buscarFun(functionID):
        print('funcion ya existe')
    else:
        tablaDeFunciones.agregarFuncion(tipoDeFuncionActual, functionID, 0, [], [], 0)
        print('\nFuncion que se agrego', functionID, 'de tipo', tipoDeFuncionActual)

#main del programa
def p_main_1(p):
    '''
    main_1 : MAIN LPAREN RPAREN LCURLY estatutos RCURLY
    '''
    global tipoDeFuncionActual
    global functionID
    global tablaDeFunciones

    tipoDeFuncionActual = p[1]

    functionID = p[1]
    # print('--------', functionID)

    tablaDeFunciones.agregarFuncion(tipoDeFuncionActual, functionID, 0, [], [], 0)
    print('\nFuncion que se agrego', functionID, 'de tipo:', tipoDeFuncionActual)

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
    for : FOR asignacion TO CTEI LCURLY estatutos RCURLY
    '''

def p_while(p):
    '''
    while : WHILE LPAREN expresion RPAREN LCURLY estatutos RCURLY
    '''

def p_if(p):
    '''
    if : IF LPAREN expresion RPAREN THEN LCURLY estatutos RCURLY else
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
    expresion : CTEI
        | CTEF
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
    lecturaAux : ID lecturaAux2
    '''

def p_lecturaAux2(p):
    '''
    lecturaAux2 : COMMA lecturaAux
        | empty
    '''

def p_asignacion(p):
    '''
    asignacion : ID guardaIdDeVariable EQUALS tipoDeOperador expresion
    '''

def p_quadruploAsignacion(p):
    '''
    quadruploAsignacion :
    '''
    if operadores.size() > 0:
        # if operadores.top() == '=':
        operadores2 = operadores.pop()
        operando_derecho = stackName.pop()
        operando_derecho_tipo = stackTypes.pop()
        operando_izquierdo = stackName.pop()
        operando_izquierdo_tipo = stackTypes.pop()
        result = cubo.getTipo(operando_izquierdo_tipo, operando_derecho_tipo, operadores2)

        if result != 'ERROR':
            quad = (operadores2, operando_derecho, None, operando_izquierdo)
            print('quadruplo:', str(quad))
            quadruples.append(quad)
        else:
            print('Type Dissmatch....')
            sys.exit()
            
    else:
        print('Vacio....')
        sys.exit()

def p_guardaIdDeVariable(p):
    '''
    guardaIdDeVariable :
    '''
    global variableID, tablaDeFunciones, functionID, pilaDeNombresDeVariables, pilaDeTiposDeDato

    variableID = p[-1]
    if tablaDeFunciones.buscarVariableEnTablaFunciones(functionID, variableID):
        tipos = tablaDeFunciones.getTipoDeVariable(variableID, functionID)
        # print('tipos saveID2', tipos)
        # print('varID saveID2', varId)
        pilaDeTiposDeDato.push(tipos)
        pilaDeNombresDeVariables.push(variableID)
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
    var1 : type ID idDeVariable varMulti SEMICOLON var2
    '''

# para agregar mas de un tipo de variablea; solo puede ser empty la segunda que entra
def p_var2(p):
    '''
    var2 : var1
        | empty
    '''


def p_varMulti(p):
    '''
    varMulti : COMMA ID idDeVariable varMulti
        | empty
    '''

def p_idDeVariable(p):
    '''
    idDeVariable :
    '''

    global variableID
    variableID = p[-1]

def p_agregarVariable(p):
    '''
    agregarVariable :
    '''

    global tablaDeFunciones
    global variableID
    global tipoDeVariableActual

    if not variableID == None:
        if tablaDeFunciones.buscarFun(functionID):
            tablaDeFunciones.agregarVariable(functionID, tipoDeVariableActual, variableID)
        else:
            print('La funcion no existe')
            #SystemExit()

def p_type(p):
    '''
    type : INT returnTipoDeFuncion
         | FLOAT returnTipoDeFuncion
         | CHAR returnTipoDeFuncion
    '''

def p_returnTipoDeFuncion(p):
    '''
    returnTipoDeFuncion :
    '''

    global tipoDeFuncionActual
    global tipoDeVariableActual

    tipoDeFuncionActual = p[-1]
    tipoDeVariableActual = p[-1]

"""
def p_tipoDeDato(p):
    '''
    tipoDeDato :
    '''
    global tipoDeFuncionActual
    tipoDeFuncionActual = p[-1]
"""

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
    argumentos : type ID multiArg
        | empty
    '''

def p_multiArg(p):
    '''
    multiArg : COMMA argumentos
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

def p_tipoDeOperador(p):
    '''
    tipoDeOperador :
    '''
    global pilaDeOperadores

    auxiliar = p[-1]
    pilaDeOperadores.push(auxiliar)


#Expresiones

def p_exp(p):
    '''
    exp : texp
        | texp OR tipoDeOperador texp
    '''

def p_texp(p):
    '''
    texp : gexp
         | gexp AND tipoDeOperador gexp
    '''

def p_gexp(p):
    '''
    gexp : mexp
         | gexp1 mexp
    '''

def p_gexp1(p):
    '''
    gexp1 : mexp GT tipoDeOperador mexp
          | mexp LT tipoDeOperador mexp
          | mexp GTE tipoDeOperador mexp
          | mexp LTE tipoDeOperador mexp
          | mexp NE tipoDeOperador mexp
    '''

def p_mexp(p):
    '''
    mexp : texp
         | texp PLUS tipoDeOperador texp
         | texp MINUS tipoDeOperador texp
    '''

def p_texp(p):
    '''
    texp : fexp
         | fexp MUL tipoDeOperador fexp
         | fexp DIV tipoDeOperador fexp
    '''

def p_fexp(p):
    '''
    fexp : var1
         | CTEI
         | CTEF
         | CTEC
         | llamada
         | LPAREN exp RPAREN
    '''


parser = yacc.yacc()

def p_quad_asignacion(p):
    'quad_asignacion'
    global operadores, stacknom, stackTypes, quadruples

    if operadores.size() > 0:
        operando

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
