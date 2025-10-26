import PySimpleGUI as sg
import numpy as np
import metodosSistemasLineares as msl
sg.theme("DarkBlue14")

def criar_layout_inicial():
    return [
        [sg.Text("Tamanho do sistema (n x n): "), sg.Input(key="-N-", size=(5,1)), sg.Button("Gerar")],
        [sg.HorizontalSeparator()],
        [sg.Button("Sair")]
    ]

janela = sg.Window("Leitor de Matrizes - Sistemas Lineares", criar_layout_inicial())

while True:
    evento, valores = janela.read()
    if evento in (sg.WIN_CLOSED, "Sair"):
        break

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
                        
                    #Metodos AQUI
                    metodo_layout = [
                        [sg.Text("Escolha o método:")],
                        [sg.Button("Gauss"), sg.Button("Gauss-Jordan"), sg.Button("Inversa")]
                    ]

                    metodo_janela = sg.Window("Método de resolução", metodo_layout, modal=True)
                    evento_metodo, _ = metodo_janela.read()
                    metodo_janela.close()

                    if evento_metodo == "Gauss":
                        resultado = msl.eliminacao_gauss(A, b)
                        
                    elif evento_metodo == "Gauss-Jordan":
                        continue
                    elif evento_metodo == "Inversa":
                        continue
                    else:
                        sg.popup_error("Nenhum método selecionado!")
                        continue
                    
                    resultado_str = "\n".join([f"x{i+1} = {resultado[i]:.4f}" for i in range(n)])
                    sg.popup("Solução encontrada:", resultado_str)
                    
                except np.linalg.LinAlgError:
                    sg.popup_error("O sistema não possui solução única (matriz singular).")
                except Exception as e:
                    sg.popup_error(f"Erro: {e}")
