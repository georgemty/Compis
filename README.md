#    :computer: Proyecto final de compiladores :computer:
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

El tercer avance consistio en la generacion de codigo de expresiones aritmeticas y de estatutos condicionales.
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

## Avance 4

###### Generacion de codigo de estatutos condicionales ciclicos y generacion de codigo de funciones

El cuarto avance consistio en generar el codigo para los estatutos condicionales y ciclicos asi como generar el codigo
de las funciones (cuadruplos). En este avance, implementamos de manera correcta los estatutos condicionales dentro del
main. Asimismo, realizamos la correcta implementacion de la clase 'avail' la cual nos servira para crear las variables
temporales de los cuadruplos.

Este cuarto avance consistio en desarrollar los siguientes bloques:
- Generacion de codigo de estatutos condicionales ciclicos
- Generacion de codigo de funciones

Este avance nos dio un preambulo para poder entender como implementar los cadruplos y manejar la precedencia de operaciones
de manera correcta. Asimismo, una vez implementados los cadruplos ya tenemos un preambulo para poder trabajar con el mapeo
de memoria (simulacion de memoria) en la siguiente entrega.

Una vez terminadas las tareas, proseguimos a corroborar que tanto la la generacion de codigo  de estatutos condicionales
y la generacion de codigo de funciones, estuvieran bien implementados y de acuerdo a nuestra definicion de terminado:
- [x] Generacion de codigo de estatutos condicionales
- [ ] Generacion de codigo de codigo de funciones (cuadruplos) - nos falta terminar la implementacion completa de los cuadruplos
- [x] El main corre de manera exitosa

## Avance 5

###### Mapa de memoria de ejecucion para la maquina virtual y maquina virtual: ejecucion de expresiones aritmeticas y estatutos secuenciales

El quinto avanace consistio en resolver problemas que tuvimos de la entrega anterior en cuanto a la generacion de los cuadruplos
de asignacion ya que tuvimos problemas para establecer las funciones que se encargaban de realizar el guardado de las variables/funciones en la tabla de funciones/variables de manera exitosa. Asimismo, seguiremos en la elaboracion de los cuadruplos que nos faltan para poder terminar de manera completa y exitosa todos los cuadruplos requeridos para el correcto funcionamiento del compilador.

Este quinto avance consistio en desarrollar los siguientes bloques:
- Relizar el desarrollo de los cuadruplos faltantes
- Resolver problemas de implementacion de los cuadruplos

Una vez terminadas las tareas, proseguimos a corroborar que tanto la implementacion de los cuadruplos como la resolucion de los problemas de implementacion estuvieran bien implementados y de acuerdo a nuestra definicion de terminado:

- [x] Tuvimos un avanace significativo en la generacion/implementacion de los cuadruplos
- [x] Resolvimos de manera correcta los problemas que surgieron al implementar los cuadruplos
- [x] El main corre de manera exitosa

## Avance 6

###### Generacion de codigo de arreglos/tipos estructurados y maquina virtual: ejecucion de estatutos condicionales

El sexto avanace consistio en resolver problemas que tuvimos de la entrega anterior en cuanto a la generacion de los cuadruplos
de asignacion, for y while ya que tuvimos problemas para establecer las funciones que se encargaban de realizar el guardado de las variables/funciones en la tabla de funciones/variables de manera exitosa. Asimismo, seguiremos en la elaboracion de los cuadruplos que nos faltan para poder terminar de manera completa y exitosa todos los cuadruplos requeridos para el funcionamiento correcto del compilador.

Este sexto avance consistio en desarrollar los siguientes bloques:
- Relizar el desarrollo de los cuadruplos faltantes
- Resolver problemas de implementacion de los cuadruplos

Una vez terminadas las tareas, proseguimos a corroborar que tanto la implementacion de los cuadruplos como la resolucion de los problemas de implementacion estuvieran bien implementados y de acuerdo a nuestra definicion de terminado:

- [x] Tuvimos un avanace significativo en la generacion/implementacion de los cuadruplos
- [x] Resolvimos de manera correcta los problemas que surgieron al implementar los cuadruplos
- [x] El main corre de manera exitosa

## Avance 7

###### Ejecución de Aplicación particular y Documentación parcial

El septimo avance consistio en implementar la memoria una vez terminados los cuadruplos. La creacion de la memoria fue relativamente rapida ya que los cuadruplos de nuestro codigo se estaban comportando de manera correcta. La memoria se encuentra en su propia clase y se llama al main donde se incorpora a los cuadruplos ya implementados. Una vez terminada la memoria e implementada con los cuadruplos de manera correcta se prosiguio a dejar en desarrollo la maquina virtual dado que tenemos previsto terminar la maquina virtual para antes de la entrega final. Asimismo, realizamos documentacion parcial del proyecto la cual se encuentra en esta entrega. 

Este septimo avance consistio en desarrollar los siguientes bloques:
- Relizar la implementacion de la memoria
- Incorporar la memoria en los cuadruplos anteriormente creados
- Realizar documentacion parcial del proyecto

Una vez terminadas las tareas, proseguimos a corroborar que tanto la implementacion de la memoria como la documentacion parcial estuvieran bien implementados y de acuerdo a nuestra definicion de terminado:

- [x] Creamos la memoria del compilador
- [x] Incorporamos en los cuadruplos el manejo de memoria
- [x] Documentados parcialmente el avance del proyecto
- [x] El main corre de manera exitosa
