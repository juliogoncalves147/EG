# ------------------------------------------------------------
# TPC1 : Intervalos (definição sintática)
#  + [100,200][3,12]
#  + [-4,-2][1,2][3,5][7,10][12,14][15,19]
#  - [19,15][12,6][-1,-3]
#  - [1000,200][30,12]
#   
#    sequencia : sentido intervalos
#   
#    sentido :  '+'
#            |  '-'
#    
#    intervalos : intervalo
#               | intervalos intervalo
#
#    intervalo : '[' NUM ',' NUM ']'
#
#
#   Se a frase de entrada estiver correta, pretende-se saber:
#       - o número de intervalos;
#       - o comprimento de cada Intervalo (Lsup-Linf); Diferença entre elementos - Intervalo
#       - o intervalo mais longo e o mais curto;  Guardar stats dos intervalos - Mais largo, mais curto
#       - a amplitude da sequência, considerando-a como a diferença (em valor absoluto) entre o limite superior do último intervalo e o limite inferior do 1º intervalo. Diferença final - Inicial
# ------------------------------------------------------------
import sys
import ply.yacc as yacc
from intervalos_lex import tokens


def semanticaCorrecta(intervalos):
    if parser.crescente:
        for i in range(1, len(intervalos)):
            if intervalos[i][0] < intervalos[i-1][1]:
                return False
            if intervalos[i][0] > intervalos[i][1]:
                return False
            if i == 1:
                if intervalos[i-1][0] > intervalos[i-1][1]:
                    return False
    else:
        for i in range(1, len(intervalos)):
            if intervalos[i][1] > intervalos[i-1][0]:
                return False
            if intervalos[i][0] < intervalos[i][1]:
                return False
            if i == 1:
                if intervalos[i-1][0] < intervalos[i-1][1]:
                    return False
            
    return True


def calcNumeroIntervalos(intervalos):
    return len(intervalos)


def calcIntervalosMaisLongoCurto(intervalos):
    return max(intervalos, key=lambda x: x[2]), min(intervalos, key=lambda x: x[2])

def calcAmplitude(intervalos):
    return abs(intervalos[0][0] - intervalos[-1][1])


# The set of syntatic rules
def p_sequencia(p):
    "sequencia : sentido intervalos"
    if semanticaCorrecta(p[2]):
        print('\nSequencia correta!!!\n')
        
        numero_intervalos = calcNumeroIntervalos(p[2])
        mais_longo, mais_curto = calcIntervalosMaisLongoCurto(p[2])
        amplitude = calcAmplitude(p[2])
    
        print('Numero de intervalos: ' + str(numero_intervalos) + '\n')
        
        a = 0
        for i in p[2]:
            a = a + 1
            print('Intervalo Nº' + str(a) + ': [' + str(i[0]) + ',' + str(i[1]) + '] tem comprimento ' + str(i[2]) + '')
            
        print('\nIntervalo mais longo: [' + str(mais_longo[0]) + ',' + str(mais_longo[1]) + '] tem comprimento ' + str(mais_longo[2]) + '')
        print('Intervalo mais curto: [' + str(mais_curto[0]) + ',' + str(mais_curto[1]) + '] tem comprimento ' + str(mais_curto[2]) + '')
        
        print('\nAmplitude: ' + str(amplitude) + '\n')
    else:
        print('Sequencia incorreta!!! /!\ \n')
    
    

    
    
def p_sentidoA(p):
    "sentido : '+'"
    parser.crescente = True

    
def p_sentidoD(p):
    "sentido : '-'"
    parser.crescente = False

    
def p_intervalos_intervalo(p):
    "intervalos : intervalo"
    p[0] = p[1]


def p_intervalos_intervalos(p):
    "intervalos : intervalos intervalo"
    p[0] = p[1] + p[2]

def p_intervalo(p):
    "intervalo : '[' NUM ',' NUM ']'"
    p[0] = [[p[2],p[4], p[4] - p[2]]]
    # print(parser.intervalos)

# Syntatic Error handling rule
def p_error(p):
    print('Syntax error: ', p)
    parser.success = False

# Build the parser
parser = yacc.yacc()

# Start parsing the input text
lineCresc = "+[1,3][7,12][15,20][25,30]"
lineDecresc = "-[30,25][20,15][12,7][3,1]"

parser.parse(lineDecresc)
