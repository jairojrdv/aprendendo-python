'''Faça uma função que, dado um número inteiro X passado como paramêtro, retorna a string "X é positivo" caso X seja um número positivo, e "X não é positivo" caso contrário'''
def verifica_positivo(x):
    if x > 0:
        return f"{x} é positivo"
    else:
        return f"{x} não é positivo"
       
print(verifica_positivo(10))  # Saída: "10 é positivo"
print(verifica_positivo(-5))  # Saída: "-5 não é positivo"