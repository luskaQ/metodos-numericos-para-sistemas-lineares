import numpy as np

def eliminacao_gauss(matrizA : np.ndarray, matrizB : np.ndarray):
    n = len(matrizA)
    x = np.zeros(n)
    matrizAumentada = np.column_stack((matrizA, matrizB)) #concatena a matrizB em A como uma coluna
    matrizAumentada = matrizAumentada.astype(float) # se certificando q a nova matriz é do tipo float
    #zerar elementos abaixo da diagonal principal
    for i in range(n):
        pivo = matrizAumentada[i][i] #pivo vai ser o elemento da diag principal
        if pivo == 0.0:
            return "Divisao por 0"
        for j in range(i+1, n):
            multiplicador =  matrizAumentada[j][i] / pivo 
            matrizAumentada[j] = matrizAumentada[j] - multiplicador * matrizAumentada[i]
        print(matrizAumentada)

    for i in range(n-1, -1, -1): #comeca em n-1 e vai ate -1 subtraindo
        soma = matrizAumentada[i][-1]
        for j in range(i+1, n):
            soma = soma - (matrizAumentada[i][j] *x[j])
        x[i] = soma / matrizAumentada[i][i]
    print(matrizAumentada)
    return x

def pivoteamento_parcial(matrizA : np.ndarray, matrizB : np.ndarray):
    n = len(matrizA)
    x = np.zeros(n)
    matrizAumentada = np.column_stack((matrizA, matrizB)) #concatena a matrizB em A como uma coluna
    matrizAumentada = matrizAumentada.astype(float) # se certificando q a nova matriz é do tipo float
    #zerar elementos abaixo da diagonal principal
    for i in range(n): #LEMBRANDO N É O TAMANHO DA MATRIZ A (POR ISSO PODEMOS USAR A MATRIZ AUMENTADA SEM SE PREOCUPAR COM ACESSAR B)
        linha_pivo = i
        valor_max = abs(matrizAumentada[i][i])
        for j in range (i+1, n):
            if abs(matrizAumentada[j][i]) > valor_max:
                linha_pivo = j
                valor_max = abs(matrizAumentada[j][i])
        if linha_pivo != i: #se o pivo estiver em uma linha diferente da diag principal atual, temos que trocar de linhas
            aux = matrizAumentada[i].copy()
            matrizAumentada[i] = matrizAumentada[linha_pivo].copy()
            matrizAumentada[linha_pivo] = aux
        
        pivo = matrizAumentada[i][i] #pivo vai ser o elemento da diag principal apos pivoteamento
        if pivo == 0.0:
            return "Divisao por 0"
        for j in range(i+1, n):
            multiplicador =  matrizAumentada[j][i] / pivo 
            matrizAumentada[j] = matrizAumentada[j] - multiplicador * matrizAumentada[i]
        print(matrizAumentada)

    for i in range(n-1, -1, -1): #comeca em n-1 e vai ate -1 subtraindo
        soma = matrizAumentada[i][-1]
        for j in range(i+1, n):
            soma = soma - (matrizAumentada[i][j] *x[j])
        x[i] = soma / matrizAumentada[i][i]
    
    return x    

def pivoteamento_completo(matrizA : np.ndarray, matrizB : np.ndarray):
    
    return

def det_submatrizes(matrizA : np.ndarray):
    n = matrizA.shape[0]
    lista_dets = []
    for i in range(1, n + 1):
        submatriz = matrizA[0:i , 0:i]
        lista_dets.append(np.linalg.det(submatriz))
    return lista_dets


'''A = np.array([
    [3, 2, 4],
    [1, 1, 2],
    [4, 3, -2]
])

B = np.array([1, 2, 3])

x = eliminacao_gauss(A, B)
x2 = pivoteamento_parcial(A, B)
print(x2)   '''

