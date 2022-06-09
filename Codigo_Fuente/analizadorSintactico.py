from asyncio.windows_events import NULL
import codecs
import ply.yacc as yacc
import os
import codecs
import re
from analizadorLexico import tokens
from sys import stdin

list

# Variable que permite guardar una bitacora de lo que se va ejecutando
global resultado
resultado = []


# para errores que tengamos en nuestro analizador
# de tipo reduce
precedencias = (
    ('right', 'EQL'),
    ('right', 'WHL'),
    ('right', 'IF'),
    ('right', 'EQL_SUM'),
    ('right', 'EQL_SUB'),
    ('right', 'EQL_DIV'),
    ('right', 'EQL_MULT'),
    ('right', 'DIF'),
    ('right', 'SML'),
    ('right', 'GTR'),
    ('right', 'SMLE'),
    ('right', 'GRTE'),
    ('left', 'ADD'),
    ('left', 'SUBST'),
    ('left', 'MULT'),
    ('left', 'DIV'),

)


# Terminales son aquellos tokens que definimos

def p_program(p):
    '''program : block'''


def p_block(p):
    '''block : declaracion
             | While
             | condicional'''


def p_declaracionEmpty(t):
    'declaracion : empty'


def p_declaracion(t):
    'declaracion : asignacion ENDST'


def p_asignacion1(t):
    'asignacion : IDF EQL expresion'

    resultado.append("declaracion" + '\n')


def p_asignacion2(t):
    'asignacion : asignacion ENDST IDF EQL expresion ENDST'
    resultado.append("declaracion" + '\n')


def p_bucle(t):
    '''While : WHL OPRT expresion CPRT OKEY expresion CKEY'''
    resultado.append("Bucle While" + '\n')


def p_expresion_numero(t):
    'expresion : INT'
    t[0] = t[1]


def p_expresion_Caracter(t):
    'expresion : CHR'
    t[0] = t[1]


def p_condicional(t):
    '''condicional : OPRT expresion CPRT OKEY expresion CKEY'''
    resultado.append("Condicional" + '\n')


def p_condicionalExpresion(t):
    '''condicional : OPRT expresion CPRT OKEY declaracion CKEY'''
    resultado.append("Condicional" + '\n')


def p_condicionalVacio(t):
    '''condicional : OPRT expresion CPRT OKEY empty CKEY'''
    resultado.append("Condicional vacio" + '\n')


def p_error(p):
    resultado.append("Error de sintaxis:" + str(p)),
    pass


def p_empty(p):
    '''empty :'''
    pass


def p_expresion_operaciones(t):
    '''
    expresion  :   expresion ADD expresion
                |   expresion SUBST expresion
                |   expresion MULT expresion
                |   expresion DIV expresion
    '''
    if t[2] == '+':
        t[0] = t[1] + t[3]
    elif t[2] == '-':
        t[0] = t[1] - t[3]
    elif t[2] == '*':
        t[0] = t[1] * t[3]
    elif t[2] == '/':
        t[0] = t[1] / t[3]
    elif t[2] == '%':
        t[0] = t[1] % t[3]
    elif t[2] == '**':
        i = t[3]
        t[0] = t[1]
        while i > 1:
            t[0] *= t[1]
            i -= 1
    resultado.append("expresion operacional" + '\n')


def p_expresion_logicas(t):
    '''
    expresion   :  expresion SML expresion
                |  expresion GRT expresion
                |  expresion SMLE expresion
                |   expresion GRTE expresion
                |   expresion EQL expresion
                |   expresion DIF expresion
                |  IDF SML IDF
                |  IDF GRT IDF
                |  IDF SMLE IDF
                |   IDF GRTE IDF
                |   IDF EQL IDF
                |   IDF DIF IDF
                |  OPRT expresion CPRT SML OPRT expresion CPRT
                |  OPRT expresion CPRT GRT OPRT expresion CPRT
                |  OPRT expresion CPRT SMLE OPRT expresion CPRT
                |  OPRT  expresion CPRT GRTE OPRT expresion CPRT
                |  OPRT  expresion CPRT EQL OPRT expresion CPRT
                |  OPRT  expresion CPRT DIF OPRT expresion CPRT
    '''
    if t[2] == "<":
        t[0] = t[1] < t[3]
    elif t[2] == ">":
        t[0] = t[1] > t[3]
    elif t[2] == "<=":
        t[0] = t[1] <= t[3]
    elif t[2] == ">=":
        t[0] = t[1] >= t[3]
    elif t[2] == "==":
        t[0] = t[1] is t[3]
    elif t[2] == "!=":
        t[0] = t[1] != t[3]
    elif t[3] == "<":
        t[0] = t[2] < t[4]
    elif t[2] == ">":
        t[0] = t[2] > t[4]
    elif t[3] == "<=":
        t[0] = t[2] <= t[4]
    elif t[3] == ">=":
        t[0] = t[2] >= t[4]
    elif t[3] == "==":
        t[0] = t[2] is t[4]
    elif t[3] == "!=":
        t[0] = t[2] != t[4]

    resultado.append("expresion Logica" + '\n')


# gramatica de expresiones booleanadas
def p_expresion_booleana(t):
    '''
    expresion   :   expresion AND expresion
                |   expresion OR expresion
                |   expresion NOT expresion
                |  OPRT expresion AND expresion CPRT
                |  OPRT expresion OR expresion CPRT
                |  OPRT expresion NOT expresion CPRT
    '''
    if t[2] == "&&":
        t[0] = t[1] and t[3]
    elif t[2] == "||":
        t[0] = t[1] or t[3]
    elif t[2] == "!":
        t[0] = t[1] is not t[3]
    elif t[3] == "&&":
        t[0] = t[2] and t[4]
    elif t[3] == "||":
        t[0] = t[2] or t[4]
    elif t[3] == "!":
        t[0] = t[2] is not t[4]
    resultado.append("expresion Booleana" + '\n')

def archivo(cadena):
    cadena = cadena.upper()
    parser = yacc.yacc()
    # ya no es necesario esta variable puesto que se guarda todo en resultado
    result = parser.parse(cadena)
    print(result)

    return (resultado)
