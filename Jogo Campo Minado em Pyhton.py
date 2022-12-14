#!/usr/bin/env python
# coding: utf-8

# ## JOGO CAMPO MINADO EM PYTHON ##
# 
# ## CREATED BY LUIZ ALBERTO ##

# In[ ]:





import math
from random import randint
import xlsxwriter


def imprimir_matriz(matriz, linhas, colunas):
    for l in range(linhas):
        for c in range(colunas):
            print(f'[{matriz[l][c]}]', end="")
        print()


def imprimir_bombas(matriz, linhas, colunas, bombas):
    for b in range(0, bombas):
        while True:
            x = randint(0, linhas - 1)
            y = randint(0, colunas - 1)
            if matriz[x][y] != "*":
                matriz[x][y] = "*"
                break
    return matriz


def verificar_minas_adjacentes(matriz, linhas, colunas):
    for a in range(0, linhas):
        for b in range(0, colunas):
            if matriz[a][b] == "*":
                continue
            cont_minas_adj = 0
            for c in range(a - 1 if a > 0 else 0, a + 2 if a < linhas - 1 else linhas):
                for d in range(b - 1 if b > 0 else 0, b + 2 if b < colunas - 1 else colunas):
                    if matriz[c][d] == "*":
                        cont_minas_adj += 1
            matriz[a][b] = str(cont_minas_adj)

    return matriz


def posicoes_restantes(matriz):
    rest = 0
    for l in matriz:
        for j in l:
            if len(j) == 2:
                rest += 1
    return rest


def ler_posicao_linha(pos, linhas):
    while True:
        try:
            var = int(input(f"Informe a {pos} que deseja selecionar [1-{linhas}]")) - 1
            if var >= 0 and var < linhas:
                return var
        except ValueError:
            pass
        print("Opção inválida")


def ler_posicao_coluna(pos, colunas):
    while True:
        try:
            var = int(input(f"Informe a {pos} que deseja selecionar [1-{colunas}]")) - 1
            if var >= 0 and var < colunas:
                return var
        except ValueError:
            pass
        print("Opção inválida")



def main():
    vitorias = 0
    derrotas = 0
    RUNNING = True

    while RUNNING:

        print("Escolha a dimensão do seu tabuleiro:")
        colunas = int(input("Digite o numero de linhas (maior que 2): "))
        linhas = int(input("Digite o numero de colunas (maior que 2): "))

        while True:
            print()
            print("Dificuldades:\n"
                  "1: Facil (15% de bombas)\n"
                  "2: Medio (25% de bombas)\n"
                  "3: Dificil (50% de bombas)")
            dificuldade = int(input("Digite o numero da dificuldade: "))
            if dificuldade == 1:
                bombas = math.ceil(linhas * colunas * 0.15)
                break
            elif dificuldade == 2:
                bombas = math.ceil(linhas * colunas * 0.25)
                break
            elif dificuldade == 3:
                bombas = math.ceil(linhas * colunas * 0.50)
                break
            else:
                print()
                print("Digite 1, 2 ou 3 para escolher os niveis!")

        matriz = [["-" for x in range(colunas)] for y in range(linhas)]
       

        matriz_bombas = imprimir_bombas(matriz, linhas, colunas, bombas)
       

        matriz_adjacente = verificar_minas_adjacentes(matriz, linhas, colunas)
       

        matriz = [["-" for x in range(colunas)] for y in range(linhas)]
       

        workbook = xlsxwriter.Workbook('campo_minado_excel.xlsx')
        worksheet = workbook.add_worksheet(name="CAMPO_TELA")
        col = 0
        for row, data in enumerate(matriz):
            worksheet.write_row(row, col, data)
        worksheet2 = workbook.add_worksheet(name="CAMPO_SECRETO")
        col = 0
        for row, data in enumerate(matriz_adjacente):
            worksheet2.write_row(row, col, data)
        workbook.close()

        while RUNNING:
            print()
            x = ler_posicao_linha("linha", linhas)
            y = ler_posicao_coluna("coluna", colunas)
            if matriz_adjacente[x][y] == "*":
                derrotas += 1
                imprimir_matriz(matriz_adjacente, linhas, colunas)
                matriz = matriz_adjacente

                workbook = xlsxwriter.Workbook('campo_minado_excel.xlsx')
                worksheet = workbook.add_worksheet(name="CAMPO_TELA")
                col = 0
                for row, data in enumerate(matriz):
                    worksheet.write_row(row, col, data)
                worksheet2 = workbook.add_worksheet(name="CAMPO_SECRETO")
                col = 0
                for row, data in enumerate(matriz_adjacente):
                    worksheet2.write_row(row, col, data)
                workbook.close()

                print("Que pena, você perdeu!")
                print(f"Você teve {vitorias} vitória(s) durante a partida.")
                RUNNING = False
                break
            elif matriz_adjacente[x][y] != "*":
                matriz[x][y] = matriz_adjacente[x][y]
                imprimir_matriz(matriz, linhas, colunas)
                vitorias += 1
                print(f"Você tem {vitorias} vitória(s).")

                workbook = xlsxwriter.Workbook('campo_minado_excel.xlsx')
                worksheet = workbook.add_worksheet(name="CAMPO_TELA")
                col = 0
                for row, data in enumerate(matriz):
                    worksheet.write_row(row, col, data)
                worksheet2 = workbook.add_worksheet(name="CAMPO_SECRETO")
                col = 0
                for row, data in enumerate(matriz_adjacente):
                    worksheet2.write_row(row, col, data)
                workbook.close()

                if vitorias >= (linhas * colunas - bombas):
                    print("Parabéns, você completou o jogo")
                    RUNNING = False
                           
                    break
                    
main()


# In[ ]:


# In[ ]:




