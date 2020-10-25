# Proyecto final de compiladores :computer:
Este repositorio, contiene el codigo que conforma el proyecto final de la
clase de compiladores. La finalidad de este proyecto, es construir un compilador
basado en **Python** el cual sea capaz de recibir un *input grafico* desde una
interfaz grafica en la cual un usuario puede crear codigo mediante la manipulacion
de bloques y organizarlos de acuerdo a la sintaxis propuesta del lenguaje (lenguaje
patito++).

Asimismo, este proyecto se subdivide en dos proyectos que juntos conforman un solo
proyecto final.

Los dos subproyectos estan divididos en:
- Elaboracion del compilador en **python** utilizando *lex & yacc*
- Elaboracion del input grafico, acoplandolo con el compilador mencionado
anteriomente

El equipo esta conformado por:
- Alban Aguilar Campos
- Jorge Arturo Ramirez

## Avance 1

###### Scanner y parser

El primer avance del proyecto, consistio en realizar:
- Analisis de lexico (scanner)
- Analisis de sintaxis (parser)

La herramienta utilizada para este proyecto fue **lex & yacc** dado que estaremos
utilizando el lenguaje de programacion *Python* para realizar el compilador.

De esta manera, el primer avance resulto tener una implementacion exitosa al momento
de probarlo y por lo tanto el primer avance resulto en una version estable del proyecto
hasta ahora.

Las tareas a desarrollar fueron las siguientes:
- Investigar como implementar **lex & yacc**
- Implementar el scanner (lex)
- Implementar el parser (yacc)

Una vez terminadas las tareas, proseguimos a corroborar que el scanner y el parser
estuvieran bien implementados de acuerdo a nuestra definicion de terminado:
- [x] Lex & Yacc fue implementado de manera correcta
- [x] El archivo de prueba contiene la sintaxis correcta propuesta por el equipo
- [x] El main corre de manera exitosa

## Avance 2

###### Tablas de variables/funciones y cubo semantico

El segundo avance, consistio en realizar las tablas de variables/funciones asi como
el cubo semantico del proyecto. Este avance, da un preambulo para poder empezar a
entender como funcionan las operaciones aritmeticas, logicas y comparaciones que se
hacen en un programa del **lenguaje patito++** asi como entender como se relacionan
las tablas de variables/funciones con los accesos de atributos y los parametros utilizados
por las funciones.

Este segundo avance consistio en desarrollar los siguientes bloques:
- Table de variables
- Tabla de funciones
- Cubo semantico

La **tabla de variables/funciones** es necesaria para poder almacenar la informacion acerca
de las distintas entidades como lo son los nombres de las variables, nombres de funciones,
objetocs, clases, interfaces, etc. La tabla de variables es utilizada tanto para el analisis
como para la sintesis del compilador.

El **cubo semantico** es necesario dentro del compilador, ya que es util para realizar operaciones
aritmeticas, logicas, comparaciones y asignaciones.

Una vez terminadas las tareas, proseguimos a corroborar que tanto la tabla de variables/funciones
asi como el cubo semantico estuvieran bien implementados y de acuerdo a nuestra definicion de terminado:
- [x] Tabla de variables/funciones fue implementado de manera correcta
- [x] Cubo semantico fue implementado de manera correcta
- [x] El main corre de manera exitosa

## Avance 3

###### Generacion de codigo de expresiones aritmeticas y de estatutos condicionales

El tercer avance consistio en realizar la generacion de codigo de expresiones aritmeticas y de estatutos condicionales.
Este avance estuvo relacionado con el avance anterior ya que implementamos de manera correcta las expresiones aritmeticas
(incluidas en el cubo semantico) y los estatutos condicionales (incluidos en las tablas de expresiones). 

Este tercer avance consistio en desarrollar los siguientes bloques:
- Generacion de codigo de expresiones aritmeticas
- Generacion de codigo de estatuos condicionales

En esta avance fue de vital importancia modificar las tablas de variables/funciones para poder integrar la generacion
de codigo de expresiones aritmeticas en el main. Asimismo, importamos el diccionario (cubo semantico) y realizamos
la creacion de instanciaciones de clases. 

Una vez terminadas las tareas, proseguimos a corroborar que tanto la la generacion de codigo  de expresiones aritmeticas 
(tabla de variables/funciones) y la generacion de codigo de estatutos condicionales (cubo semantico) estuvieran bien 
implementados y de acuerdo a nuestra definicion de terminado:
- [x] Generacion de codigo de expresiones aritmeticas
- [x] Generacion de codigo de estatutos condicionales
- [x] El main corre de manera exitosa
