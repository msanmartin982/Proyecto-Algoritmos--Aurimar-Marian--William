'''
Validación de entrada, con el fin de continuar o no un ciclo.
'''
def valid_continue(msg):
    while True:
        ans = input(msg)
        if ans != 'y' and ans != 'n':
            print("Error, escriba 'y' o 'n' para continuar.")
        else:
            return ans
