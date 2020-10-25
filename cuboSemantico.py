import sys
from collections import defaultdict

#Este archivo contiene el cubo semantico del proyecto, el cual es util
#para realizar operaciones aritmeticas, logicas, comparaciones y asignaciones

#inicializacion del diccionario
cuboSemantico = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: None)))

#ADDITION

cuboSemantico['int']['int']['+'] = 'int'
cuboSemantico['int']['float']['+'] = 'float'
cuboSemantico['float']['int']['+'] = 'float'

cuboSemantico['int']['char']['+'] = 'error'
cuboSemantico['char']['int']['+'] = 'error'

cuboSemantico['char']['float']['+'] = 'error'
cuboSemantico['float']['char']['+'] = 'error'

cuboSemantico['float']['float']['+'] = 'float'

cuboSemantico['char']['char']['+'] = 'error'

#SUBTRACTION

cuboSemantico['int']['int']['-'] = 'int'
cuboSemantico['int']['float']['-'] = 'float'
cuboSemantico['float']['int']['-'] = 'float'

cuboSemantico['int']['char']['-'] = 'error'
cuboSemantico['char']['int']['-'] = 'error'

cuboSemantico['char']['float']['-'] = 'error'
cuboSemantico['float']['char']['-'] = 'error'

cuboSemantico['float']['float']['-'] = 'float'

cuboSemantico['char']['char']['-'] = 'error'

#MULTIPLICATION

cuboSemantico['int']['int']['*'] = 'int'
cuboSemantico['int']['float']['*'] = 'float'
cuboSemantico['float']['int']['*'] = 'float'

cuboSemantico['int']['char']['*'] = 'error'
cuboSemantico['char']['int']['*'] = 'error'

cuboSemantico['char']['float']['*'] = 'error'
cuboSemantico['float']['char']['*'] = 'error'

cuboSemantico['float']['float']['*'] = 'float'

cuboSemantico['char']['char']['*'] = 'error'

#DIVISION

cuboSemantico['int']['int']['/'] = 'float'
cuboSemantico['int']['float']['/'] = 'float'
cuboSemantico['float']['int']['/'] = 'float'

cuboSemantico['int']['char']['/'] = 'error'
cuboSemantico['char']['int']['/'] = 'error'

cuboSemantico['char']['float']['/'] = 'error'
cuboSemantico['float']['char']['/'] = 'error'

cuboSemantico['float']['float']['/'] = 'float'

cuboSemantico['char']['char']['/'] = 'error'

#GREATER THAN

cuboSemantico['int']['int']['>'] = 'bool'
cuboSemantico['int']['float']['>'] = 'bool'
cuboSemantico['float']['int']['>'] = 'bool'

cuboSemantico['int']['char']['>'] = 'error'
cuboSemantico['char']['int']['>'] = 'error'

cuboSemantico['char']['float']['>'] = 'error'
cuboSemantico['float']['char']['>'] = 'error'

cuboSemantico['float']['float']['>'] = 'bool'

cuboSemantico['char']['char']['>'] = 'error'

#LESS THAN

cuboSemantico['int']['int']['<'] = 'bool'
cuboSemantico['int']['float']['<'] = 'bool'
cuboSemantico['float']['int']['<'] = 'bool'

cuboSemantico['int']['char']['<'] = 'error'
cuboSemantico['char']['int']['<'] = 'error'

cuboSemantico['char']['float']['<'] = 'error'
cuboSemantico['float']['char']['<'] = 'error'

cuboSemantico['float']['float']['<'] = 'bool'

cuboSemantico['char']['char']['<'] = 'error'

#GREATER OR EQUAL THAN

cuboSemantico['int']['int']['=>'] = 'bool'
cuboSemantico['int']['float']['=>'] = 'bool'
cuboSemantico['float']['int']['=>'] = 'bool'

cuboSemantico['int']['char']['=>'] = 'error'
cuboSemantico['char']['int']['=>'] = 'error'

cuboSemantico['char']['float']['=>'] = 'error'
cuboSemantico['float']['char']['=>'] = 'error'

cuboSemantico['float']['float']['=>'] = 'bool'

cuboSemantico['char']['char']['=>'] = 'error'

#LESS OR EQUAL THAN

cuboSemantico['int']['int']['<='] = 'bool'
cuboSemantico['int']['float']['<='] = 'bool'
cuboSemantico['float']['int']['<='] = 'bool'

cuboSemantico['int']['char']['<='] = 'error'
cuboSemantico['char']['int']['<='] = 'error'

cuboSemantico['char']['float']['<='] = 'error'
cuboSemantico['float']['char']['<='] = 'error'

cuboSemantico['float']['float']['<='] = 'bool'

cuboSemantico['char']['char']['<='] = 'error'

#DIFFERENT NO EQUAL

cuboSemantico['int']['int']['<>'] = 'bool'
cuboSemantico['int']['float']['<>'] = 'bool'
cuboSemantico['float']['int']['<>'] = 'bool'

cuboSemantico['int']['char']['<>'] = 'error'
cuboSemantico['char']['int']['<>'] = 'error'

cuboSemantico['char']['float']['<>'] = 'error'
cuboSemantico['float']['char']['<>'] = 'error'

cuboSemantico['float']['float']['<>'] = 'bool'

cuboSemantico['char']['char']['<>'] = 'bool'

#AND

cuboSemantico['int']['int']['&'] = 'bool'
cuboSemantico['int']['float']['&'] = 'bool'
cuboSemantico['float']['int']['&'] = 'bool'

cuboSemantico['int']['char']['&'] = 'error'
cuboSemantico['char']['int']['&'] = 'error'

cuboSemantico['char']['float']['&'] = 'error'
cuboSemantico['float']['char']['&'] = 'error'

cuboSemantico['float']['float']['&'] = 'bool'

cuboSemantico['char']['char']['&'] = 'error'

#OR

cuboSemantico['int']['int']['|'] = 'bool'
cuboSemantico['int']['float']['|'] = 'bool'
cuboSemantico['float']['int']['|'] = 'bool'

cuboSemantico['int']['char']['|'] = 'error'
cuboSemantico['char']['int']['|'] = 'error'

cuboSemantico['char']['float']['|'] = 'error'
cuboSemantico['float']['char']['|'] = 'error'

cuboSemantico['float']['float']['|'] = 'bool'

cuboSemantico['char']['char']['|'] = 'error'

#EQUAL

cuboSemantico['int']['int']['='] = 'int'
cuboSemantico['int']['float']['='] = 'float'
cuboSemantico['float']['int']['='] = 'float'

cuboSemantico['int']['char']['='] = 'error'
cuboSemantico['char']['int']['='] = 'error'

cuboSemantico['char']['float']['='] = 'error'
cuboSemantico['float']['char']['='] = 'error'

cuboSemantico['float']['float']['='] = 'float'

cuboSemantico['char']['char']['='] = 'char'

#EQUAL EQUAL

cuboSemantico['int']['int']['=='] = 'bool'
cuboSemantico['int']['float']['=='] = 'bool'
cuboSemantico['float']['int']['=='] = 'bool'

cuboSemantico['int']['char']['=='] = 'error'
cuboSemantico['char']['int']['=='] = 'error'

cuboSemantico['char']['float']['=='] = 'error'
cuboSemantico['float']['char']['=='] = 'error'

cuboSemantico['float']['float']['=='] = 'bool'

cuboSemantico['char']['char']['=='] = 'bool'

def getType(left, right, operator):
    return cuboSemantico[left][right][operator]
