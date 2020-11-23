import sys
import time
import memoria as memoria

class VirtualMachine():
    def __init__(self):
        self.quads = []
        self.iterators = []
        self.pending = []
        self.pendingDirection = []
        self.memoria = memoria.Memory()
        self.start_time = 0
        self.ip = 0
        self.activation_record = []

    def rebuildCte(self):
        with open('constantes.txt', 'r') as cteList:
            lines = []
            for line in cteList:
                lines.append(eval(line))

            for line in lines:
                self.memoria.value_to_memory(line[1], line[0])

    def clean_quad(self):
        with open('cuadruplos.txt', 'r') as quadsList:
            quads = []
            for quad in quadsList:
                quads.append(eval(quad))
            return quads


    def reading (self, quads):
        while self.ip != len(quads):
            if quads[self.ip][0] == self.memoria.get_operator_address('+'):
                self.plus(quads[self.ip])
                self.ip += 1

            elif quads[self.ip][0] == self.memoria.get_operator_address('-'):
                self.minus(quads[self.ip])
                self.ip += 1

            elif quads[self.ip][0] == self.memoria.get_operator_address('*'):
                self.mult(quads[self.ip])
                self.ip += 1

            elif quads[self.ip][0] == self.memoria.get_operator_address('/'):
                self.division(quads[self.ip])
                self.ip += 1

            elif quads[self.ip][0] == self.memoria.get_operator_address('<'):
                self.less_equal(quads[self.ip])
                self.ip += 1

            elif quads[self.ip][0] == self.memoria.get_operator_address('>'):
                self.greater_equal(quads[self.ip])
                self.ip +=1

            elif quads[self.ip][0] == self.memoria.get_operator_address('<='):
                self.lessThan_equal(quads[self.ip])
                self.ip += 1

            elif quads[self.ip][0] == self.memoria.get_operator_address('>='):
                self.greaterThan_equal(quads[self.ip])
                self.ip += 1

            elif quads[self.ip][0] == self.memoria.get_operator_address('=='):
                self.compare(quads[self.ip])
                self.ip += 1

            elif quads[self.ip][0] == self.memoria.get_operator_address('!='):
                self.Not_Equal(quads[self.ip])
                self.ip += 1

            elif quads[self.ip][0] == self.memoria.get_operator_address('&&'):
                self.and_compare(quads[self.ip])
                self.ip += 1

            elif quads[self.ip][0] == self.memoria.get_operator_address('|'):
                self.or_compare(quads[self.ip])
                self.ip += 1

            elif quads[self.ip][0] == self.memoria.get_operator_address('='):
                self.asignacion(quads[self.ip])
                self.ip += 1

            elif quads[self.ip][0] == self.memoria.get_operator_address('read'):
                self.inputOP(quads[self.ip])
                self.ip += 1

            elif quads[self.ip][0] == self.memoria.get_operator_address('print'):
                self.printing(quads[self.ip])
                self.ip += 1

            elif quads[self.ip][0] == 'GOTO':
                self.goto(quads[self.ip])

            elif quads[self.ip][0] == 'GOTOF':
                self.gotof(quads[self.ip])

            elif quads[self.ip][0] == 'GOTOV':
                self.gotov(quads[self.ip])

            elif quads[self.ip][0] == 'GOSUB':
                self.goto(quads[self.ip])

            elif quads[self.ip][0] == 'ERA':
                self.era(quads[self.ip])

            elif quads[self.ip][0] == 'ENDFUNC':
                self.goto(quads[self.ip])

            elif quads[self.ip][0] == 'GOTOMAIN':
                self.gotomain(quads[self.ip])

            elif quads[self.ip][0] == 'PARAM':
                print('ENTRO A PARAM en VM', quads[2])
                self.param(quads[self.ip])
            else:
                sys.exit()

    #----------------------------------------------OPERADORES LOGICOS Y DE COMPARACION---------------------------
    def greater_equal(self, quad):
        if self.memoria.value_from_memory(quad[1]) > self.memoria.value_from_memory(quad[2]):
            self.memoria.value_to_memory(quad[3], True)

        else:
            self.memoria.value_to_memory(quad[3], False)

    def less_equal(self, quad):
        if self.memoria.value_from_memory(quad[1]) < self.memoria.value_from_memory(quad[2]):
            self.memoria.value_to_memory(quad[3], True)
        else:
            self.memoria.value_to_memory(quad[3], False)


    def greaterThan_equal(self, quad):
        if self.memoria.value_from_memory(quad[1]) >= self.memoria.value_from_memory(quad[2]):
            self.memoria.value_to_memory(quad[3], True)
        else:
            self.memoria.value_to_memory(quad[3], False)


    def lessThan_equal(self, quad):
        if self.memoria.value_from_memory(quad[1]) <= self.memoria.value_from_memory(quad[2]):
            self.memoria.value_to_memory(quad[3], True)
        else:
            self.memoria.value_to_memory(quad[3], False)


    def Not_Equal(self, quad):
        if self.memoria.value_from_memory(quad[1]) != self.memoria.value_from_memory(quad[2]):
            self.memoria.value_to_memory(quad[3], True)
        else:
            self.memoria.value_to_memory(quad[3], False)


    def compare(self, quad):
        if self.memoria.value_from_memory(quad[1]) == self.memoria.value_from_memory(quad[2]):
            self.memoria.value_to_memory(quad[3], True)
        else:
            self.memoria.value_to_memory(quad[3], False)


    def and_compare(self, quad):
        if self.memoria.value_from_memory(quad[1]) and self.memoria.value_from_memory(quad[2]):
            self.memoria.value_to_memory(quad[3], True)
        else:
            self.memoria.value_to_memory(quad[3], False)


    def or_compare(self, quad):
        if self.memoria.value_from_memory(quad[1]) or self.memoria.value_from_memory(quad[2]):
            self.memoria.value_to_memory(quad[3], True)
        else:
            self.memoria.value_to_memory(quad[3], False)


    #----------------------------------------------PRINT OPERADOR---------------------------
    def printing(self, quad):
        if isinstance(quad[1], str):
            print(quad[1])
        else:
            print(self.memoria.value_from_memory(quad[3]))

    #----------------------------------------------INPUT DE OPERADOR---------------------------
    def inputOP(self, quad):
        inputVM = input()
        if inputVM.isdigit():
            self.memoria.value_to_memory(quad[3], int(inputVM))

        elif inputVM.replace('.','',1).isdigit():
            self.memoria.value_to_memory(quad[3], float(inputVM))

        else:
            self.memoria.value_to_memory(quad[3], inputVM)



    #----------------------------------------------OPERADORES ARITMETICOS---------------------------
    def mult (self, quad):
        temp = self.memoria.value_from_memory(quad[1]) * self.memoria.value_from_memory(quad[2])
        self.memoria.value_to_memory(quad[3], temp)

    def division (self, quad):
        temp = self.memoria.value_from_memory(quad[1]) / self.memoria.value_from_memory(quad[2])
        self.memoria.value_to_memory(quad[3], temp)

    def plus (self, quad):
        temp = self.memoria.value_from_memory(quad[1]) + self.memoria.value_from_memory(quad[2])
        self.memoria.value_to_memory(quad[3], temp)

    def minus (self, quad):
        temp = self.memoria.value_from_memory(quad[1]) - self.memoria.value_from_memory(quad[2])
        self.memoria.value_to_memory(quad[3], temp)

    def asignacion(self, quad):
        self.memoria.value_to_memory(quad[3], self.memoria.value_from_memory(quad[1]))


    #----------------------------------------------SALTOS-------------------------------------------
    def gotof(self, quad):
        # print ('quad3', quad[3])
        if not self.memoria.value_from_memory(quad[1]):
            self.ip = int(quad[3])
        else:
            self.ip +=1

    def goto(self, quad):
        self.ip = int(quad[3])

    def gotov(self, quad):
        if not self.memoria.value_from_memory(quad[1]):
            self.ip = int(quad[3])
        else:
            self.ip +=1
    def gotomain(self, quad):
        self.ip = int(quad[3])

    def returnV(self, quad):
        self.memoria.value_to_memory(quad[3], self.memoria.value_from_memory(quad[1]))
        self.ip +=1

    def era(self, quad):
        self.ip += 1

    def param(self, quad):
        if quad[2] == None:
            self.memoria.value_to_memory(quad[3], self.memoria.value_from_memory(quad[1]))
            self.ip +=1
