import PySimpleGUI as sg
import numpy as np
import metodosSistemasLineares as msl
import zerofuncoes as zf
import converteDf
import time
from formatador import formatar_funcao
sg.theme("DarkBlue14")

def criar_layout_inicial():
    return [
        [sg.Text("Tamanho do sistema (n x n): "), sg.Input(key="-N-", size=(5,1)), sg.Button("Gerar")],
        [sg.HorizontalSeparator()],
        [sg.Button("Sair")]
    ]

while True:
    layout_modo = [[sg.Button("Zero de funcoes")], [sg.Button("Sistemas Lineares")]]
    janela_modo = sg.Window("Calculadora de zeros de funcoes ou sistemas lineares", layout_modo)
    modo, _ = janela_modo.read()
    
    if(modo == "Sistemas Lineares"):
        janela = sg.Window("Leitor de Matrizes - Sistemas Lineares", criar_layout_inicial())
        evento, valores = janela.read()
        if evento in (sg.WIN_CLOSED, "Sair"):
            janela.close()

        if evento == "Gerar":
            try:
                n = int(valores["-N-"])
                if n <= 0 or n > 10:
                    sg.popup_error("Digite um número entre 1 e 10!")
                    continue
            except:
                sg.popup_error("Por favor, insira um número inteiro válido!")
                continue

            janela.close()

            layout_matriz = [[sg.Text(f"Sistema de {n} equações:")]]
            for i in range(n):
                linha = [sg.Input(size=(5,1), key=f"A-{i}-{j}") for j in range(n)]
                linha.append(sg.Text("|"))
                linha.append(sg.Input(size=(5,1), key=f"B-{i}"))
                layout_matriz.append(linha)
            layout_matriz.append([sg.Button("Resolver"), sg.Button("Voltar"), sg.Button("Sair")])

            janela = sg.Window("Matriz do Sistema", layout_matriz)

            while True:
                evento, valores = janela.read()
                if evento in (sg.WIN_CLOSED, "Sair"):
                    exit()
                if evento == "Voltar":
                    janela.close()
                    janela = sg.Window("Leitor de Matrizes - Sistemas Lineares", criar_layout_inicial())
                    break

                if evento == "Resolver":
                    try:
                        A = np.zeros((n,n), dtype=float)
                        b = np.zeros(n, dtype=float)
                        for i in range(n):
                            for j in range(n):
                                A[i][j] = float(valores[f"A-{i}-{j}"])
                            b[i] = float(valores[f"B-{i}"])
                            
                        metodo_layout = [
                            [sg.Text("Escolha o método:")],
                            [sg.Button("Eliminação de Gauss"), sg.Button("Eliminação de Gauss com pivoteamento parcial"),
                            sg.Button("Eliminação de Gauss com pivoteamento completo"),
                            sg.Button("Fatoracao LU"),
                            sg.Button("Fatoracao Cholesky"),
                            sg.Button("Gauss-Jacobi"),
                            sg.Button("Gauss-Seidel")]
                        ]
                        info_iter_layout = []
                        metodo_janela = sg.Window("Método de resolução", metodo_layout, modal=True)
                        evento_metodo, _ = metodo_janela.read()
                        metodo_janela.close()
                        n_iteracoes = -1
                        if evento_metodo == "Eliminação de Gauss":
                            inicio_tempo = time.time()
                            resultado = msl.eliminacao_gauss(A, b)
                            fim_tempo = time.time()
                        elif evento_metodo == "Eliminação de Gauss com pivoteamento parcial":
                            inicio_tempo = time.time()
                            resultado = msl.pivoteamento_parcial(A,b)
                            fim_tempo = time.time()
                        elif evento_metodo == "Eliminação de Gauss com pivoteamento completo":
                            inicio_tempo = time.time()
                            resultado = msl.pivoteamento_completo(A, b)
                            fim_tempo = time.time()
                        elif evento_metodo == "Fatoracao LU":
                            inicio_tempo = time.time()
                            resultado = msl.fatoracao_LU(A, b)
                            fim_tempo = time.time()
                        elif evento_metodo == "Fatoracao Cholesky":
                            inicio_tempo = time.time()
                            resultado = msl.fatoracao_cholesky(A, b)
                            fim_tempo = time.time()
                        elif evento_metodo == "Gauss-Jacobi":
                            info_iter_layout = [
                                [sg.Text("Vetor inicial (separe por ponto-vírgula):")],
                                [sg.Input(key='x_inicial')],
                                [sg.Text("Número máximo de iterações:")],
                                [sg.Input(key='num_max_iter')],
                                [sg.Text("Tolerância (delta):")],
                                [sg.Input(key='delta')],
                                [sg.Button("Confirmar"), sg.Button("Cancelar")]
                            ]
                            
                            janela_info = sg.Window("Informações de Iteração", info_iter_layout, modal=True)
                            evento_info, valores_info = janela_info.read()
                            janela_info.close()

                            if evento_info == "Confirmar":
                                x_inicial = [float(x) for x in valores_info['x_inicial'].split(';')]
                                num_max_iter = int(valores_info['num_max_iter'])
                                delta = float(valores_info['delta'])
                                if len(x_inicial) != len(A):
                                    sg.popup_error("x0 de tamanho diferente de A!")
                                    continue 
                                inicio_tempo = time.time()
                                resultado, n_iteracoes = msl.gauss_jacobi(A, b, x_inicial, delta, num_max_iter)
                                fim_tempo = time.time()
                        elif evento_metodo == "Gauss-Seidel":
                            info_iter_layout = [
                                [sg.Text("Vetor inicial (separe por ponto-vírgula):")],
                                [sg.Input(key='x_inicial')],
                                [sg.Text("Número máximo de iterações:")],
                                [sg.Input(key='num_max_iter')],
                                [sg.Text("Tolerância (delta):")],
                                [sg.Input(key='delta')],
                                [sg.Button("Confirmar"), sg.Button("Cancelar")]
                            ]
                            
                            janela_info = sg.Window("Informações de Iteração", info_iter_layout, modal=True)
                            evento_info, valores_info = janela_info.read()
                            janela_info.close()

                            if evento_info == "Confirmar":
                                x_inicial = [float(x) for x in valores_info['x_inicial'].split(';')]
                                num_max_iter = int(valores_info['num_max_iter'])
                                delta = float(valores_info['delta'])
                                if len(x_inicial) != len(A):
                                    sg.popup_error("x0 de tamanho diferente de A!")
                                    continue
                                inicio_tempo = time.time()
                                resultado, n_iteracoes = msl.gauss_seidel(A, b, x_inicial, delta, num_max_iter)
                                fim_tempo = time.time()
                        else:
                            sg.popup_error("Nenhum método selecionado!")
                            continue
                        
                        resultado_str = "\n".join([f"x{i+1} = {resultado[i]:.4f}" for i in range(n)])
                        tempo_exec = fim_tempo - inicio_tempo
                        if n_iteracoes == -1:
                            sg.popup("Solução encontrada:", resultado_str, "Tempo de execucao (segundos): ", tempo_exec)
                        else:
                            sg.popup("Solução encontrada:", resultado_str, "Num de iteracoes: ", n_iteracoes, "Tempo de execucao (segundos): ", tempo_exec)

                        
                    except np.linalg.LinAlgError:
                        sg.popup_error("O sistema não possui solução única (matriz singular).")
                    except Exception as e:
                        sg.popup_error(f"Erro: {e}")
    elif modo == "Zero de funcoes":
        layout_zero = [
            [sg.Text("f(x): ")],
            [sg.Input(key='f(x)')],
            [sg.Text("f'(x): ")],
            [sg.Input(key="f_derivado")],
            [sg.Text("phi(x): ")],
            [sg.Input(key='phi(x)')],
            [sg.Text("a: ")],
            [sg.Input(key='a')],
            [sg.Text("b: ")],
            [sg.Input(key='b')],
            [sg.Text("Precisao: ")],
            [sg.Input(key='precisao')],
            [sg.Text("x0: ")],
            [sg.Input(key='x0')],
            [sg.Text("x1: ")],
            [sg.Input(key='x1')],
            [sg.Text("Numero maximo de iteracoes: ")],
            [sg.Input(key='iteracoes')],
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]
        zero_info = sg.Window("Calcular zero de funcao", layout_zero)
        evento_zero, valores_zero = zero_info.read()
        if(evento_zero == "Confirmar"):
            f_de_x = valores_zero['f(x)']
            f_derivado = valores_zero['f_derivado']
            phi = valores_zero['phi(x)']
            a_intervalo =  float(valores_zero['a'])
            b_intervalo =  float(valores_zero['b'])
            precisao = float(valores_zero['precisao'])
            x0 = float(valores_zero['x0'])
            x1 = float(valores_zero['x1'])
            num_max_iter = int(valores_zero['iteracoes'])
            
            f_de_x = formatar_funcao(f_de_x)
            f_derivado = formatar_funcao(f_derivado)
            phi = formatar_funcao(phi)
            
            zf.definir_expressoes(f_de_x, f_derivado, phi)
            xs_bissec = zf.bisseccao(a_intervalo, b_intervalo, precisao, num_max_iter)
            if not zf.checar_continuidade_intervalo(a_intervalo, b_intervalo):
                try:
                    raise Exception("funcao phi nao continua no intervalo")
                except Exception:
                    sg.popup_error(f"funcao phi nao continua no intervalo")
            xs_mil = zf.mil(x0, precisao, num_max_iter)
            xs_newton = zf.newton(x0, precisao, num_max_iter)
            xs_secante = zf.secante(x0, x1, precisao, num_max_iter)
            xs_regulaFalsi = zf.regulaFalsi(a_intervalo, b_intervalo, precisao, num_max_iter)
            print("dei erro no df")
            planilha_resultados = converteDf.converte(xs_bissec, xs_mil, xs_newton, xs_secante, xs_regulaFalsi)
            
            layout_df = [
                [sg.Text("Tabela de resultados:")],
                [sg.Multiline(planilha_resultados.to_string(index=False), size=(100, 40), disabled=True)],
                [sg.Button("Fechar")]
            ]
            janela_df = sg.Window("Tabela resultados", layout_df)
            while True:
                evento, _ = janela_df.read()
                if evento in (sg.WIN_CLOSED, "Fechar"):
                    break

            janela_df.close()
        else:
            zero_info.close()

        
    janela_modo.close()