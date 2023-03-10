# ------------------------------------------------------------
# TPC1: Intervalos (definição léxica)
# 
# ------------------------------------------------------------
import ply.lex as lex
import sys

# List of token names.   This is always required
tokens = ['NUM']

# Literals
literals = ['+', '-', '[', ']', ',']

# A regular expression rule with some action code
def t_NUM(t):
    r'-?\d+'
    t.value = int(t.value)    
    return t

#----------------------------------------------------
# Define a rule so we can track line numbers


# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t\n'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
    
#-------------------------------------------------------------- 
# Build the lexer
lexer = lex.lex()

# data = '+[100,200][3,12]'

# lexer.input(data)

# while True:
#    tok = lexer.token()
#    if not tok: break      # No more input
#    print(tok)