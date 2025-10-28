import numpy as np

def eliminacao_gauss(matrizA : np.ndarray, matrizB : np.ndarray):
    if(np.linalg.det(matrizA) == 0):
        return "matriz sem solucao"
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
    if(np.linalg.det(matrizA) == 0):
        return "matriz sem solucao"
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
    if(np.linalg.det(matrizA) == 0):
        return "matriz sem solucao"
    n = len(matrizA)
    x = np.zeros(n)
    matrizAumentada = np.column_stack((matrizA, matrizB)) #concatena a matrizB em A como uma coluna
    matrizAumentada = matrizAumentada.astype(float) # se certificando q a nova matriz é do tipo float
    trocaColunas = np.arange(n)
    #zerar elementos abaixo da diagonal principal
    for i in range(n): #LEMBRANDO N É O TAMANHO DA MATRIZ A (POR ISSO PODEMOS USAR A MATRIZ AUMENTADA SEM SE PREOCUPAR COM ACESSAR B)
        linha_pivo = i
        coluna_pivo = i
        valor_max = abs(matrizAumentada[i][i])
        for j in range (i, n):
            for k in range(i, n):
                if abs(matrizAumentada[j][k]) > valor_max:
                    linha_pivo = j
                    coluna_pivo = k
                    valor_max = abs(matrizAumentada[j][k])
        if linha_pivo != i: #se o pivo estiver em uma linha diferente da diag principal atual, temos que trocar de linhas
            aux = matrizAumentada[i].copy()
            matrizAumentada[i] = matrizAumentada[linha_pivo].copy()
            matrizAumentada[linha_pivo] = aux
        if coluna_pivo != i: #se o pivo estiver em uma linha diferente da diag principal atual, temos que trocar de linhas
            matrizAumentada[:, [i, coluna_pivo]] = matrizAumentada[:, [coluna_pivo, i]]
            trocaColunas[[i, coluna_pivo]] = trocaColunas[[coluna_pivo, i]]
        
        pivo = matrizAumentada[i][i] #pivo vai ser o elemento da diag principal apos pivoteamento
        if pivo == 0.0:
            return "Divisao por 0"
        for j in range(i+1, n):
            multiplicador =  matrizAumentada[j][i] / pivo 
            matrizAumentada[j] = matrizAumentada[j] - multiplicador * matrizAumentada[i]
        print(matrizAumentada)

    for i in range(n-1, -1, -1): #comeca em n-1 e vai ate -1 subtraindo
        soma = matrizAumentada[i][-1] #ultimo elementro da linha i (elementro de b)
        for j in range(i+1, n):
            soma = soma - (matrizAumentada[i][j] *x[j])
        x[i] = soma / matrizAumentada[i][i]
    
    x_final = np.zeros_like(x)
    for i in range(n):
        x_final[trocaColunas[i]] = x[i]
    
    return x_final

def eliminacao_LU(matrizA : np.ndarray, matrizB : np.ndarray):
    #matrizA = matrizA.astype(float)
    if(np.linalg.det(matrizA) == 0):
        return "matriz sem solucao"
    n = len(matrizA)
    x = np.zeros(n)
    matrizL = np.zeros((n,n), dtype=float)
    for i in range(n):
        matrizL[i][i] = 1.0
    #zerar elementos abaixo da diagonal principal
    for i in range(n):
        pivo = matrizA[i][i] #pivo vai ser o elemento da diag principal
        if pivo == 0.0:
            return "Divisao por 0"
        for j in range(i+1, n):
            multiplicador =  matrizA[j][i] / pivo 
            matrizA[j] = matrizA[j] - multiplicador * matrizA[i]
            matrizL[j][i] = multiplicador
    y = np.zeros(n)
    for i in range(n):
        soma = matrizB[i]
        for j in range(i): #j deve ir apenas ate i, para nao acessar y's nao calculados
            soma -= matrizL[i][j] * y[j]
        y[i] = soma / matrizL[i][i]
    for i in range(n-1,-1,-1):
        soma = y[i]
        for j in range(i+1, n): #j deve ir apenas ate i, para nao acessar y's nao calculados
            soma -= matrizA[i][j] * x[j] #matrizA é U
        x[i] = soma / matrizA[i][i]
    
    return x

def det_submatrizes(matrizA : np.ndarray):
    n = matrizA.shape[0]
    lista_dets = []
    for i in range(1, n + 1):
        submatriz = matrizA[0:i , 0:i]
        lista_dets.append(np.linalg.det(submatriz))
    return lista_dets

A = np.array([
    [3, 2, 4],
    [1, 1, 2],
    [4, 3, -2]
], dtype=float)

B = np.array([1, 2, 3])
print(eliminacao_LU(A,B))
'''

x = eliminacao_gauss(A, B)
x2 = pivoteamento_parcial(A, B)
print(x2)   '''

