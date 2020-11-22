class Memory:
    def __init__(self):
        #DICCIONARIOS PARA VARIABLES
        self.globales = {}
        self.constants = {}
        self.locales = {}
        self.temporal = {}
        self.operators = {
            '+' : 1,
            '-' : 2,
             '*' : 3,
             '/' : 4,
             '<' : 5,
             '>' : 6,
             '<=' : 7,
             '>=' : 8,
             '==' : 9,
             '!=' : 10,
             '&&' : 11,
             '|' : 12,
             '=' : 13,
             'for' : 14,
             'while' : 15,
             'read' : 16,
             'print' : 17,
             'GOTO' : 18,
             'GOTOF' : 19,
             'GOTOV' : 20,
             'ERA' : 21,
             'GOSUB' : 22,
             'return': 23,
             'ENDPROC' : 24,
             'VER': 25,
             'END': 26,
            }

        #GLOBALES
        self.gi = 1000 #lower 1000 upper 2999
        self.gf = 3000 #lower 3000 upper 4999
        self.gc = 5000 #lower 5000 upper 6999
        self.gb = 7000 #lower 7000 upper 8999

        # TEMPORALES
        self.gLi = 11000 #lower 11000 upper 12999
        self.gLf = 13000 #lower 13000 upper 14999
        self.gLc = 15000 #lower 15000 upper 16999
        self.gLb = 17000 #lower 17000 upper 18999


        # LOCALES
        self.li = 23000 #lower 23000 upper 25999
        self.lf = 26000 #lower 26000 upper 28999
        self.lc = 29000 #lower 29000 upper 30999
        self.lb = 31000 #lower 31000 upper 32999

        # CONSTANTES
        self.ctei = 45000 #lower 45000 upper 45999
        self.ctef = 46000 #lower 46000 upper 46999
        self.ctec = 47000 #lower 47000 upper 47999
        self.cteString = 48000 #lower 48000 upper 48999

        # FUNCIONES EJECUCION
    def value_to_memory(self, address, value):
        if address >= 1000 and address < 9000:
            if address < 3000:
                self.globales[address] = value

            elif address < 5000:
                self.globales[address] = value

            elif address < 7000:
                self.globales[address] = value

            else:
                self.globales[address] = value


        elif address >= 23000 and address <= 31000:
            if address < 26000 and address >= 23000:
                self.locales[address] = value

            elif address < 29000 and address >=26000:
                self.locales[address] = value

            elif address < 31000 and address >= 29000:
                self.locales[address] = value

            elif address < 33000 and address >= 31000:
                self.locales[address] = value

            else:
                print("index out of range")

        elif address >= 45000 and address <49000:
            if address < 46000:
                self.constants[address] = value
            elif address <47000:
                self.constants[address] = value
            elif address <48000:
                self.constants[address] = value
            elif address <49000:
                self.constants[address] = value
            else:
                print("index out of range")
        else:
            if address < 19000 and address >= 11000:
                if address < 13000 and address >= 11000:
                    self.temporal[address] = value

                elif address < 15000 and address >= 13000:
                    self.temporal[address] = value


                elif address < 17000 and address >= 15000:
                    self.temporal[address] = value


                elif address < 19000 and address >= 17000:
                    self.temporal[address] = value

                else:
                    print("Out of range")


    def value_from_memory(self, address):
        if address < 9000:
            if address < 3000 and address >= 1000:
                 return self.globales[address]

            elif address < 5000 and address >= 3000:
                return self.globales[address]

            elif address < 7000 and address >= 5000:
                return self.globales[address]

            elif address < 9000 and address >= 7000:
                return self.globales[address]
            else:
                print ("index ouf range")


        elif address >= 23000 and address < 33000:

            if address < 26000 and address >= 23000:
                if address in self.locales:
                    return self.locales[address]

            elif address < 29000 and address >= 26000:
                return self.locales[address]

            elif address < 31000 and address >= 29000:
                return self.locales[address]

            elif address < 33000 and address >= 31000:
                return self.locales[address]

            else:
                print("index out of range")

        elif address < 49000 and address >=45000:
            if address <46000:
                return self.constants[address]

            elif address <47000:
                return self.constants[address]

            elif address <48000:
                return self.constants[address]

            elif address < 49000:
                return self.constants[address]

            else:
                print("index out of range")

        else:
            if address < 13000:
                    return self.temporal[address]

            elif address < 15000:
                    return self.temporal[address]

            elif address < 17000:
                    return self.temporal[address]

            elif address < 19000:
                    return self.temporal[address]
            else:
                print("index ouf of range")


    # FUNCIONES COMPILACION

    def set_var_direction(self, tipo, id, funId):
        #VARIABLES GLOBALES
        if funId == 'programa':
            if tipo == 'int':
                if self.gi <3000:
                    address = self.gi
                    # print("se ha configurado la var", id, "global, la direccion es:", address)
                    self.gi += 1
                    #print("address actualizada a ", self.gi)
                else:
                    print("index out of range")

            elif tipo == 'float':
                if self.gf < 5000:
                    address = self.gf
                    # print("se ha configurado la var", id, "global, la direccion es:", address)
                    self.gf += 1
                    #print("address actualizada a ", self.gf)

                else:
                    print("index out of range")

            elif tipo == 'char':
                if self.gc < 7000:
                    address = self.gc
                    self.gc += 1
                else:
                    print("index out of range")

            else:
                if self.gb < 9000:
                    address = self.gb
                    self.gb += 1


        else:
            if tipo == 'int':

                if self.li <26000:
                    address = self.li
                    # print("se ha configurado la var", id, "Local, la direccion es:", address)
                    self.li += 1
                    #print("address actualizada a ", self.li)
                else:
                    print("index out of range")

            elif tipo == 'float':
                if self.lf < 29000:
                    address = self.lf
                    # print("se ha configurado la var", id, "local, la direccion es:", address)
                    self.lf += 1
                    #print("address actualizada a ", self.lf)

                else:
                    print("index out of range")

            elif tipo == 'char':
                if self.lc < 31000:
                    address = self.lc
                    # print("se ha configurado la var", id, "local, la direccion es:", address)
                    self.lc += 1
                    #print("address actualizada a ", self.lc)

                else:
                    print("index out of range")

            else:
                if self.lb < 33000:
                    address = self.lb
                    #print("se ha configurado la var", id, "local, la direccion es:", address)
                    self.lb += 1
                    #print("address actualizada a ", self.lb)

        return address

    def set_temp_direction(self, tipo, id, funId):
        if tipo == 'int':
            if self.gLi <13000:
                address = self.gLi
                #print("adress", address)
                self.gLi += 1
                #print("address actualizada a ", self.li)
            else:
                    print("index out of range")

        elif tipo == 'float':
           if self.gLf < 15000:
               address = self.gLf
               self.gLf += 1
           else:
                print("index out of range")

        elif tipo == 'char':
            if self.gLc < 17000:
                address = self.gLc
                #print("se ha configurado la var", id, "local, la direccion es:", address)
                self.gLc += 1
                #print("address actualizada a ", self.lc)
            else:
                print("index out of range")

        else:
            if self.gLb < 20000:
                address = self.gLb
                #print("se ha configurado la var", id, "local, la direccion es:", address)
                self.gLb += 1
                #print("address actualizada a ", self.lb)
        return address


     # CONSTANTES

    def set_cte(self, val):
        if isinstance(val, int):
            if(self.ctei < 46000):
                address = self.ctei
                self.ctei += 1


        elif isinstance(val, float):
            if self.ctef < 47000:
                address = self.ctef
                #print("constante flotante se ha configurado con dir",val, address)
                self.ctef += 1
                #print("constante flotante updated ", self.ctef)

        elif isinstance(val, str):
            if len(val)<2:
                if self.ctec < 48000:
                    address = self.cteString
                    #print("constante char se ha configurado con dir ",val ,address)
                    self.ctec += 1
                    #print("constante char updated ", self.ctec)
            else:
                if self.cteString < 49000:
                    address = self.cteString
                    #print("constante string se ha configurado con dir ",val, address)
                    self.cteString += 1
                    #print("constante string updated ", self.cteString)
        return address

    def set_var_address(self, tipo, vid, funId):
        if self.get_var_address(vid) == -1:
            ad = self.set_var_direction(tipo, vid, funId)
            self.locales[vid] = {
                'address': ad
            }

    def get_var_address(self, temp):
        if temp in self.locales.keys():
            return self.locales[temp]['address']
        else:
            return -1

    def set_temp_address(self, tipo, vid, funId):
        if self.get_temp_address(vid) == -1:
            ad = self.set_temp_direction(tipo, vid, funId)
            self.temporal[vid] = {
                'address': ad
            }

    def get_temp_address(self, temp):
        if temp in self.temporal.keys():
            return self.temporal[temp]['address']
        else:
            return -1



    def set_cte_address(self, val):
        #asigna una direccion de memoria para agregar al diccionario de ctes
        if self.get_cte_address(val) == -1:
            ad = self.set_cte(val)
            self.constants[val] = {
            'address': ad
            }


    def get_cte_address (self, val):
        if val in self.constants.keys():
            return self.constants[val]["address"]
        else:
            return -1

    def get_operator_address(self, op):
        if op in self.operators.keys():
            return self.operators[op]


    def reset_temp_vals(self):
        self.li = 23000
        self.lf = 26000
        self.lc = 29000
        self.lb = 31000
