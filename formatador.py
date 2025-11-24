from math import *
import re
import sympy as sp

x = sp.symbols('x')

funcoes_conhecidas = {"sin", "cos", "tan", "exp", "log", "log10", "sqrt", "asin", "acos", "atan", "pow"}

def adicionar_mult_antes_de_parenteses(match):
    nome = match.group(1)
    #se o grupo 1 estiver nas funcoes reconhecidas, retorna esse grupo sem alteracoes
    if nome in funcoes_conhecidas:
        return match.group(0)
    #se nao, retorna adicioando um asterisco
    else:
        return nome + "*("

def formatar_funcao(expressao : str):
    expressao = expressao.replace("phi(x)","")
    expressao = expressao.replace("f(x)","")
    expressao = expressao.replace("y","")
    expressao = expressao.replace("f'(x)","")
    expressao = expressao.replace("y'","")
    expressao = expressao.replace("dy/dx","")
    expressao = expressao.replace("=","")
    expressao = expressao.replace("tg", "tan")
    expressao = expressao.replace("sen", "sin")
    expressao = expressao.replace("e^", "exp")
    expressao = expressao.replace("^", "**")
    expressao = re.sub(r"\blog\b", "log10", expressao)
    expressao = expressao.replace("ln", "log")
    
    expressao = expressao.replace("xexp", "x*exp") #repetir isso para todas as funcoes conhecidas
    expressao = expressao.replace("xsin", "x*sin")
    expressao = expressao.replace("xcos", "x*cos")
    expressao = expressao.replace("xtan", "x*tan")
    expressao = expressao.replace("xsqrt", "x*sqrt")
    expressao = expressao.replace("xlog", "x*log")
    expressao = expressao.replace("xsqrt", "x*sqrt")
    expressao = expressao.replace("xasin", "x*asin")
    expressao = expressao.replace("xacos", "x*acos")
    expressao = expressao.replace("xatan", "x*atan")
    expressao = expressao.replace("xpow", "x*pow")



    #\blog\b é o padrao que procuramos, um log que esta entre limitadores de palavras (espacos, parenteses etc)
    #substituimos por log10
    
    expressao = expressao.replace("log10", "LOGDEZ") 
    expressao = re.sub(r"(\d)([a-zA-Z\(])", r"\1*\2", expressao) #ERRO AQUI
    expressao = expressao.replace("LOGDEZ", "log10") 
    #procuramos por um agrupamento de numeros seguidos por um agrupamento de caracteres ou parenteses
    expressao = re.sub(r"(\))\s*([a-zA-Z0-9\(])", r"\1*\2", expressao)
    #caso de (x-1)(x+1) ou (x)3 - fechamento de parenteses seguido por outra expressao, com verificacao de espaços 
    padrao_mult = r"([a-zA-Z0-9]+)(\()"
    #padrao de variavel/numero (group 1) seguido por abertura de parenteses
    expressao = re.sub(padrao_mult, adicionar_mult_antes_de_parenteses, expressao)
    #aqui é o caso de um numero/variavel multiplicando algo nos parenteses, o padrao_funcao garente que a
    #verificacao nao ocorrera caso seja encontrado alguma daquelas funcoes antes de uma abertura de parenteses
   
    expressao = re.sub(r"(\bexp)(-?\w+(?:\.\w+)?(?:\*\*[+\-]?\w+)?)", r"\1(\2)", expressao)
    #procuro um exp que nao esteja no meio de uma palavra, o capturo, e depois procuro: um sinal opcional, seguido
    #por um ou mais numeros/variaveis seguido por uma parte decimal opcional, seguido por mais um ** com sinal opcional

    
    expressao = expressao.replace(" ", "")

    return expressao
