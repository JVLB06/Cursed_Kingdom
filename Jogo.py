# Importações de bibliotecas
import os
import PySimpleGUI as gui
import Features as f
from time import sleep

# Declaração das variáveis
confirma = False
abrir = False
gerar = False
carregamento = ""
s1 = "Save1.txt"
s2 = "Save2.txt"
s3 = "Save3.txt"
gui.theme("Reds")
ciclo = f.capa()
sleep(0.5)
while ciclo: # Acesso aos possíveis saves open txt
    save_screen = [[gui.Text("Selecione um save:", font=("Arial", 15))],
                    [gui.Radio("Save 1", "group 1", key="SAVE1", font=("Arial", 15), default=True), 
                     gui.Radio("Save 2", "group 1", key="SAVE2", font=("Arial", 15)), 
                     gui.Radio("Save 3", "group 1", key="SAVE3", font=("Arial", 15))],
                     [gui.Button("Novo jogo", key="new", font=("Arial", 13)), gui.Button("Carregar", key="select", font=("Arial", 13))]]
    save = gui.Window("Save Screen", save_screen, element_justification='c', size=(335, 150))
    event, values = save.read()
    if event == "select": # Interface para seleção de save
        abrir = True
        # Listagem dos saves
        if values["SAVE1"] == True:
            confirma = f.abre_teste(s1)
            carregamento = s1
        if values["SAVE2"] == True:
            confirma = f.abre_teste(s2)
            carregamento = s2
        if values["SAVE3"] == True:
            confirma = f.abre_teste(s3)
            carregamento = s3
        if confirma == False:
            carregamento = ""
            while True: # Caso: arquivo inválido
                tente_outra_vez = [[gui.Text("Este arquivo de jogo não existe:")], [gui.Button("Ok", key="ok")]]
                tente = gui.Window("Arquivo inválido", tente_outra_vez, element_justification='c', size=(230, 70))
                results, valor = tente.read()
                if results == "ok":
                    tente.close()
                    break
        else: # Caso: arquivo válido
            print(carregamento)
            save.close()
            break
    if event == "new": # Caso, criação de novo jogo
        save.close()
        while True: # Tela de seleção de save
            novo_jogo = [[gui.Text("Selecione um slot:", font=("Arial", 15))],
                    [gui.Radio("Slot 1", "group 1", key="SLOT1", font=("Arial", 15), default=True), 
                     gui.Radio("Slot 2", "group 1", key="SLOT2", font=("Arial", 15)), 
                     gui.Radio("Slot 3", "group 1", key="SLOT3", font=("Arial", 15))],
                     [gui.Button("Criar", key="feito", font=("Arial", 13))]]
            novo = gui.Window("Novo save", novo_jogo, element_justification='c', size=(330,150))
            event, values = novo.read()
            if event == gui.WIN_CLOSED:
                novo.close()
                break          
            if event == "feito":
                gerar = True
                if values["SLOT1"] == True:
                    r = open(s1, "wt")
                    r.close()
                    carregamento = s1
                    novo.close()
                    break
                if values["SLOT2"] == True:
                    r = open(s2, "wt")
                    r.close()
                    carregamento = s2
                    novo.close()
                    break
                if values["SLOT3"] == True:
                    r = open(s3, "wt") 
                    r.close()
                    carregamento = s3
                    novo.close()
                    break
    if event == gui.WIN_CLOSED:
        save.close()
        break  
if gerar == True:
    # Padrão de lista: Capítulo, Max HP, HP atual, Dano especial, Arquivo mapa[], Coordenada (x, y) no mapa
    novo_save = open(carregamento, "at")
    novo_save.write("0\n")
    novo_save.write("50\n")
    novo_save.write("50\n")
    novo_save.write("15\n")
    novo_save.write("1\n")
    novo_save.write("0\n")  
    novo_save.write("280\n") 
    novo_save.close() 
if abrir == True:
    # Padrão de lista: Capítulo, Max HP, HP atual, Dano especial, Arquivo mapa[], Coordenada (x, y) no mapa
    # Save selecionado, abrir arquivo de jogo  
    start_game = f.abridor(carregamento)
    # Manipulação do texto de leitura
    for c in range(len(start_game)):
        start_game[c] = int(start_game[c])
# Acesso aos diferentes níveis
if str(start_game[0]) == "0": # Intro
    fecha = f.intro()
    start_game[0] = fecha
if str(start_game[0]) == "1": # Nível 1
    backup = f.chapter1(start_game[1], start_game[2], start_game[3], start_game[4], start_game[5], start_game[6])
    os.remove(carregamento)
    capitulo_1 = open(carregamento, "at")
    capitulo_1.write(str(backup[0])+"\n")
    capitulo_1.write(str(backup[1])+"\n")
    capitulo_1.write(str(backup[2])+"\n")
    capitulo_1.write(str(backup[3])+"\n")
    capitulo_1.write(str(backup[4])+"\n")
    capitulo_1.write(str(backup[5])+"\n")
    capitulo_1.write(str(backup[6])+"\n")
    capitulo_1.close()
if str(start_game[0]) == "2": # Nível 2
    print(2)
if str(start_game[0]) == "3": # Nível 3
    print(3)
if str(start_game[0]) == "4": # Nível 4
    print(4)
if str(start_game[0]) == "5": # Nível 5
    print(5)
