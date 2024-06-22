# Código em Python de ordenação usando o método "Bubble Sort".

L = [4, 1, 1, 9, 2] # Lista a ser ordenada (Dados)
fim = 5
trocou = False 
while fim > 1:
    x=0
    while x < fim-1:        #
        if L[x] > L[x+1]:   # Efetua a troca se o elemento anterior for             trocou = True   # o posterior
            temp = L[x]     # maior que o  posterior
            L[x] = L[x+1]
            L[x+1] = temp
        x+=1    

    if not trocou:          # Encerra o código se nenhuma troca for efetuada
        break
    
    fim-=1
print(L)                    # Imprime a lista já ordenada