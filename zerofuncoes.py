from math import *

funcao_compilada = ''
derivada_compilada = ''
phi_compilado = ''

def definir_expressoes(funcao, derivada, phi):
    global funcao_compilada, derivada_compilada, phi_compilado
    funcao_compilada = funcao
    derivada_compilada = derivada
    phi_compilado = phi

def f(x):
    return eval(funcao_compilada)
    #return exp(-x**2) - cos(x)
def derivada_f(x):
    return eval(derivada_compilada)
def phi(x):
    return eval(phi_compilado)

def bisseccao(a,b, precisao, n):
    k = 0
    xs_bissec = []
    if(fabs(b-a) < precisao):
        raiz = a
        xs_bissec.append(a)
    else:
        while(fabs(b-a) > precisao and k < n):
            k = k+1
            finicio = f(a)
            meio = (a+b)/2
            fmeio = f(meio)
            if(fmeio * finicio < 0):
                b = meio
            else:
                a = meio
            xs_bissec.append(a)
        raiz = a
    print('\n',"Raiz de f(x) = ", raiz)
    print('\n',"Iteracoes = ", k)
    if k == n:
        xs_bissec.append("NUM MAX DE ITERACOES ATINGIDO")
    return xs_bissec

def mil(x,precisao, n):
    xs_mil = []
    k = 0
    x_ant = x
    if(fabs(f(x)) < precisao):
        raiz = x
        xs_mil.append(x)
    else:
        while(fabs(f(x)) > precisao or fabs(x_ant-x) > precisao and k < n):
            x_ant = x
            x = phi(x)
            k+= 1
            xs_mil.append(x)
    raiz = x
    print('\n',"Raiz de f(x) = ", raiz)
    print('\n',"Iteracoes = ", k) 
    if k == n:
        xs_mil.append("NUM MAX DE ITERACOES ATINGIDO")
    return xs_mil
         
def newton(x0, precisao, n):
    xs_newton = []
    k = 0
    f_de_x = f(x0)
    if(fabs(f_de_x) < precisao):
        raiz = x0
        xs_newton.append(x0)
    else:
        f_de_x_linha = derivada_f(x0)
        x1 = x0 - (f_de_x/f_de_x_linha)
        f_de_x = f(x1)
        k += 1
        xs_newton.append(x1)
        while((fabs(f_de_x) > precisao or fabs(x1 - x0) > precisao) and k < n):
            k += 1
            x0 = x1
            f_de_x = f(x0)
            f_de_x_linha = derivada_f(x0)
            x1 = x0 - (f_de_x/f_de_x_linha)
            xs_newton.append(x1)
        raiz = x1
    print('\n',"Raiz de f(x) = ", raiz)
    print('\n',"Iteracoes = ", k)   
    if k == n:
        xs_newton.append("NUM MAX DE ITERACOES ATINGIDO")
    return xs_newton
               
def secante(x0, x1, precisao, n):
    k= 0
    xs_secante = []
    if(fabs(f(x0)) < precisao):
        raiz = x0
        xs_secante.append(x0)
    elif(fabs(f(x1)) < precisao):
        raiz = x1
        xs_secante.append(x1)
    else:
        while True:
            k += 1
            x2 = x1 - ((f(x1)*(x1-x0))/(f(x1)- f(x0)))
            x0 = x1
            x1 = x2
            xs_secante.append(x2)
            if(fabs(f(x2)) < precisao or k >= n):
                raiz = x2
                break
    print(f"Raiz de f(x) = {raiz}")
    print(f"Numero de iteracoes: {k}")
    if k == n:
        xs_secante.append("NUM MAX DE ITERACOES ATINGIDO")
    return xs_secante

def regulaFalsi(a, b, precisao, n):
    xs_regulaFalsi = []
    k = 0
    if(fabs(b-a) < precisao):
        raiz = a
        xs_regulaFalsi.append(a)
    elif (fabs(f(a)) < precisao):
        raiz = a
        xs_regulaFalsi.append(a)
    elif (fabs(f(b)) < precisao):
        raiz = b
        xs_regulaFalsi.append(b)
    else:
        while True:
            k += 1
            numerador = (a*f(b)) - (b*f(a))
            denominador = f(b) - f(a)
            x = numerador/denominador
            m = f(a)
            xs_regulaFalsi.append(x)
            if(fabs(f(x)) < precisao or k > n):
                raiz = x
                break
            if(m*f(x) > 0):
                a = x
            else:
                b = x
            if(fabs(b-a) < precisao):
                raiz = x
                break
    print(f"Raiz de f(x) = {raiz}")
    print(f"Numero de iteracoes: {k}")
    if k == n:
        xs_regulaFalsi.append("NUM MAX DE ITERACOES ATINGIDO")
    return xs_regulaFalsi
                    
            
  
