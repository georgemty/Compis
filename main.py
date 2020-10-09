import ply.lex as lex
import ply.yacc as yacc
import re
import codecs
import os
import sys

# palabras reservadas
reservadas = {
    'cond': 'CONDITION',
    'else': 'ELSE',
    'int': 'INT',
    'float': 'FLOAT',
    'output': 'OUTPUTPRINT',
    'program': 'PROGRAM',
    'var': 'VAR',
}

# Lista de tokens a usar
tokens = [
         'CTEI', 'CTEF', 'CTESTRING', 'ID',
         'TIMES', 'DIVIDE', 'SEMICOLON',
         'OPENP', 'CLOSEP', 'COMA',
         'OPENC', 'CLOSEC', 'COLON',
         'EQUAL', 'GREATERTHAN', 'LESSTHAN',
         'DIFERENT', 'MINUS', 'PLUS',
         ] + list(reservadas.values())

t_MINUS = r'\-'
t_PLUS = r'\+'
t_TIMES = r'\*'
t_DIVIDE = r'\/'
t_SEMICOLON = r'\;'
t_OPENP = r'\('
t_CLOSEP = r'\)'
t_COMA = r'\,'
t_EQUAL = r'\='
t_OPENC = r'\{'
t_CLOSEC = r'\}'
t_COLON = r'\:'
t_GREATERTHAN = r'\>'
t_LESSTHAN = r'\<'
t_DIFERENT = r'\<>'
t_ignore = ' \t\n' #espacios y tabulados


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

def t_CTEF(t):
    r'[-+]?\d*\.\d+'
    t.value = float(t.value)
    return t

def t_CTEI(t):
    r'0|[-+]?[1-9][0-9]*'
    t.value = int(t.value)
    return t

def t_CTESTRING(t):
    r'\'[\w\d\s\,. ]*\'|\"[\w\d\s\,. ]*\"'
    return t

def t_ID(t):
    r'[a-zA-Z][a-zA-Z_\d]*'
    t.type = reservadas.get(t.value, 'ID')
    return t



# el lexer
lexer = lex.lex()


def p_programa(p):

    p[0] = 'Programa compilado'


def p_empty(p):
    '''
        empty :
    '''
    p[0] = None


def p_error(p):
   print("Errores de sintaxis en el input", p)


# aalizador lexico
yacc.yacc()

def usaArchivo():
    try:
        archivo = 'prueba incorrecta.txt'
        arch = open(archivo, 'r')
        print("Nombre del archivo utilizado: " + archivo)
        info = arch.read()
        arch.close()
        lexer.input(info)
        while True:
            tok = lexer.token()
            if not tok:
                break
            print(tok)
        if (yacc.parse(info, tracking=True) == 'Programa compilado'):
            print("Sin errores de sintaxis")
        else:
            print("Error de sintaxis")
    except EOFError:
        print(EF)

usaArchivo()
