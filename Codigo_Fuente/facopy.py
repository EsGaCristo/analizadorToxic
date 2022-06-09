from asyncio.windows_events import NULL
from queue import Empty
import re
from sys import setswitchinterval
from numpy import indices, result_type
from sympy import subresultants
import analizadorLexico as aL

id = aL.lId
# -*- coding: utf-8 -*-
def fa(contenido):
    idC = len(id)
    pc = 0
    palabras = []
    pc = contenido.count(';')
    a = 0
    s = []
    
    """while pc > 0:
        print('Jijijijja')
        while idC > 0:
            cadena = re.findall(str(id[a]), contenido)
            
            if cadena:
                print(cadena)
            a += 1
            idC -= 1
    return a
    """


    
    # Definicion del alfabeto
    Σ = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','5','(',')','>','if','{','}',';','=']

    # Declaracion de la tabla de transicionesEstados/
    #        δ(q0,x)=q1, δ(q1,'')=q1
    #        Estados     x
    #        ->q0        qf
    #          qf *     NULL
    #############################
    #Tabla logica
    #   -espacio de memoria- se conecte a otro espacio de memoria
    #   -enviar un caracter entre espacios de memoria
    #   Lista
    #   '0' = Posicion actual del nodo
    #   'x' = El dato de esa posicion
    #   '1' = El siguiente nodo
    #   Esta esla reperesentacion en python = [0,'x',1] 
    #   Estados                     
    #   q0 Posicionde me moria 0
    #   qf Posicion de memoria 1 
    #   'x' Caracter enviar de q0 a qf
    ##################################################
    # Tabla es:
    # 0     x       1
    # 1     NA      NULL
    #Transicion vacia tabla logica
    # [0,'',1]
    ###################################################
    #Tabla de transiciones
    
    #TablaT=[[0, '(', 1],[1,str(id[1]),2],[2, '>', 3],[3,'5',4],[4,')',5]]
    TablaT=[[0, '(', 1],[1,'a',2],[2, '>', 3],[3,'5',4],[4,')',5],[5,'{',6]]
    TablaW=[[0, '(', 1],[1,'a',2],[2, '>', 3],[3,'5',4],[4,')',5]]
    TablaD=[[0, 'a', 1],[1,'=',2],[2, 'b', 3]]


    #TablaT=[[0,'a',0],[1, 'x', 1]]


    #Tabla para almacenar los estado que se mueven
    TablaC = []
    #estado inicial q0 = posicion 0 de la tabla
    EI = 0
    #Estafo final qf = posicion 1 de la tabla 
    EF=[5]
    #Estado actual
    EA = EI
    
    cadena = contenido
    
    #cadena de caracteres del alfabeto
    '''print ("Inserta la cadena a evaluar")
    cadena = input()
    '''
    


    def tablas(Table,TablaCop,EF,EA,cadena):
        subresultado = ""
        result = ""
        #Utilizar una bandera para revisar que (x ϵ Σ)
        bandera = True
        print("\n"+cadena)

        for caracter in cadena:
            #print (caracter)
            result= result+caracter+" "
            #verificar que el caracter pertenezca a el Σ = ['x']
            if caracter in Σ:

                if caracter == '{':
                    indices_c = cadena.index('{')
                    #indices_h = cadena.index()
                    subcadena = cadena[indices_c+1:len(cadena)]
                    if subcadena != "":
                        subresultado= "\n =============================\n"+casos(subcadena)
                        break
                elif caracter == ';':
                    indices_c = cadena.index(';')     
                    subcadena = cadena[indices_c+1:len(cadena)]
                    if subcadena != "":
                        subresultado= "\n =============================\n"+casos(subcadena)
                        break
  
                     
                
                #print ("El carcacter (car ϵ Σ) ")
                #result= result+"El carcacter (car ϵ Σ) "+"\n"
                #Buscar en la tabla el caracter TablaT
                for f in Table:
                    #Recorrer las transiciones de la tabla
                    #Indicar el estado actual y el estado final
                    if caracter in f and EA in f:
                        #Agregar elementos a la tabla comparativa TablaC
                        TablaCop.append([EA,caracter,f[2]])  
                        #actualizar el estado
                        EA=f[2]
                        #print ("Estado actual es : " + str(EA))
                        result = result+"Estado actual es : " + str(EA)+"\n"
                        
            else:
                #print("Cadena no pertenece al alfabeto")
                result+="Cadena no pertenece al alfabeto \n"
                bandera = False
                #Comparar si el estado actual es igual al estafo final
        if EA in EF and (bandera == True):
            result+=("------------------------------\n")
            result+=("Es valida la cadena de entrada\n")
            result+=("____Tabla de transiciones_____\n")
            for t in TablaC:
                #print (t)
                result+=str(t)+"\n"
            result+= subresultado                
        else:
            result+=("---------------------------------\n")
            result+=("NO es valida la cadena de entrada\n")
            result+=("______Tabla de transiciones______\n")
            for t in TablaC:
                #print (t)
                result+=str(t)+"\n"
            result+= subresultado    
        return result     
    """

"""
    def casos(cadenaA):
        if re.findall("if",cadenaA):
                cadenaA = cadenaA.replace("if","")
                cadenaA = cadenaA.replace("\n","")
                result = tablas(TablaT,TablaC,[6],EA,cadenaA)
                return result
        elif re.findall("whl",cadenaA):
                cadenaA = cadenaA.replace("whl","")
                cadenaA = cadenaA.replace("\n","")
                result =  tablas(TablaW,TablaC,[5],EA,cadenaA)
                return result
        else:
            result = tablas(TablaD,TablaC,[3],EA,cadenaA)
            return result        
     



    contenido = contenido.lower()
    return casos(contenido)


    
