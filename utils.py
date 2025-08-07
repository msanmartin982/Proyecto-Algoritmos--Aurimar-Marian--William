'''
Validación de entrada, con el fin de continuar o no un ciclo.
'''
def valid_continue(msg):
    while True:
        ans = input(msg)
        if ans != 'si' and ans != 'no':
            print("Error, escriba 'si' o 'no' para continuar.")
        else:
            return ans
