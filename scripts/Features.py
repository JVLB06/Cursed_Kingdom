from sys import exit
import PySimpleGUI
import os

x = 320
y = 320
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# Sem uso por enquanto
def find_arq(nome_arquivo):
    # Percorra recursivamente todo o sistema de arquivos
    for pasta_raiz, _, arquivos in os.walk('/'):
        # Verifique se o arquivo está na lista de arquivos do diretório atual
        if nome_arquivo in arquivos:
            # Retorne o caminho completo do arquivo
            return os.path.join(pasta_raiz, nome_arquivo)

    # Se o arquivo não for encontrado em todo o sistema de arquivos, retorne None
    return None

def death_screen():
    import pygame
    # Inicializar Pygame
    pygame.init()
    # Criar tela
    size = (640, 480)
    pygame.display.set_caption("You died")
    screen = pygame.display.set_mode(size)
    # Configurar relógio para controlar a taxa de quadros
    clock = pygame.time.Clock()
    # Tratamento de texto
    fonte = pygame.font.SysFont("arial", 50)
    fonte2 = pygame.font.SysFont("arial", 30)
    # Importação de imagens
    queda = pygame.image.load("C:/Users/User/Documents/Cursed_Kingdom/Sprites jogo/Player/Player_death.png")
    posicao = [(a * 120, 0) for a in range(10)]
    morreu = [pygame.transform.scale(queda.subsurface(pygame.Rect(pos, (120, 80))), (120 * 4, 80 * 4)) for pos in posicao]
    parado = 0
    rodando = True
    reviver = False
    while rodando:
        clock.tick(30)
        screen.fill(black)
        parado += 0.3
        if parado >= 9:
            parado = 9
        screen.blit(morreu[int(parado)], (180, 60))
        screen.blit(fonte.render("Você Morreu!", True, (255, 0, 0)), (200, 70))
        screen.blit(fonte2.render("Pressione ESC para sair ou SHIFT para continuar", True, white), (60, 400))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodando = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    reviver = False
                    rodando = False
                if event.key == pygame.K_RSHIFT or event.key == pygame.K_LSHIFT:
                    reviver = True
                    rodando = False
        pygame.display.update()
    pygame.quit()
    return reviver
def abre_teste(arq):
    try:
        r = open(arq, "rt")
        r.read()
    except:
        existe = False
    else: 
        existe = True
    finally:
        return existe
def abridor(arquivo): # Deve abrir o arquivo .txt e retornar suas informações em lista
    # Padrão de lista: Capítulo, Max HP, HP atual, Dano especial, Arquivo mapa[], Coordenada (x, y) no mapa
    arq = open(arquivo, "rt")
    ler = arq.readlines()
    salvamento = []
    for seq in range(len(ler)):
        leitura = ler[seq].split()
        ler[seq] = ""
        for b in range(len(leitura)):
            ler[seq] += leitura[b]
        salvamento.append(str(ler[seq]))
    arq.close()
    return salvamento
def tem_certeza():
    import PySimpleGUI as sg
    sg.theme("Reds")
    while True:
        layout = [[sg.Text("Tem certeza de que deseja sair?")], [sg.Text("As informações não salvas serão perdidas")], [sg.Button("Sair", key="SAIR"), sg.Button("Cancelar", key="CANCEL")]]
        save = sg.Window("Não vá embora", layout, (640, 480))
        event, values = save.read()
        if event == "SAIR":
            save.close()
            retorno = True
            break
        if event == "CANCEL":
            save.close()
            retorno = False
            break
    return retorno
def pausar(pause_screen, size, hp, vida_total, especial):
    import pygame
    from sys import exit
    # Programar o Pause
    pygame.init()
    valida = False
    botao = False
    giro = pygame.time.Clock()
    salvar = False
    parado = 0
    # Tratamento de imagem
    fonte = pygame.font.SysFont("arial", 50)
    main = pygame.font.SysFont("arial", int(size[0][1]/25))
    position = [(0,32), (0,96), (48,96), (112,80), (112,96), (112,112), (136,160), (72,16), (128,16),(8,160),(80,64)]
    tamanhos = [(48,48), (48,32), (32,32), (32,16), (32,16), (32,16), (16,16), (56,16), (56,16),(16,16),(16,16)]
    par_pos = [(0,0),(120,0),(240,0),(360,0),(480,0),(600,0),(720,0),(840,0),(960,0),(1080,0)]
    chave_pos = [(32,0), (0,16),(64,32),(96,0)] #Esc, Shift, Space, Backspace
    cp = [(32,0),(48,0),(0,64),(96,64)] # Left, Right, Q, W 
    # Importação de imagens
    gui = pygame.image.load("C:/Users/User/Documents/Cursed_Kingdom/Sprites jogo/GUI.png")
    par = pygame.image.load("C:/Users/User/Documents/Cursed_Kingdom/Sprites jogo/Player/Player_idle.png")
    sinal = pygame.image.load("C:/Users/User/Documents/Cursed_Kingdom/Sprites jogo/Keyboard Extras.png")
    letra = pygame.image.load("C:/Users/User/Documents/Cursed_Kingdom/Sprites jogo/Keyboard Letters.png")
    #Listas vazias
    display_geral = []
    idle = []
    keyboard = []
    for rep in range(len(chave_pos)):
        ui = sinal.subsurface(chave_pos[rep], (32,16))
        keyboard.append(ui)
    for rep in range(len(cp)):
        ui = letra.subsurface(cp[rep], (16,16))
        keyboard.append(ui)
    for rep in range(len(par_pos)):
        ui = par.subsurface(par_pos[rep], (120,80))
        idle.append(ui)
    for rep in range(len(position)):
        ui = gui.subsurface(position[rep], tamanhos[rep])
        display_geral.append(ui)
    op = size[0][0]/4 * hp/vida_total 
    display_geral[1] = pygame.transform.scale(display_geral[1], (size[0][0]-650, size[0][1]+100))
    display_geral[0] = pygame.transform.scale(display_geral[0], (size[0][0]-500, size[0][1]+100))
    display_geral[2] = pygame.transform.scale(display_geral[2], (size[0][0]-800, size[0][1]-100))
    display_geral[3] = pygame.transform.scale(display_geral[3], (size[0][0]/6, size[0][1]/6))
    display_geral[4] = pygame.transform.scale(display_geral[4], (size[0][0]/6, size[0][1]/6))
    display_geral[5] = pygame.transform.scale(display_geral[5], (size[0][0]/6, size[0][1]/6))
    display_geral[6] = pygame.transform.scale(display_geral[6], (size[0][0]/6*0.8, size[0][1]/6*0.8))
    display_geral[7] = pygame.transform.scale(display_geral[7], (op, size[0][1]/6*0.8))
    display_geral[8] = pygame.transform.scale(display_geral[8], (size[0][0]/4, size[0][1]/6*0.8))
    display_geral[9] = pygame.transform.scale(display_geral[9], (size[0][0]/6*0.8, size[0][1]/6*0.8))
    display_geral[10] = pygame.transform.scale(display_geral[10], (size[0][0]/6*0.7, size[0][1]/6*0.7))
    keyboard[0] = pygame.transform.scale(keyboard[0], (size[0][0]/9, size[0][1]/9))
    keyboard[1] = pygame.transform.scale(keyboard[1], (size[0][0]/9, size[0][1]/9))
    keyboard[2] = pygame.transform.scale(keyboard[2], (size[0][0]/9, size[0][1]/9))
    keyboard[3] = pygame.transform.scale(keyboard[3], (size[0][0]/9, size[0][1]/9))
    keyboard[4] = pygame.transform.scale(keyboard[4], (size[0][0]/15,size[0][0]/15))
    keyboard[5] = pygame.transform.scale(keyboard[5], (size[0][0]/15,size[0][0]/15))
    keyboard[6] = pygame.transform.scale(keyboard[6], (size[0][0]/15,size[0][0]/15))
    keyboard[7] = pygame.transform.scale(keyboard[7], (size[0][0]/15,size[0][0]/15))
    ok = True
    sair = False
    while ok:
        botao = False
        giro.tick(30)
        pause_screen.fill((0, 0, 128))
        parado += 1
        if parado >= 10:
            parado = 0
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                botao = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    valida = tem_certeza()
                    if valida == True:
                        exit()
                if event.key == pygame.K_RSHIFT or event.key == pygame.K_LSHIFT:
                    ok = False
        pause_screen.blit(display_geral[1], (-50,0))
        pause_screen.blit(display_geral[0], (size[0][0]-790, -50))
        pause_screen.blit(display_geral[2], (30,100))
        # Controle do mouse
        # Sair do jogo
        ml = pygame.mouse.get_pos()
        if ml[0] < size[0][0]-300 or ml[0] > size[0][0]-300 + size[0][0]/6 or ml[1] < 80 or ml[1] > 80 + size[0][1]/6:
            pause_screen.blit(display_geral[3], (size[0][0]-300,80))
        if ml[0] > size[0][0]-300 and ml[0] < size[0][0]-300 + size[0][0]/6 and ml[1] > 80 and ml[1] < 80 + size[0][1]/6:
            pause_screen.blit(display_geral[5], (size[0][0]-300,80))
            if botao == True:
                pause_screen.blit(display_geral[4], (size[0][0]-300,80))
                salvar = True
                sair = True
                botao = False
                break
        # Salvar o jogo
        if ml[0] < size[0][0]-660 or ml[0] > size[0][0]-660 + size[0][0]/6 or ml[1] < 80 or ml[1] > 80 + size[0][1]/6:
            pause_screen.blit(display_geral[3], (size[0][0]-660,80))
        if ml[0] > size[0][0]-660 and ml[0] < size[0][0]-660 + size[0][0]/6 and ml[1] > 80 and ml[1] < 80 + size[0][1]/6:
            pause_screen.blit(display_geral[5], (size[0][0]-660,80))
            if botao == True:
                pause_screen.blit(display_geral[4], (size[0][0]-660,80))
                count = 0
                conte = 0
                while True:
                    pause_screen.fill(white)
                    count += 1
                    txt1 = fonte.render("Salvando seu jogo, não se desconecte", False, black)
                    txt2 = fonte.render("Seu jogo foi salvo.", False, black)
                    if count >= 500:
                        pause_screen.blit(txt2, (450, 300))
                        conte += 1
                        if conte >= 500:
                            break
                    else:
                        pause_screen.blit(txt1, (300, 300))
                    pygame.display.flip()
                salvar = True
                botao = False
        idle[int(parado)] = pygame.transform.scale(idle[int(parado)], (120*3.3*4, 80*2.5*4))
        pause_screen.blit(display_geral[8], (size[0][0]-720, size[0][1]-550))
        pause_screen.blit(display_geral[7], (size[0][0]-670, size[0][1]-550))
        # Controles do jogo
        pause_screen.blit(main.render("----------Controles----------", True, white), (size[0][0]-500, size[0][1]-380))
        pause_screen.blit(idle[int(parado)], (-430, -100))
        pause_screen.blit(display_geral[6], (size[0][0]-640,86))
        pause_screen.blit(display_geral[9], (size[0][0]-280,86))
        if especial <= 1:
            pause_screen.blit(display_geral[10], (size[0][0]-380,230))
        pause_screen.blit(keyboard[4], (size[0][0]-650, size[0][1]-200))
        pause_screen.blit(keyboard[5], (size[0][0]-550, size[0][1]-200))
        pause_screen.blit(keyboard[2], (size[0][0]-430, size[0][1]-200))
        pause_screen.blit(keyboard[6], (size[0][0]-250, size[0][1]-200))
        pause_screen.blit(keyboard[7], (size[0][0]-150, size[0][1]-200))
        controles1 = main.render("   Left      Right              Jump              Atk 1      Atk 2", True, white)
        pause_screen.blit(controles1, (size[0][0]-650, size[0][1]-120))
        pause_screen.blit(keyboard[0], (size[0][0]-680, size[0][1]-330))
        pause_screen.blit(keyboard[1], (size[0][0]-520, size[0][1]-330))
        pause_screen.blit(keyboard[3], (size[0][0]-360, size[0][1]-330))
        controles2 = main.render("   Exit               Pause            Special", True, white)
        pause_screen.blit(controles2, (size[0][0]-650, size[0][1]-250))
        pygame.display.flip()
    return [salvar, sair]
def intro():
    # Importações específicas
    import pygame as p
    from sys import exit
    # Declaração de variáveis 
    p.init()
    screen = p.display.set_mode((1000, 500)) # Cria tela
    p.display.set_caption("Intro(Cursed Kingdom)")
    tiktak = p.time.Clock() # Taxa de renderização da tela
    sprite_p = (320, 250)
    giro = 0
    x = 0
    x_texto = 1500
    ps = [(0, 0), (120, 0), (240, 0), (360, 0), (480, 0), (600, 0), (720, 0), (840, 0), (960, 0), (1080, 0)]
    rs = []
    font = p.font.SysFont("arial", 32, False, False) # Fonte do texto
    # História do jogo, preparar
    lore = "Este era um reino de muita paz, e assim foi por muitos anos. O povo era feliz e vivia em paz em suas terras, até o dia em que ele chegou, seja lá o que fosse aquilo. Um mago deixou uma maldição sobre o reino, destruindo tudo que havia ali. O rei tentou lutar, porém o mago dominou as florestas e lançou uma maldição sobre o rei, tomando posse do reino para si. Com esse domínio, o reino sucumbiu e o povo se foi, na esperança de um dia ver a salvação de seu reino..."
    # Imagens do jogador e cenário
    cenario = [p.image.load("C:/Users/User/Documents/Cursed_Kingdom/Sprites jogo/Background/Cenário intro/11.png").convert_alpha(),
    p.image.load("C:/Users/User/Documents/Cursed_Kingdom/Sprites jogo/Background/Cenário intro/10.png").convert_alpha(),
    p.image.load("C:/Users/User/Documents/Cursed_Kingdom/Sprites jogo/Background/Cenário intro/09.png").convert_alpha(),
    p.image.load("C:/Users/User/Documents/Cursed_Kingdom/Sprites jogo/Background/Cenário intro/08.png").convert_alpha(),
    p.image.load("C:/Users/User/Documents/Cursed_Kingdom/Sprites jogo/Background/Cenário intro/07.png").convert_alpha(),
    p.image.load("C:/Users/User/Documents/Cursed_Kingdom/Sprites jogo/Background/Cenário intro/06.png").convert_alpha(),
    p.image.load("C:/Users/User/Documents/Cursed_Kingdom/Sprites jogo/Background/Cenário intro/05.png").convert_alpha(),
    p.image.load("C:/Users/User/Documents/Cursed_Kingdom/Sprites jogo/Background/Cenário intro/04.png").convert_alpha(),
    p.image.load("C:/Users/User/Documents/Cursed_Kingdom/Sprites jogo/Background/Cenário intro/03.png").convert_alpha(),
    p.image.load("C:/Users/User/Documents/Cursed_Kingdom/Sprites jogo/Background/Cenário intro/02.png").convert_alpha(),
    p.image.load("C:/Users/User/Documents/Cursed_Kingdom/Sprites jogo/Background/Cenário intro/01.png").convert_alpha(),
    p.image.load("C:/Users/User/Documents/Cursed_Kingdom/Sprites jogo/Background/Cenário intro/00.png").convert_alpha()]
    run = p.image.load("C:/Users/User/Documents/Cursed_Kingdom/Sprites jogo/Player/Player_run.png").convert_alpha()
    # Seleção das várias imagens
    for pos in range(len(ps)):
        st = run.subsurface(ps[pos], (120, 80))
        rs.append(st)
    # Loop para a tela
    while True:
        # Seletor de acontecimentos
        for event in p.event.get():
            if event.type == p.QUIT:
                p.quit()
                fecha = "0"
                return fecha
                exit()
            if event.type == p.KEYDOWN:
                if event.key == p.K_SPACE:
                    # Parar a música (a fazer)
                    p.quit()
                    fecha = "1"
                    return fecha
                    exit() 
        # Variáveis de controle de repetição
        giro += 1.5
        if giro >= 10:
            giro = 0
        x -= 30
        if x <= -1000:
            x = 0
        x_texto -= 10
        # Atualização da tela
        tiktak.tick(120)
        screen.fill((0, 0, 0))
        # Ciclo de cenário
        for sequence in range(0,11):
            cenario[sequence] = p.transform.scale(cenario[sequence], (1000, 600))
            screen.blit(cenario[sequence], (x, -120))
        for sequence in range(0,11):
            cenario[sequence] = p.transform.scale(cenario[sequence], (1000, 600))
            screen.blit(cenario[sequence], ((x+1000), -120)) 
        # Texto da lore do jogo
        if x_texto > -5000:
            write = font.render(lore, False, white)
            screen.blit(write, (x_texto, 120))
        else: # Caso para término da introdução
            texto = "--Pressione ESPAÇO para continuar--"
            write = font.render(texto, False, white)
            screen.blit(write, (270, 240))
        # Desenho do personagem
        rs[int(giro)] = p.transform.scale(rs[int(giro)], (120*2.5, 80*2.5))
        screen.blit(rs[int(giro)], sprite_p)
        p.display.flip()
# Parâmetros: Max HP, HP atual, Dano especial, Arquivo mapa[], Coordenada (x, y) no mapa
def chapter1(hp_max, vida, atk_especial, parte_chapter, cx, cy):
    import pygame as p
    from random import randint
    from time import sleep
    # Base para a formatação
    p.init()
    p.display.init()
    size = p.display.list_modes()
    ref = int(0)
    tela = p.display.set_mode(size[ref])
    tiktak = p.time.Clock()
    # Importação de imagens
    gui = p.image.load("C:/Users/User/Documents/Cursed_Kingdom/Sprites jogo/GUI.png")
    pos = [(128,16),(72,16),(80,64),(144,64),(0,16)]
    tamanho = [(56,16),(56,16),(16,16),(48,16),(56,16)]
    gui_geral = []
    arvores = p.image.load("C:/Users/User/Documents/Cursed_Kingdom/Sprites jogo/Background/Arvore_sabia.png").convert_alpha()
    castelo1 = p.image.load("C:/Users/User/Documents/Cursed_Kingdom/Sprites jogo/Background/Castelo_i1.jpg").convert_alpha()
    castelo2 = p.image.load("C:/Users/User/Documents/Cursed_Kingdom/Sprites jogo/Background/Castelo_i2.jpg").convert_alpha()
    castelo3 = p.image.load("C:/Users/User/Documents/Cursed_Kingdom/Sprites jogo/Background/Castelo_i3.png").convert_alpha()
    entrada = p.image.load("C:/Users/User/Documents/Cursed_Kingdom/Sprites jogo/Background/abertura_castelo.png").convert_alpha()
    forest = p.image.load("C:/Users/User/Documents/Cursed_Kingdom/Sprites jogo/Background/Cenário intro.jpeg").convert_alpha()
    player = [p.image.load("C:/Users/User/Documents/Cursed_Kingdom/Sprites jogo/Player/Player_run.png").convert_alpha(), 
              p.image.load("C:/Users/User/Documents/Cursed_Kingdom/Sprites jogo/Player/Player_attack1.png").convert_alpha(),
              p.image.load("C:/Users/User/Documents/Cursed_Kingdom/Sprites jogo/Player/Player_attack2.png").convert_alpha(),
              p.image.load("C:/Users/User/Documents/Cursed_Kingdom/Sprites jogo/Player/Player_special.png").convert_alpha(),
              p.image.load("C:/Users/User/Documents/Cursed_Kingdom/Sprites jogo/Player/Player_idle.png").convert_alpha(),
              p.image.load("C:/Users/User/Documents/Cursed_Kingdom/Sprites jogo/Player/Player_death.png").convert_alpha(),
              p.image.load("C:/Users/User/Documents/Cursed_Kingdom/Sprites jogo/Player/Player_hit.png").convert_alpha(),
              p.image.load("C:/Users/User/Documents/Cursed_Kingdom/Sprites jogo/Player/Player_jump.png").convert_alpha()]
    monsters = [p.image.load("C:/Users/User/Documents/Cursed_Kingdom/Sprites jogo/.1 Desesperate World/Goblin.png").convert_alpha(),
                p.image.load("C:/Users/User/Documents/Cursed_Kingdom/Sprites jogo/.1 Desesperate World/Flying_eye.png").convert_alpha(),
                p.image.load("C:/Users/User/Documents/Cursed_Kingdom/Sprites jogo/.1 Desesperate World/Mushroom.png").convert_alpha(),
                p.image.load("C:/Users/User/Documents/Cursed_Kingdom/Sprites jogo/.1 Desesperate World/Projectile.png").convert_alpha()]
    boss = p.image.load("C:/Users/User/Documents/Cursed_Kingdom/Sprites jogo/.1 Desesperate World/Boss_Knight.png").convert_alpha()
    # Declaração de variáveis
    pulo = False
    andar = False
    ataque1 = False
    ataque2 = False
    v_special = False
    death_player = False
    ande = True
    sair = False
    finish = True
    direita = True
    aprovado1 = False
    aprovado2 = False
    aprovado3 = False
    aprovado4 = False
    aprovado5 = False
    aprovado6 = False
    tutorial = False
    chefao = False
    fala = False
    fala2 = False
    cfala = 0
    cfala2 = 0
    fala_rei = ["QUEM OUSA ADENTRAR O MEU CASTELO?!", "QUEM PENSA QUE TEM PODER CONTRA MIM?!", "Se você tem tanta coragem, então venha ME ENFRENTAR!", "Um mortal como você não será páreo para o REI MORTO!", "Então é você quem vem me desafiar?!", "Vá em frente e tente destruir o REI MORTO!", "Liberte o rei morto da maldição"]
    stop = True
    atk_chos = 5
    anterior = 0
    nivel = 1
    valida_save = False
    lista = [f"{parte_chapter}", f"{hp_max}", f"{vida}", f"{atk_especial}", f"{parte_chapter}", f"{cx}", f"{cy}"]
    result = 70
    parado = 0
    andando = 0
    pulando = 0
    fall = 0
    atk = 0
    loopt = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    dano_geral = [0]
    chao = 300

    npc_pos = p.display.list_modes()
    gera_goblin = [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False] # Definição da existência dos goblins
    g_pos = [900,1100,1200,1000,1000,1100,1500,900,-100,-150,-200,npc_pos[0][0]-600,npc_pos[0][0]-700,npc_pos[0][0]-800,1200,1100,1300,900,800,700,750,600,1100,1000,1000,1100,1200] # Posição dos goblins
    g_y = [chao,chao,chao,chao,chao,chao,chao,chao,chao,chao,chao,chao,chao,chao,chao,chao,chao,chao,chao,chao,chao,chao,chao,chao,chao,chao,chao] # Posição y dos goblins
    g_direita = [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
    g_action = [0, 3, 13, 14, 24] # Parado, Andando, Hit, Morte, Ataque 
    g_vida = [100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100] # Vida dos goblins
    m_g = [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]

    gera_mushroom = [False,False,False,False,False,False,False,False,False,False,False,False,False,False]
    m_pos = [1000, 1000, 1100, 1200, 1000, 1000, 1100, 1150, 900, 850, 0, 0, 100, 210, 1000, 1000]
    m_y = [chao,chao,chao,chao,chao,chao,chao,chao,chao,chao,chao,chao,chao,chao,chao,chao,chao,chao,chao,chao]
    m_direita = [False,False,False,False,False,False,False,False,False,False,False,False,False,False]
    m_action = [0, 3, 13, 14, 21, 30] # Parado, Andando, Hit, Morte, Ataque, Recarregar vida
    m_vida = [100, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50]
    m_m = [False,False,False,False,False,False,False,False,False,False,False,False,False,False]

    gera_fly = [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
    f_pos = [1100,1000,1100,900,1000,1000,1000,1000,1000,1000,1000,1000,-100,-50,0,1100,1200,1300,1200]
    f_y = [chao,chao+7,chao-2,chao,chao,chao,chao,chao,chao,chao,chao,chao,chao,chao,chao,chao,chao,chao,chao,chao]
    f_direita = [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
    f_action = [0, 3, 10, 11, 25] # Parado, Andando, Hit, Morte, Ataque, Projétil
    projetil_fly = [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
    f_vida = [70, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 500]
    m_f = [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
    pro_move = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    x_player = cx
    y_player = cy
    multi_x = 3.3 # X tela : multi_x = X sprite
    multi_y = 2.5 # Y tela : multi_y = Y sprite
    altura = float(size[ref][0])
    comprimento = float(size[ref][1])
    font = p.font.SysFont("arial", 25, False, False)
    fonte = p.font.SysFont("arial", 30, False, False)
    carregamento = p.font.SysFont("Times New Roman", 50, True, False)
    # Padrão de lista: Capítulo, Max HP, HP atual, Dano especial, Arquivo mapa[], Coordenada (x, y) no mapa
    if parte_chapter < 4 and parte_chapter != 0:
        dano1level = 2
        dano2level = 3
    if parte_chapter <= 6 and parte_chapter > 3 and parte_chapter != 0:
        dano1level = 3
        dano2level = 4
    if parte_chapter == 0:
        dano1level = 5
        dano2level = 6.5
    # Sequência de medidas das imagens
    # JOGADOR
    p_idle = [(0, 0), (120, 0), (240, 0), (360, 0), (480, 0), (600, 0), (720, 0), (840, 0), (960, 0), (1080, 0)]
    idle_all = []
    p_death = [(0, 0), (120, 0), (240, 0), (360, 0), (480, 0), (600, 0), (720, 0), (840, 0), (960, 0), (1080, 0)]
    death_all = []
    p_run = [(0, 0), (120, 0), (240, 0), (360, 0), (480, 0), (600, 0), (720, 0), (840, 0), (960, 0), (1080, 0)]
    run_all = []
    hit_all = []
    p_at1 = [(0, 0), (120, 0), (240, 0), (360, 0)]
    at1_all = []
    p_at2 = [(0, 0), (120, 0), (240, 0), (360, 0), (480, 0), (600, 0)]
    at2_all = []
    p_special = [(0, 0), (120, 0), (240, 0), (360, 0), (480, 0), (600, 0), (720, 0), (840, 0), (960, 0), (1080, 0)]
    special_all = []
    p_jump = [(0, 0), (113, 0), (226, 0), (339, 0), (452, 0)]
    jump_all = []

    # GOBLIN
    class goblin():
        def __init__(self) -> None:
            p_goblin = []
            self.sprite_sheet = []
            for g in range(28):
                p_goblin.append(((150*g), 0)) # 150 x 150
            for rep in range(len(p_goblin)):
                spr = monsters[0].subsurface(p_goblin[rep], (150, 150))
                self.sprite_sheet.append(spr)
            self.goblin = monsters[0]
            self.x = 200
            self.walk = 4
            self.rep = 0
            self.hp = 100
            self.dano = 0.9
            self.loop = 0
        def mover(self, taxa, d_e, x):
            if d_e == True:
                x += taxa
            if d_e == False:
                x -= taxa    
        def far(self, player, x):
            if player - x >= 300 or x - player >= 300:
                return True
            else:
                return False
        def identificar(self, player, x):
            if x - player >= 50 and x - player <= 800 or player - x >= 50 and player - x <= 800:
                return True
            else: 
                return False
        def dist(self, player, x):
            if player >= x:
                return True
            if player <= x:
                return False
        def parado_d(self, par, x):
            self.sprite_sheet[int(par)] = p.transform.scale(self.sprite_sheet[int(par)], (altura/multi_x*1.1, comprimento/multi_y*1.1))
            tela.blit(self.sprite_sheet[int(par)], (x, chao+100))
        def parado_e(self, par, x):
            self.sprite_sheet[int(par)] = p.transform.flip(self.sprite_sheet[int(par)], True, False)
            self.sprite_sheet[int(par)] = p.transform.scale(self.sprite_sheet[int(par)], (altura/multi_x*1.1, comprimento/multi_y*1.1))
            tela.blit(self.sprite_sheet[int(par)], (x, chao+100))
            self.sprite_sheet[int(par)] = p.transform.flip(self.sprite_sheet[int(par)], True, False)
        def andando_direita(self, walk, x):
            self.sprite_sheet[int(walk)] = p.transform.scale(self.sprite_sheet[int(walk)], (altura/multi_x*1.1, comprimento/multi_y*1.1))
            tela.blit(self.sprite_sheet[int(walk)], (x, chao+100))
            return True
        def andando_esquerda(self, walk, x):
            self.sprite_sheet[int(walk)] = p.transform.flip(self.sprite_sheet[int(walk)], True, False)
            self.sprite_sheet[int(walk)] = p.transform.scale(self.sprite_sheet[int(walk)], (altura/multi_x*1.1, comprimento/multi_y*1.1))
            tela.blit(self.sprite_sheet[int(walk)], (x, chao+100))
            self.sprite_sheet[int(walk)] = p.transform.flip(self.sprite_sheet[int(walk)], True, False)
            return False
        def ataque_d(self, at, x):
            self.sprite_sheet[int(at)] = p.transform.scale(self.sprite_sheet[int(at)], (altura/multi_x*1.1, comprimento/multi_y*1.1))
            tela.blit(self.sprite_sheet[int(at)], (x, chao+100))
        def ataque_e(self, at, x):
            self.sprite_sheet[int(at)] = p.transform.flip(self.sprite_sheet[int(at)], True, False)
            self.sprite_sheet[int(at)] = p.transform.scale(self.sprite_sheet[int(at)], (altura/multi_x*1.1, comprimento/multi_y*1.1))
            tela.blit(self.sprite_sheet[int(at)], (x, chao+100))
            self.sprite_sheet[int(at)] = p.transform.flip(self.sprite_sheet[int(at)], True, False)
        def hit_d(self, h, x):
            self.sprite_sheet[int(h)] = p.transform.scale(self.sprite_sheet[int(h)], (altura/multi_x*1.1, comprimento/multi_y*1.1))
            tela.blit(self.sprite_sheet[int(h)], (x, chao+100))
        def hit_e(self, h, x):
            self.sprite_sheet[int(h)] = p.transform.flip(self.sprite_sheet[int(h)], True, False)
            self.sprite_sheet[int(h)] = p.transform.scale(self.sprite_sheet[int(h)], (altura/multi_x*1.1, comprimento/multi_y*1.1))
            tela.blit(self.sprite_sheet[int(h)], (x, chao+100))
            self.sprite_sheet[int(h)] = p.transform.flip(self.sprite_sheet[int(h)], True, False)
        def morte_d(self, m, x):
            self.sprite_sheet[int(m)] = p.transform.scale(self.sprite_sheet[int(m)], (altura/multi_x*1.1, comprimento/multi_y*1.1))
            tela.blit(self.sprite_sheet[int(m)], (x, chao+100))
            return False
        def morte_e(self, m, x):
            self.sprite_sheet[int(m)] = p.transform.flip(self.sprite_sheet[int(m)], True, False)
            self.sprite_sheet[int(m)] = p.transform.scale(self.sprite_sheet[int(m)], (altura/multi_x*1.1, comprimento/multi_y*1.1))
            tela.blit(self.sprite_sheet[int(m)], (x, chao+100))
            self.sprite_sheet[int(m)] = p.transform.flip(self.sprite_sheet[int(m)], True, False)
            return False   
    # MUSHROOM
    class mushroom():
        def __init__(self) -> None:
            p_mushroom = []
            self.sprite_sheet = []
            for g in range(39):
                p_mushroom.append(((150*g), 0)) # 150 x 150
            for rep in range(len(p_mushroom)):
                spr = monsters[2].subsurface(p_mushroom[rep], (150, 150))
                self.sprite_sheet.append(spr)
            self.mushroom = monsters[2]
            self.x = 200
            self.walk = 4
            self.rep = 0
            self.hp = 100
            self.dano = 0.5
            self.loop = 0
        def mover(self, taxa, d_e, x):
            if d_e == True:
                x += taxa
            if d_e == False:
                x -= taxa    
        def far(self, player, x):
            if player - x >= 300 or x - player >= 300:
                return True
            else:
                return False
        def identificar(self, player, x):
            if x - player >= 50 and x - player <= 800 or player - x >= 50 and player - x <= 800:
                return True
            else: 
                return False
        def dist(self, player, x):
            if player >= x:
                return True
            if player <= x:
                return False
        def parado_d(self, par, x):
            self.sprite_sheet[int(par)] = p.transform.scale(self.sprite_sheet[int(par)], (altura/multi_x*1.1, comprimento/multi_y*1.1))
            tela.blit(self.sprite_sheet[int(par)], (x, chao+100))
        def parado_e(self, par, x):
            self.sprite_sheet[int(par)] = p.transform.flip(self.sprite_sheet[int(par)], True, False)
            self.sprite_sheet[int(par)] = p.transform.scale(self.sprite_sheet[int(par)], (altura/multi_x*1.1, comprimento/multi_y*1.1))
            tela.blit(self.sprite_sheet[int(par)], (x, chao+100))
            self.sprite_sheet[int(par)] = p.transform.flip(self.sprite_sheet[int(par)], True, False)
        def andando_direita(self, walk, x):
            self.sprite_sheet[int(walk)] = p.transform.scale(self.sprite_sheet[int(walk)], (altura/multi_x*1.1, comprimento/multi_y*1.1))
            tela.blit(self.sprite_sheet[int(walk)], (x, chao+100))
            return True
        def andando_esquerda(self, walk, x):
            self.sprite_sheet[int(walk)] = p.transform.flip(self.sprite_sheet[int(walk)], True, False)
            self.sprite_sheet[int(walk)] = p.transform.scale(self.sprite_sheet[int(walk)], (altura/multi_x*1.1, comprimento/multi_y*1.1))
            tela.blit(self.sprite_sheet[int(walk)], (x, chao+100))
            self.sprite_sheet[int(walk)] = p.transform.flip(self.sprite_sheet[int(walk)], True, False)
            return False
        def ataque_d(self, at, x):
            self.sprite_sheet[int(at)] = p.transform.scale(self.sprite_sheet[int(at)], (altura/multi_x*1.1, comprimento/multi_y*1.1))
            tela.blit(self.sprite_sheet[int(at)], (x, chao+100))
        def ataque_e(self, at, x):
            self.sprite_sheet[int(at)] = p.transform.flip(self.sprite_sheet[int(at)], True, False)
            self.sprite_sheet[int(at)] = p.transform.scale(self.sprite_sheet[int(at)], (altura/multi_x*1.1, comprimento/multi_y*1.1))
            tela.blit(self.sprite_sheet[int(at)], (x, chao+100))
            self.sprite_sheet[int(at)] = p.transform.flip(self.sprite_sheet[int(at)], True, False)
        def hit_d(self, h, x):
            self.sprite_sheet[int(h)] = p.transform.scale(self.sprite_sheet[int(h)], (altura/multi_x*1.1, comprimento/multi_y*1.1))
            tela.blit(self.sprite_sheet[int(h)], (x, chao+100))
        def hit_e(self, h, x):
            self.sprite_sheet[int(h)] = p.transform.flip(self.sprite_sheet[int(h)], True, False)
            self.sprite_sheet[int(h)] = p.transform.scale(self.sprite_sheet[int(h)], (altura/multi_x*1.1, comprimento/multi_y*1.1))
            tela.blit(self.sprite_sheet[int(h)], (x, chao+100))
            self.sprite_sheet[int(h)] = p.transform.flip(self.sprite_sheet[int(h)], True, False)
        def morte_d(self, m, x):
            self.sprite_sheet[int(m)] = p.transform.scale(self.sprite_sheet[int(m)], (altura/multi_x*1.1, comprimento/multi_y*1.1))
            tela.blit(self.sprite_sheet[int(m)], (x, chao+100))
            return False
        def morte_e(self, m, x):
            self.sprite_sheet[int(m)] = p.transform.flip(self.sprite_sheet[int(m)], True, False)
            self.sprite_sheet[int(m)] = p.transform.scale(self.sprite_sheet[int(m)], (altura/multi_x*1.1, comprimento/multi_y*1.1))
            tela.blit(self.sprite_sheet[int(m)], (x, chao+100))
            self.sprite_sheet[int(m)] = p.transform.flip(self.sprite_sheet[int(m)], True, False)
            return False
        def regenerate(self, m, x):
            self.sprite_sheet[int(m)] = p.transform.scale(self.sprite_sheet[int(m)], (altura/multi_x*1.1, comprimento/multi_y*1.1))
            tela.blit(self.sprite_sheet[int(m)], (x, chao+100))
    # FLYING EYE
    class fly():
        def __init__(self) -> None:
            p_fly = []
            p_projectile = []
            self.sprite_sheet = []
            self.sprite_projetil = []
            for g in range(30):
                p_fly.append(((150*g), 0)) # 150 x 150
            for rep in range(len(p_fly)):
                spr = monsters[1].subsurface(p_fly[rep], (150, 150))
                self.sprite_sheet.append(spr)
            for g in range(8):
                p_projectile.append(((43*g), 0)) # 43 x 48
            for rep in range(len(p_projectile)):
                sprite = monsters[3].subsurface(p_projectile[rep], (43, 48))
                self.sprite_projetil.append(sprite)
            self.x = 200
            self.walk = 4
            self.rep = 0
            self.hp = 100
            self.dano = 1.5
        def mover(self, taxa, d_e, x):
            if d_e == True:
                x += taxa
            if d_e == False:
                x -= taxa    
        def far(self, player, x):
            if player - x >= 500 or x - player >= 500:
                return True
            else:
                return False
        def identificar(self, player, x):
            if x - player >= 400 and x - player <= 800 or player - x >= 400 and player - x <= 800:
                return True
            else: 
                return False
        def dist(self, player, x):
            if player >= x:
                return True
            if player <= x:
                return False
        def parado_d(self, par, x):
            self.sprite_sheet[int(par)] = p.transform.scale(self.sprite_sheet[int(par)], (altura/multi_x*1.1, comprimento/multi_y*1.1))
            tela.blit(self.sprite_sheet[int(par)], (x, chao+50))
        def parado_e(self, par, x):
            self.sprite_sheet[int(par)] = p.transform.flip(self.sprite_sheet[int(par)], True, False)
            self.sprite_sheet[int(par)] = p.transform.scale(self.sprite_sheet[int(par)], (altura/multi_x*1.1, comprimento/multi_y*1.1))
            tela.blit(self.sprite_sheet[int(par)], (x, chao+50))
            self.sprite_sheet[int(par)] = p.transform.flip(self.sprite_sheet[int(par)], True, False)
        def andando_direita(self, walk, x):
            self.sprite_sheet[int(walk)] = p.transform.scale(self.sprite_sheet[int(walk)], (altura/multi_x*1.1, comprimento/multi_y*1.1))
            tela.blit(self.sprite_sheet[int(walk)], (x, chao+50))
            return True
        def andando_esquerda(self, walk, x):
            self.sprite_sheet[int(walk)] = p.transform.flip(self.sprite_sheet[int(walk)], True, False)
            self.sprite_sheet[int(walk)] = p.transform.scale(self.sprite_sheet[int(walk)], (altura/multi_x*1.1, comprimento/multi_y*1.1))
            tela.blit(self.sprite_sheet[int(walk)], (x, chao+50))
            self.sprite_sheet[int(walk)] = p.transform.flip(self.sprite_sheet[int(walk)], True, False)
            return False
        def ataque_d(self, at, x):
            self.sprite_sheet[int(at)] = p.transform.scale(self.sprite_sheet[int(at)], (altura/multi_x*1.1, comprimento/multi_y*1.1))
            tela.blit(self.sprite_sheet[int(at)], (x, chao+50))
        def ataque_e(self, at, x):
            self.sprite_sheet[int(at)] = p.transform.flip(self.sprite_sheet[int(at)], True, False)
            self.sprite_sheet[int(at)] = p.transform.scale(self.sprite_sheet[int(at)], (altura/multi_x*1.1, comprimento/multi_y*1.1))
            tela.blit(self.sprite_sheet[int(at)], (x, chao+50))
            self.sprite_sheet[int(at)] = p.transform.flip(self.sprite_sheet[int(at)], True, False)
        def hit_d(self, h, x):
            self.sprite_sheet[int(h)] = p.transform.scale(self.sprite_sheet[int(h)], (altura/multi_x*1.1, comprimento/multi_y*1.1))
            tela.blit(self.sprite_sheet[int(h)], (x, chao+50))
        def hit_e(self, h, x):
            self.sprite_sheet[int(h)] = p.transform.flip(self.sprite_sheet[int(h)], True, False)
            self.sprite_sheet[int(h)] = p.transform.scale(self.sprite_sheet[int(h)], (altura/multi_x*1.1, comprimento/multi_y*1.1))
            tela.blit(self.sprite_sheet[int(h)], (x, chao+50))
            self.sprite_sheet[int(h)] = p.transform.flip(self.sprite_sheet[int(h)], True, False)
        def morte_d(self, m, x):
            self.sprite_sheet[int(m)] = p.transform.scale(self.sprite_sheet[int(m)], (altura/multi_x*1.1, comprimento/multi_y*1.1))
            tela.blit(self.sprite_sheet[int(m)], (x, chao+150))
            return False
        def morte_e(self, m, x):
            self.sprite_sheet[int(m)] = p.transform.flip(self.sprite_sheet[int(m)], True, False)
            self.sprite_sheet[int(m)] = p.transform.scale(self.sprite_sheet[int(m)], (altura/multi_x*1.1, comprimento/multi_y*1.1))
            tela.blit(self.sprite_sheet[int(m)], (x, chao+150))
            self.sprite_sheet[int(m)] = p.transform.flip(self.sprite_sheet[int(m)], True, False)
            return False
        def projetil_d(self, pro, x):
            self.sprite_projetil[int(pro)] = p.transform.scale(self.sprite_projetil[int(pro)], (altura/multi_x*0.5, comprimento/multi_y*0.2))
            tela.blit(self.sprite_projetil[int(pro)], (x, chao+180))
        def projetil_e(self, pro, x):
            self.sprite_projetil[int(pro)] = p.transform.flip(self.sprite_projetil[int(pro)], True, False)
            self.sprite_projetil[int(pro)] = p.transform.scale(self.sprite_projetil[int(pro)], (altura/multi_x*0.5, comprimento/multi_y*0.2))
            tela.blit(self.sprite_projetil[int(pro)], (x, chao+180))
            self.sprite_projetil[int(pro)] = p.transform.flip(self.sprite_projetil[int(pro)], True, False)

    # BOSS
    x_boss = npc_pos[0][0]/2
    y_boss = 0.0
    boss_anda = False
    boss_ataca = False
    boss_ataca_rapido = False
    boss_sofre = False
    boss_morre = False
    boss_direita = False
    boss_vida = 550
    danos_boss = [10, 5, 3]
    boss_action = [0,3,11,16,20,24,27,29,35] # Idle, Walk, Attack 1, Attack 2, Attack 3, Run + Attack, Hit, Death, Jump
    knight_frames = []
    boss_sprites = []
    knight_size = (96, 85)
    for z in range(41):
        knight_frames.append(((96*z), 0)) # 96 x 85
    for t in range(len(knight_frames)):
        s = boss.subsurface(knight_frames[t], knight_size)
        boss_sprites.append(s)
    # Invocação das personagens em Sprite
    class roda_game():
        def __init__(self) -> None:
            pass
            self.gob = goblin()
            self.mush = mushroom()
            self.fly = fly()
        def goblin(self, id):
            if gera_goblin[id] == True:
                    # Parado, Andando, Hit, Morte, Ataque
                    find = self.gob.identificar(x_player, g_pos[id])
                    longe = self.gob.far(x_player, g_pos[id])
                    g_direita[id] = self.gob.dist(x_player, g_pos[id])
                    # Se identificar o jogador, anda até ele
                    if find == True:
                        if g_direita[id] == True:
                            g_action[1] += 0.3
                            g_pos[id] += 10
                            if g_action[1] >= 12:
                                g_action[1] = 4
                            self.gob.andando_direita(g_action[1], g_pos[id])
                        if g_direita[id] == False:
                            g_action[1] += 0.3
                            g_pos[id] -= 5
                            if g_action[1] >= 12:
                                g_action[1] = 4
                            self.gob.andando_esquerda(g_action[1], g_pos[id])
                    # Se não identificar o jogador, fica parado
                    if find == False:
                        if longe == False and g_y[id] - y_player < 50:
                            if g_direita[id] == True:
                                loopt[id] += 0.2
                                if loopt[id] >= 10 and loopt[id] <= 14:
                                    g_action[4] += 0.47
                                    if g_action[4] >= 27:
                                        g_action[4] = 24
                                        dano_geral.append(self.gob.dano)
                                    self.gob.ataque_d(g_action[4], g_pos[id])
                                    if loopt[id] >= 13:
                                        loopt[id] = 0
                            if g_direita[id] == False:
                                loopt[id] += 0.2
                                if loopt[id] >= 10 and loopt[id] <= 14:
                                    g_action[4] += 0.47
                                    if g_action[4] >= 27:
                                        g_action[4] = 24
                                        dano_geral.append(self.gob.dano)
                                    self.gob.ataque_e(g_action[4], g_pos[id]) 
                                    if loopt[id] >= 13:
                                        loopt[id] = 0
                            if direita == True:
                                if ataque1 == True:
                                    g_vida[id] -= dano1
                                    self.gob.hit_d(g_action[2], g_pos[id])
                                if ataque2 == True:
                                    g_vida[id] -= dano2
                                    self.gob.hit_d(g_action[2], g_pos[id])
                                if v_special == True:
                                    g_vida[id] -= atk_especial
                                    self.gob.hit_d(g_action[2], g_pos[id])
                            if direita == False:
                                if ataque1 == True:
                                    g_vida[id] -= dano1
                                    self.gob.hit_e(g_action[2], g_pos[id])
                                if ataque2 == True:
                                    g_vida[id] -= dano2
                                    self.gob.hit_e(g_action[2], g_pos[id])
                                if v_special == True:
                                    g_vida[id] -= atk_especial
                                    self.gob.hit_e(g_action[2], g_pos[id])
                            if loopt[id] < 10:
                                longe = True
                        if longe == True and m_g[id] == False or g_y[id] - y_player > 50 and m_g[id] == False:
                            g_action[0] += 0.3
                            if g_action[0] >= 4:
                                g_action[0] = 0
                            if g_direita[id] == True:
                                self.gob.parado_d(g_action[0], g_pos[id])
                            if g_direita[id] == False:
                                self.gob.parado_e(g_action[0], g_pos[id])
                        if g_vida[id] <= 0:
                            if g_direita[id] == True:
                                g_action[3] += 0.3
                                self.gob.morte_d(g_action[3], g_pos[id])
                                m_g[id] = True
                            if g_direita[id] == False:
                                g_action[3] += 0.3
                                self.gob.morte_e(g_action[3], g_pos[id])
                                m_g[id] = True
                            if g_action[3] >= 19:
                                gera_goblin[id] = False
        def mushroom(self, id):
            if gera_mushroom[id] == True:
                    # Parado, Andando, Hit, Morte, Ataque
                    find = self.mush.identificar(x_player, m_pos[id])
                    longe = self.mush.far(x_player, m_pos[id])
                    m_direita[id] = self.mush.dist(x_player, m_pos[id])
                    # Se identificar o jogador, anda até ele
                    if find == True:
                        if m_direita[id] == True:
                            m_action[1] += 0.3
                            m_pos[id] += 3
                            if m_action[1] >= 12:
                                m_action[1] = 4
                            self.mush.andando_direita(m_action[1], m_pos[id])
                        if m_direita[id] == False:
                            m_action[1] += 0.3
                            m_pos[id] -= 3
                            if m_action[1] >= 12:
                                m_action[1] = 4
                            self.mush.andando_esquerda(m_action[1], m_pos[id])
                    # Se não identificar o jogador longe
                    if find == False:
                        # Ataque 
                        if longe == False and m_y[id] - y_player < 50:
                            if m_direita[id] == True:
                                loopt[id] += 0.2
                                if loopt[id] >= 10:
                                    m_action[4] += 0.35
                                    if m_action[4] >= 30:
                                        m_action[4] = 21
                                        dano_geral.append(self.mush.dano)
                                    self.mush.ataque_d(m_action[4], m_pos[id])
                                    if loopt[id] >= 13:
                                        loopt[id] = 0
                            if m_direita[id] == False:
                                loopt[id] += 0.2
                                if loopt[id] >= 10:
                                    m_action[4] += 0.35
                                    if m_action[4] >= 30:
                                        m_action[4] = 21
                                        dano_geral.append(self.mush.dano)
                                    self.mush.ataque_e(m_action[4], m_pos[id]) 
                                    if loopt[id] >= 13:
                                        loopt[id] = 0
                            # Dano
                            if direita == True:
                                if ataque1 == True:
                                    m_vida[id] -= dano1
                                    self.mush.hit_d(m_action[2], m_pos[id])
                                if ataque2 == True:
                                    m_vida[id] -= dano2
                                    self.mush.hit_d(m_action[2], m_pos[id])
                                if v_special == True:
                                    m_vida[id] -= atk_especial
                                    self.mush.hit_d(m_action[2], m_pos[id])
                            if direita == False:
                                if ataque1 == True:
                                    m_vida[id] -= dano1
                                    self.mush.hit_e(m_action[2], m_pos[id])
                                if ataque2 == True:
                                    m_vida[id] -= dano2
                                    self.mush.hit_e(m_action[2], m_pos[id])
                                if v_special == True:
                                    m_vida[id] -= atk_especial
                                    self.mush.hit_e(m_action[2], m_pos[id])
                            if loopt[id] < 10:
                                longe = True
                        # Fica parado se o jogador estiver muito longe
                        if longe == True and m_m[id] == False or m_y[id] - y_player > 50 and m_m[id] == False and m_action[5] == 30:
                            m_action[0] += 0.2
                            if m_action[0] >= 4:
                                m_action[0] = 0
                            if m_direita[id] == True:
                                self.mush.parado_d(m_action[0], m_pos[id])
                            if m_direita[id] == False:
                                self.mush.parado_e(m_action[0], m_pos[id])
                        if m_vida[id] <= 0:
                            if m_direita[id] == True:
                                m_action[3] += 0.3
                                self.mush.morte_d(m_action[3], m_pos[id])
                                m_m[id] = True
                            if m_direita[id] == False:
                                m_action[3] += 0.3
                                self.mush.morte_e(m_action[3], m_pos[id])
                                m_m[id] = True
                            if m_action[3] >= 19:
                                gera_mushroom[id] = False
                        if m_vida[id] > 0 and m_vida[id] < 30:
                            m_action[5] += 0.4
                            if m_action[5] > 37:
                                m_action[5] = 30
                                m_vida[id] += 50
                            self.mush.regenerate(m_action[5], m_pos[id])
        def flying_eye(self, id, x_player):
            if gera_fly[id] == True:
                    # Parado, Andando, Hit, Morte, Ataque
                    find = self.fly.identificar(x_player, f_pos[id])
                    longe = self.fly.far(x_player, f_pos[id])
                    f_direita[id] = self.fly.dist(x_player, f_pos[id])
                    # Se identificar o jogador, anda até ele
                    if find == True:
                        if f_direita[id] == True:
                            f_action[1] += 0.3
                            f_pos[id] += 5
                            if f_action[1] >= 9:
                                f_action[1] = 3
                            self.fly.andando_direita(f_action[1], f_pos[id])
                        if f_direita[id] == False:
                            f_action[1] += 0.3
                            f_pos[id] -= 5
                            if f_action[1] >= 9:
                                f_action[1] = 3
                            self.fly.andando_esquerda(f_action[1], f_pos[id])
                    # Se não identificar o jogador, fica parado
                    if find == False:
                        if longe == False and f_y[id] - y_player < 50:
                            if f_direita[id] == True and projetil_fly[id] == False:
                                loopt[id] += 0.2
                                if loopt[id] >= 10 and loopt[id] <= 14:
                                    f_action[4] += 0.3
                                    if f_action[4] >= 27:
                                        f_action[4] = 24
                                        projetil_fly[id] = True
                                    self.fly.ataque_d(f_action[4], f_pos[id])                                 
                                    if loopt[id] >= 13:
                                        loopt[id] = 0
                            if f_direita[id] == False and projetil_fly[id] == False:
                                loopt[id] += 0.2
                                if loopt[id] >= 10 and loopt[id] <= 14:
                                    f_action[4] += 0.3
                                    if f_action[4] >= 27:
                                        f_action[4] = 24
                                        projetil_fly[id] = True
                                    self.fly.ataque_e(f_action[4], f_pos[id])                               
                                    if loopt[id] >= 13:
                                        loopt[id] = 0
                            rec = x_player - f_pos[id]
                            if rec < 0:
                                rec = f_pos[id] - x_player
                            if rec < 30:
                                if direita == True:
                                    if ataque1 == True:
                                        f_vida[id] -= dano1
                                        self.fly.hit_d(f_action[2], f_pos[id])
                                    if ataque2 == True:
                                        f_vida[id] -= dano2
                                        self.fly.hit_d(f_action[2], f_pos[id])
                                    if v_special == True:
                                        f_vida[id] -= atk_especial
                                        self.fly.hit_d(f_action[2], f_pos[id])
                                if direita == False:
                                    if ataque1 == True:
                                        f_vida[id] -= dano1
                                        self.fly.hit_e(f_action[2], f_pos[id])
                                    if ataque2 == True:
                                        f_vida[id] -= dano2
                                        self.fly.hit_e(f_action[2], f_pos[id])
                                    if v_special == True:
                                        f_vida[id] -= atk_especial
                                        self.fly.hit_e(f_action[2], f_pos[id])
                            if projetil_fly[id] == True:
                                if pro_move[id] == 0:
                                    pro_move[id] = f_pos[id]
                                if f_direita[id] == True:
                                    pro_move[id] += 8
                                    if pro_move[id] / x_player < 1:
                                        projetil_fly[id] = False
                                        pro_move[id] = 0
                                        dano_geral.append(self.fly.dano)
                                    self.fly.projetil_d(0, pro_move[id])
                                if f_direita[id] == False:
                                    pro_move[id] -= 8
                                    if x_player == 0:
                                        x_player += 0.1
                                    if pro_move[id] / x_player < 1.5:
                                        projetil_fly[id] = False
                                        pro_move[id] = 0
                                        dano_geral.append(self.fly.dano)
                                    self.fly.projetil_e(0, pro_move[id])
                            if loopt[id] < 10:
                                longe = True
                        if longe == True and m_f[id] == False or f_y[id] - y_player > 50 and m_f[id] == False or projetil_fly[id] == True:
                            f_action[0] += 0.3
                            if f_action[0] >= 4:
                                f_action[0] = 0
                            if f_direita[id] == True:
                                self.fly.parado_d(f_action[0], f_pos[id])
                            if f_direita[id] == False:
                                self.fly.parado_e(f_action[0], f_pos[id])
                        if f_vida[id] <= 0:
                            if f_direita[id] == True:
                                f_action[3] += 0.3
                                self.fly.morte_d(f_action[3], f_pos[id])
                                m_f[id] = True
                            if f_direita[id] == False:
                                f_action[3] += 0.3
                                self.fly.morte_e(f_action[3], f_pos[id])
                                m_f[id] = True
                            if f_action[3] >= 16:
                                gera_fly[id] = False
   
    # JOGADOR
    # Jogador andando
    for rep in range(len(p_run)):
        run = player[0].subsurface(p_run[rep], (120, 80))
        run_all.append(run)
    # Jogador ataque 1
    for rep in range(len(p_at1)):
        at1 = player[1].subsurface(p_at1[rep], (120, 80))
        at1_all.append(at1)
    # Jogador ataque 2
    for rep in range(len(p_at2)):
        at2 = player[2].subsurface(p_at2[rep], (120, 80))
        at2_all.append(at2)
    # Jogador especial
    for rep in range(len(p_special)):
        especial = player[3].subsurface(p_special[rep], (120, 80))
        special_all.append(especial)
    # Jogador Parado
    for rep in range(len(p_idle)):
        idle = player[4].subsurface(p_idle[rep], (120, 80))
        idle_all.append(idle)
    # Jogador morte
    for rep in range(len(p_death)):
        death = player[5].subsurface(p_death[rep], (120, 80))
        death_all.append(death)  
    # Jogador dano
    hit_all.append(player[6].subsurface((0, 0), (120, 80)))
    # Jogador pulo
    for rep in range(len(p_jump)):
        jump = player[7].subsurface(p_jump[rep], (113, 76))
        jump_all.append(jump)  
    for l in range(len(pos)):
        hb = gui.subsurface(pos[l], tamanho[l])
        hb = p.transform.scale(hb, (size[0][0]/4, size[0][1]/6*0.8))
        gui_geral.append(hb)
    while True:    
    # Loop principal da parte 1
        if parte_chapter < 7 and parte_chapter != 0:
            while True:
                tiktak.tick(30)
                tela.fill(black)
                # Seletor de partes do capítulo
                if parte_chapter == 1:
                    forest = p.transform.scale(forest, (altura, comprimento))
                    tela.blit(forest, (0, 0))
                    if aprovado1 == False:
                        if x_player >= size[0][0]:
                            x_player = size[0][0]-10
                        tela.blit(font.render("Tutorial: Pressione < e > para se locomover", False, white), (80, size[0][1]-100))
                        tela.blit(font.render("Pressione as teclas Q e W para atacar", False, white), (80, size[0][1]-70))
                        tela.blit(font.render("Use espaço para pular", False, white), (80, size[0][1]-40))
                        if m_g[0] == False:
                            gera_goblin[0] = True
                        if m_m[0] == False:
                            gera_mushroom[0] = True
                        if m_f[0] == False:
                            gera_fly[0] = True
                    if gera_fly[0] == False and gera_goblin[0] == False and gera_mushroom[0] == False:
                        aprovado1 = True
                    if aprovado1 == True:
                        tela.blit(font.render("Agora que apareceu este símbolo estranho aí em cima, aperte backspace para usar seu ataque especial", False, white), (80, size[0][1]-100))
                        tela.blit(font.render("Ele sempre estará disponível aleatoriamente para você, fique atento", False, white), (80, size[0][1]-70))
                        for event in p.event.get():
                            if event.type == p.KEYDOWN:
                                if event.key == p.K_BACKSPACE:
                                    tutorial = True
                                    result = 70
                                else:
                                    result = 1
                        if tutorial == True:
                            tela.blit(font.render("Muito bem, seu tutorial foi concluído! Siga adiante para a próxima etapa e boa sorte.", False, white), (80, size[0][1]-40))
                        if x_player >= size[0][0]:
                            parte_chapter = 2
                            x_player = -230
                            vida = hp_max
                            aprovado1 = False
                if parte_chapter == 2:
                    arvores = p.transform.scale(arvores, (altura, comprimento))
                    tela.blit(arvores, (0,0))
                    if aprovado2 == False:
                        if x_player >= size[0][0]:
                            x_player = size[0][0]-10
                        if m_g[1] == False and m_g[2] == False and m_g[3] == False:
                            gera_goblin[1] = True
                            gera_goblin[2] = True
                            gera_goblin[3] = True
                        if m_f[1] == False and m_f[2] == False and m_f[3] == False:
                            gera_fly[1] = True
                            gera_fly[2] = True
                            gera_fly[3] = True
                        if m_g[1] == True and m_g[2] == True and m_g[3] == True and m_f[1] == True and m_f[2] == True and m_f[3] == True:
                            if m_g[4] == False and m_g[5] == False and m_g[6] == False and m_g[7] == False and m_m[1] == False and m_m[2] == False and m_m[3] == False and m_m[4] == False and m_m[5] == False:
                                if fala == False:
                                    if x_player > 0:
                                        direita = False
                                        andar = True
                                    if x_player <= 0:
                                        direita = True
                                        andar = False
                                    cfala += 1
                                    ar_fala = ["Ei, meu jovem, você aí! Espere!", "Fique atento, o rei morto virá atrás de você!", "Você é nossa única esperança para salvar este reino.","Agora vá embora, não perca mais tempo."]
                                    gui_geral[3] = p.transform.scale(gui_geral[3], (size[0][0]/2, size[0][1]/7))
                                    tela.blit(gui_geral[3], (size[0][0]-640, 130))
                                    if cfala < 150:
                                        tela.blit(fonte.render(ar_fala[0], False, black), (size[0][0]-600, 150))
                                    if cfala > 150 and cfala < 300:
                                        tela.blit(fonte.render(ar_fala[1], False, black), (size[0][0]-600, 150))
                                    if cfala > 300 and cfala < 450:
                                        tela.blit(fonte.render(ar_fala[2], False, black), (size[0][0]-600, 150))
                                    if cfala > 450:
                                        tela.blit(fonte.render(ar_fala[3], False, black), (size[0][0]-600, 150))
                                    if cfala > 500:
                                        fala = True
                                vida += 5
                                if fala == True:
                                    gera_goblin[4] = True
                                    gera_goblin[5] = True
                                    gera_goblin[6] = True
                                    gera_goblin[7] = True
                                    gera_mushroom[1] = True
                                    gera_mushroom[2] = True
                                    gera_mushroom[3] = True
                                    gera_mushroom[4] = True
                                    gera_mushroom[5] = True
                        if m_g[4] == True and m_g[5] == True and m_g[6] == True and m_g[7] == True and m_m[1] == True and m_m[2] == True and m_m[3] == True and m_m[4] == True and m_m[5] == True:
                            aprovado2 = True
                    if aprovado2 == True:
                        if x_player >= size[0][0]:
                            parte_chapter = 3
                            x_player = -230
                if parte_chapter == 3:
                    entrada = p.transform.scale(entrada, (altura*4, comprimento*2.3))
                    tela.blit(entrada,(-3250,-970))
                    if aprovado3 == False:
                        if x_player >= size[0][0]:
                            x_player = size[0][0]-10
                        if x_player >= size[0][0] -580:
                            x_player = size[0][0] -590
                        if x_player >= size[0][0]-900 and x_player <= size[0][0]-700:
                            if m_g[12] == False and m_g[11] == False and m_g[10] == False and m_g[9] == False and m_g[8] == False and m_g[13] == False:
                                gera_goblin[12] = True
                                gera_goblin[11] = True
                                gera_goblin[10] = True
                                gera_goblin[9] = True
                                gera_goblin[8] = True
                                gera_goblin[13] = True
                        if m_g[12] == True and m_g[11] == True and m_g[10] == True and m_g[9] == True and m_g[8] == True and m_g[13] == True:
                            aprovado3 = True
                    if aprovado3 == True:
                        if x_player >= size[0][0]-600:
                            parte_chapter = 4
                            x_player = -230
                            vida += 10
                            entrada = p.transform.scale(entrada, (altura,comprimento))
                            tela.blit(entrada,(0,0))
                            tela.blit(carregamento.render("Entrando no castelo...", False, black), ((size[0][0]/2)-200, (size[0][1]/2)))
                            p.display.update()
                            sleep(7)
                # Parte do interior do castelo
                if parte_chapter == 4:
                    # Preparação para interior do castelo
                    castelo1 = p.transform.scale(castelo1, (altura,comprimento))
                    dano1level = 3
                    dano2level = 4
                    tela.blit(castelo1, (0,70))
                    if aprovado4 == False:
                        if x_player >= size[0][0]:
                            x_player = size[0][0]-10
                        if m_f[6] == False and m_f[7] == False and m_f[8] == False and m_f[9] == False and m_f[10] == False and m_f[11] == False and m_f[12] == False and m_f[13] == False and m_f[14] == False and m_f[15] == False and x_player > 700 and x_player < 900:
                            gera_fly[6] = True
                            gera_fly[7] = True
                            gera_fly[8] = True
                            gera_fly[9] = True
                            gera_fly[10] = True
                            gera_fly[11] = True
                            gera_fly[12] = True
                            gera_fly[13] = True
                            gera_fly[14] = True
                            gera_fly[15] = True
                        if m_f[6] == True and m_f[7] == True and m_f[8] == True and m_f[9] == True and m_f[10] == True and m_f[11] == True and m_f[12] == True and m_f[13] == True and m_f[14] == True and m_f[15] == True: 
                            if fala2 == False:
                                cfala2 += 1
                                gui_geral[3] = p.transform.scale(gui_geral[3], (size[0][0]/1.8, 150))
                                tela.blit(gui_geral[3], (400,180))
                                if cfala2 < 300 and cfala2 >= 30:
                                    tela.blit(fonte.render(fala_rei[0], False, (200,0,0)), (470,200))
                                if cfala2 > 300 and cfala2 < 600:
                                    tela.blit(fonte.render(fala_rei[1], False, (200,0,0)), (470,200))
                                if cfala2 > 600 and cfala2 < 800:
                                    tela.blit(fonte.render(fala_rei[2], False, black), (450,200))
                                    tela.blit(fonte.render(fala_rei[3], False, black), (450,250))
                                if cfala2 >= 800:
                                    fala2 = True
                            if fala2 == True:    
                                aprovado4 = True
                    if aprovado4 == True:
                        if x_player >= size[0][0]:
                            parte_chapter = 5
                            vida +=10
                            x_player = -230
                if parte_chapter == 5:
                    castelo2 = p.transform.scale(castelo2, (altura,comprimento))
                    tela.blit(castelo2, (0,70))
                    if aprovado5 == False:
                        if x_player >= size[0][0]:
                            x_player = size[0][0]-10
                        if m_g[14] == False and m_g[15] == False and m_g[16] == False and m_g[17] == False and m_g[18] == False and m_m[6] == False and m_m[7] == False and m_m[8] == False and m_m[9] == False and m_m[10] == False:
                            gera_goblin[14] = True
                            gera_goblin[15] = True
                            gera_goblin[16] = True
                            gera_goblin[17] = True
                            gera_goblin[18] = True
                            gera_mushroom[6] = True
                            gera_mushroom[7] = True
                            gera_mushroom[8] = True
                            gera_mushroom[9] = True
                            gera_mushroom[10] = True
                        if m_g[14] == True and m_g[15] == True and m_g[16] == True and m_g[17] == True and m_g[18] == True and m_m[6] == True and m_m[7] == True and m_m[8] == True and m_m[9] == True and m_m[10] == True:                       
                            if m_g[19] == False and m_g[20] == False and m_g[21] == False and m_g[22] == False and m_g[23] == False:
                                gera_goblin[19] = True
                                gera_goblin[20] = True
                                gera_goblin[21] = True
                                gera_goblin[22] = True
                                gera_goblin[23] = True
                            if m_g[19] == True and m_g[20] == True and m_g[21] == True and m_g[22] == True and m_g[23] == True: 
                                aprovado5 = True
                    if aprovado5 == True:
                        if x_player >= size[0][0]:
                            x_player = -230
                            vida += 13
                            parte_chapter = 6
                if parte_chapter == 6:
                    castelo3 = p.transform.scale(castelo3, (altura, comprimento))
                    tela.blit(castelo3, (0,0))
                    hp_max = 70
                    if aprovado6 == False:
                        if m_g[24] == False and m_g[25] == False and m_g[26] == False and m_m[11] == False and m_m[12] == False and m_m[13] == False:
                            gera_goblin[24] = True
                            gera_goblin[25] = True
                            gera_goblin[26] = True
                            gera_mushroom[11] = True
                            gera_mushroom[12] = True
                            gera_mushroom[13] = True
                        if m_g[24] == True and m_g[25] == True and m_g[26] == True and m_m[11] == True and m_m[12] == True and m_m[13] == True:
                            if m_f[16] == False:
                                gera_fly[16] = True
                            if m_f[16] == True:
                                aprovado6 = True
                                vida = hp_max+10
                    if aprovado6 == True:
                        parte_chapter = 0
                        break
                if x_player <= -300:
                    x_player = -200
                # Seletor de eventos
                if vida > hp_max:
                    vida = hp_max
                # Validador de especial
                special = randint(0, 10000)
                if special <= 1:
                    result = special
                if result <= 1:
                    tela.blit(gui_geral[2], (300,0))
                for event in p.event.get():
                    # Sair da tela
                    if event.type == p.KEYDOWN:
                        if event.key == p.K_LSHIFT or event.key == p.K_RSHIFT:
                            valida_save = pausar(tela, size, vida, hp_max, result)
                            p.init()
                            cx = x_player
                            cy = y_player
                            if valida_save[0] == True:
                                lista = [f"{nivel}", f"{hp_max}", f"{vida}", f"{atk_especial}", f"{parte_chapter}", f"{cx}", f"{cy}"]
                            if valida_save[1] == True:
                                lista = [f"{nivel}", f"{hp_max}", f"{vida}", f"{atk_especial}", f"{parte_chapter}", f"{cx}", f"{cy}"]
                                sair = True
                                break
                        if event.key == p.K_ESCAPE:
                            valida = tem_certeza()
                            if valida == True:
                                sair = True
                                break
            # Ações do JOGADOR
                        # Caso: Comando pulo
                        if event.key == p.K_SPACE:
                            pulo = True
                        # Caso: Comando Ataque1
                        if event.key == p.K_q:
                            ataque1 = True
                            dano1 = dano1level
                        # Caso: Comando Ataque 2
                        if event.key == p.K_w:
                            ataque2 = True
                            dano2 = dano2level
                        # Caso: Comando Especial
                        if event.key == p.K_BACKSPACE:
                            if result <= 1:
                                v_special = True
                                result = 70
                # Caso: Morte
                if vida <= 0:
                    fall += 0.5
                    if fall >= len(death_all):
                        fall = len(p_death)-1
                        death_player = True
                    if direita == True:
                        death_all[int(fall)] = p.transform.scale(death_all[int(fall)], (int(altura/multi_x), int(comprimento/multi_y)))
                        tela.blit(death_all[int(fall)], (x_player, y_player))
                    if direita == False:
                        death_all[int(fall)] = p.transform.flip(death_all[int(fall)], True, False)
                        death_all[int(fall)] = p.transform.scale(death_all[int(fall)], (int(altura/multi_x), int(comprimento/multi_y)))
                        tela.blit(death_all[int(fall)], (x_player, y_player))
                        death_all[int(fall)] = p.transform.flip(death_all[int(fall)], True, False)
                # Caso: ataque 1
                # Direção do golpe
                if direita == False:
                    at1_right = at1_all[:]
                    for esq in range(len(p_at1)):
                        at1_right[esq] = p.transform.flip(at1_all[esq], True, False)
                    at1_all = at1_right[:]
                # Execução do golpe
                if ataque1 == True:
                    stop = False
                    if atk < len(p_at1):
                        atk += 0.8
                    if atk >= len(p_at1): 
                        atk = 0
                        stop = True
                        ataque1 = False
                    at1_all[int(atk)] = p.transform.scale(at1_all[int(atk)], (int(altura/multi_x), int(comprimento/multi_y)))
                    # Desenhar imagem
                    tela.blit(at1_all[int(atk)], (x_player, y_player))
                # Correção da direção
                if direita == False:
                    at1_right = at1_all[:]
                    for esq in range(len(p_at1)):
                        at1_right[esq] = p.transform.flip(at1_all[esq], True, False)
                    at1_all = at1_right[:]
                # Caso: ataque 2
                # Direção do golpe
                if direita == False:
                    at2_right = at2_all[:]
                    for esq in range(len(p_at2)):
                        at2_right[esq] = p.transform.flip(at2_all[esq], True, False)
                    at2_all = at2_right[:]
                # Execução do golpe
                if ataque2 == True:
                    stop = False
                    if atk < len(p_at2):
                        atk += 0.8
                    if atk >= len(p_at2): 
                        atk = 0
                        stop = True
                        ataque2 = False
                    at2_all[int(atk)] = p.transform.scale(at2_all[int(atk)], (int(altura/multi_x), int(comprimento/multi_y)))
                    # Desenhar imagem
                    tela.blit(at2_all[int(atk)], (x_player, y_player))
                # Correção da direção do golpe
                if direita == False:
                    at2_right = at2_all[:]
                    for esq in range(len(p_at2)):
                        at2_right[esq] = p.transform.flip(at2_all[esq], True, False)
                    at2_all = at2_right[:]
                # Caso: especial
                # Direção do golpe
                if direita == False:
                    special_right = special_all[:]
                    for esq in range(len(p_special)):
                        special_right[esq] = p.transform.flip(special_all[esq], True, False)
                    special_all = special_right[:]
                # Execução do golpe
                if v_special == True:
                    stop = False
                    if atk < len(p_special):
                        atk += 0.34
                    if atk >= len(p_special): 
                        atk = 0
                        stop = True
                        v_special = False
                    special_all[int(atk)] = p.transform.scale(special_all[int(atk)], (int(altura/multi_x), int(comprimento/multi_y)))
                    # Desenhar imagem
                    tela.blit(special_all[int(atk)], (x_player, y_player))
                # Correção da direção do golpe
                if direita == False:
                    special_right = special_all[:]
                    for esq in range(len(p_special)):
                        special_right[esq] = p.transform.flip(special_all[esq], True, False)
                    special_all = special_right[:]
                # Caso: Pulo
                # Definir direção do trajeto
                if direita == False:
                    jump_right = jump_all[:]
                    for esq in range(len(p_jump)):
                        jump_right[esq] = p.transform.flip(jump_all[esq], True, False)
                    jump_all = jump_right[:]
                # Pulo: subida
                if pulo == True:
                    stop = False
                    y_player -= 10
                    if y_player == chao - 10:
                        pulando = 0
                    else:
                        pulando = 1
                    if p.key.get_pressed()[p.K_RIGHT] == False and p.key.get_pressed()[p.K_LEFT] == False:
                        jump_all[int(pulando)] = p.transform.scale(jump_all[int(pulando)], (int(altura/multi_x), int(comprimento/multi_y)))
                    # Desenhar imagem
                        tela.blit(jump_all[int(pulando)], (x_player, y_player))
                # Pulo: apse
                if y_player == chao - 100:
                    pulo = False
                    pulando = 2
                    if p.key.get_pressed()[p.K_RIGHT] == False and p.key.get_pressed()[p.K_LEFT] == False:
                        jump_all[int(pulando)] = p.transform.scale(jump_all[int(pulando)], (int(altura/multi_x), int(comprimento/multi_y)))
                        # Desenhar imagem
                        tela.blit(jump_all[int(pulando)], (x_player, y_player))
                # Pulo descida
                if pulo == False and y_player <= chao:
                    y_player += 10
                    if y_player == chao - 50:
                        pulando = 3
                    else:
                        pulando = 4
                        stop = True
                    if p.key.get_pressed()[p.K_RIGHT] == False and p.key.get_pressed()[p.K_LEFT] == False:
                        jump_all[int(pulando)] = p.transform.scale(jump_all[int(pulando)], (int(altura/multi_x), int(comprimento/multi_y)))
                        # Desenhar imagem
                        tela.blit(jump_all[int(pulando)], (x_player, y_player))
                # Retorna imagem para formato original
                if direita == False:
                    jump_right = jump_all[:]
                    for esq in range(len(p_jump)):
                        jump_right[esq] = p.transform.flip(jump_all[esq], True, False)
                    jump_all = jump_right[:]
                # Dano do jogador
                if len(dano_geral) > 0:
                    for rep in range(len(dano_geral)):
                        vida -= dano_geral[rep]
                    if direita == True:
                        hit_all[0] = p.transform.scale(hit_all[0], (int(altura/multi_x), int(comprimento/multi_y)))
                        tela.blit(hit_all[0], (x_player, y_player))
                    if direita == False:
                        hit_all[0] = p.transform.flip(hit_all[0], True, False)
                        hit_all[0] = p.transform.scale(hit_all[0], (int(altura/multi_x), int(comprimento/multi_y)))
                        tela.blit(hit_all[0], (x_player, y_player))
                        hit_all[0] = p.transform.flip(hit_all[0], True, False)
                # Caso: andar para esquerda             
                if p.key.get_pressed()[p.K_LEFT] == True and p.key.get_pressed()[p.K_RIGHT] == False or andar == True:
                    x_player -= 10
                    if andando >= (len(run_all)-1):
                        andando = 0
                    else:
                        andando += 0.5
                    direita = False
                    # Inverter imagem para esquerda
                    run_allleft = run_all[:]
                    run_allleft[int(andando)] = p.transform.flip(run_all[int(andando)], True, False)
                    run_allleft[int(andando)] = p.transform.scale(run_allleft[int(andando)], (int(altura/multi_x), int(comprimento/multi_y)))
                    # Desenhar imagem
                    tela.blit(run_allleft[int(andando)], (x_player, y_player))
                # Caso: andar para direita
                if p.key.get_pressed()[p.K_RIGHT] and p.key.get_pressed()[p.K_LEFT] == False:
                    x_player += 10
                    if andando >= (len(run_all)-1):
                        andando = 0
                    else:
                        andando += 0.5
                    direita = True
                    run_all[int(andando)] = p.transform.scale(run_all[int(andando)], (int(altura/multi_x), int(comprimento/multi_y)))
                    tela.blit(run_all[int(andando)], (x_player, y_player))
                # Caso: Parado
                if p.key.get_pressed()[p.K_RIGHT] == False and p.key.get_pressed()[p.K_LEFT] == False and stop == True and len(dano_geral) == 0 and death_player == False:
                    if direita == False:
                        idle_right = idle_all[:]
                        for esq in range(len(p_idle)):
                            idle_right[esq] = p.transform.flip(idle_all[esq], True, False)
                        idle_all = idle_right[:]
                    if parado >= (len(idle_all)-1):
                        parado = 0
                    else:
                        parado += 0.34
                    idle_all[int(parado)] = p.transform.scale(idle_all[int(parado)], (int(altura/multi_x), int(comprimento/multi_y)))
                    tela.blit(idle_all[int(parado)], (x_player, y_player))
                    if direita == False:
                        idle_right = idle_all[:]
                        for esq in range(len(p_idle)):
                            idle_right[esq] = p.transform.flip(idle_all[esq], True, False)
                        idle_all = idle_right[:]
                
                # CORRETOR DE DANO
                dano_geral.clear()
                # GERAR GOBLINS
                goblin00 = roda_game()
                goblin00.goblin(0)
                goblin01 = roda_game()
                goblin01.goblin(1)
                goblin02 = roda_game()
                goblin02.goblin(2)
                goblin03 = roda_game()
                goblin03.goblin(3)
                goblin04 = roda_game()
                goblin04.goblin(4)
                goblin05 = roda_game()
                goblin05.goblin(5)
                goblin06 = roda_game()
                goblin06.goblin(6)
                goblin07 = roda_game()
                goblin07.goblin(7)
                goblin08 = roda_game()
                goblin08.goblin(8)
                goblin09 = roda_game()
                goblin09.goblin(9)
                goblin10 = roda_game()
                goblin10.goblin(10)
                goblin11 = roda_game()
                goblin11.goblin(11)
                goblin12 = roda_game()
                goblin12.goblin(12)
                goblin13 = roda_game()
                goblin13.goblin(13)
                goblin14 = roda_game()
                goblin14.goblin(14)
                goblin15 = roda_game()
                goblin15.goblin(15)
                goblin16 = roda_game()
                goblin16.goblin(16)
                goblin17 = roda_game()
                goblin17.goblin(17)
                goblin18 = roda_game()
                goblin18.goblin(18)
                goblin19 = roda_game()
                goblin19.goblin(19)
                goblin20 = roda_game()
                goblin20.goblin(20)
                goblin21 = roda_game()
                goblin21.goblin(21)
                goblin22 = roda_game()
                goblin22.goblin(22)
                goblin23 = roda_game()
                goblin23.goblin(23)
                goblin24 = roda_game()
                goblin24.goblin(24)
                goblin25 = roda_game()
                goblin25.goblin(25)
                goblin26 = roda_game()
                goblin26.goblin(26)
                # GERAR MUSHROOMS
                mushroom00 = roda_game()
                mushroom00.mushroom(0)
                mushroom01 = roda_game()
                mushroom01.mushroom(1)
                mushroom02 = roda_game()
                mushroom02.mushroom(2)
                mushroom03 = roda_game()
                mushroom03.mushroom(3)
                mushroom04 = roda_game()
                mushroom04.mushroom(4)
                mushroom05 = roda_game()
                mushroom05.mushroom(5)
                mushroom06 = roda_game()
                mushroom06.mushroom(6)
                mushroom07 = roda_game()
                mushroom07.mushroom(7)
                mushroom08 = roda_game()
                mushroom08.mushroom(8)
                mushroom09 = roda_game()
                mushroom09.mushroom(9)
                mushroom10 = roda_game()
                mushroom10.mushroom(10)
                mushroom11 = roda_game()
                mushroom11.mushroom(11)
                mushroom12 = roda_game()
                mushroom12.mushroom(12)
                mushroom13 = roda_game()
                mushroom13.mushroom(13)
                # GERAR OLHOS VOADORES
                flying00 = roda_game()
                flying00.flying_eye(0, x_player)
                flying01 = roda_game()
                flying01.flying_eye(1, x_player)
                flying02 = roda_game()
                flying02.flying_eye(2, x_player)
                flying03 = roda_game()
                flying03.flying_eye(3, x_player)
                flying04 = roda_game()
                flying04.flying_eye(4, x_player)
                flying05 = roda_game()
                flying05.flying_eye(5, x_player)
                flying06 = roda_game()
                flying06.flying_eye(6, x_player)
                flying07 = roda_game()
                flying07.flying_eye(7, x_player)
                flying08 = roda_game()
                flying08.flying_eye(8, x_player)
                flying09 = roda_game()
                flying09.flying_eye(9, x_player)
                flying10 = roda_game()
                flying10.flying_eye(10, x_player)
                flying11 = roda_game()
                flying11.flying_eye(11, x_player)
                flying12 = roda_game()
                flying12.flying_eye(12, x_player)
                flying13 = roda_game()
                flying13.flying_eye(13, x_player)
                flying14 = roda_game()
                flying14.flying_eye(14, x_player)
                flying15 = roda_game()
                flying15.flying_eye(15, x_player)
                flying16 = roda_game()
                flying16.flying_eye(16, x_player)
                if death_player == True:
                    break
                if sair == True:
                    p.quit()
                    break
                op = size[0][0]/4*vida/hp_max
                gui_geral[0] = p.transform.scale(gui_geral[0], (size[0][0]/4, size[0][1]/6*0.8))
                gui_geral[1] = p.transform.scale(gui_geral[1], (op, size[0][1]/6*0.8))
                tela.blit(gui_geral[0], (0, 0))
                tela.blit(gui_geral[1], (50,0))
                p.display.flip() # Atualiza a tela
        # Sala boss
        sleep(3)
        if parte_chapter == 0: 
            # Variáveis contra o boss
            x_final = 0
            y_final = 0
            enter = 43.0
            dano1level = 5
            dano2level = 6.5
            atk_especial = 20
            cfala = 0
            cfala2 = 0
            count_fala = 0
            count_ataque = 0
            while True:
                tiktak.tick(30)
                tela.fill(black)
                castelo3 = p.transform.scale(castelo3, (altura, comprimento))
                tela.blit(castelo3, (x_final,y_final))
                special = randint(0, 10000)
                count_ataque += 1
                if special <= 1:
                    result = special
                if result <= 1:
                    tela.blit(gui_geral[2], (300,0))
                for event in p.event.get():
                    # Sair da tela
                    if event.type == p.KEYDOWN:
                        if event.key == p.K_LSHIFT or event.key == p.K_RSHIFT:
                            valida_save = pausar(tela, size, vida, hp_max, result)
                            if valida_save[1] == True:
                                sair = True
                                break
                        if event.key == p.K_ESCAPE:
                            valida = tem_certeza()
                            if valida == True:
                                sair = True
                                break
                        # Ações do JOGADOR
                        # Caso: Comando pulo
                        if event.key == p.K_SPACE:
                            pulo = True
                        # Caso: Comando Ataque1
                        if event.key == p.K_q and count_ataque % 3:
                            ataque1 = True
                            boss_sofre = True
                            dano1 = dano1level
                        # Caso: Comando Ataque 2
                        if event.key == p.K_w and count_ataque % 3:
                            ataque2 = True
                            boss_sofre = True
                            dano2 = dano2level
                        # Caso: Comando Especial
                        if event.key == p.K_BACKSPACE:
                            if result <= 1:
                                v_special = True
                                boss_sofre = True
                                result = 70
                # Caso: andar para esquerda
                if p.key.get_pressed()[p.K_LEFT] and p.key.get_pressed()[p.K_RIGHT] == False or andar == True:
                    x_player -= 10
                    if andando >= (len(run_all)-1):
                        andando = 0
                    else:
                        andando += 0.5
                    direita = False
                    # Inverter imagem para esquerda
                    run_allleft = run_all[:]
                    run_allleft[int(andando)] = p.transform.flip(run_all[int(andando)], True, False)
                    run_allleft[int(andando)] = p.transform.scale(run_allleft[int(andando)], (int(altura/multi_x), int(comprimento/multi_y)))
                    # Desenhar imagem
                    tela.blit(run_allleft[int(andando)], (x_player, y_player))
                # Caso: andar para direita
                if p.key.get_pressed()[p.K_RIGHT] and p.key.get_pressed()[p.K_LEFT] == False:
                    x_player += 10
                    if andando >= (len(run_all)-1):
                        andando = 0
                    else:
                        andando += 0.5
                    direita = True
                    run_all[int(andando)] = p.transform.scale(run_all[int(andando)], (int(altura/multi_x), int(comprimento/multi_y)))
                    tela.blit(run_all[int(andando)], (x_player, y_player))
                # Caso: Morte
                if vida <= 0:
                    fall += 0.5
                    if fall >= len(death_all):
                        fall = len(p_death)-1
                        death_player = True
                    if direita == True:
                        death_all[int(fall)] = p.transform.scale(death_all[int(fall)], (int(altura/multi_x), int(comprimento/multi_y)))
                        tela.blit(death_all[int(fall)], (x_player, y_player))
                    if direita == False:
                        death_all[int(fall)] = p.transform.flip(death_all[int(fall)], True, False)
                        death_all[int(fall)] = p.transform.scale(death_all[int(fall)], (int(altura/multi_x), int(comprimento/multi_y)))
                        tela.blit(death_all[int(fall)], (x_player, y_player))
                        death_all[int(fall)] = p.transform.flip(death_all[int(fall)], True, False)
                # Caso: ataque 1
                # Direção do golpe
                if direita == False:
                    at1_right = at1_all[:]
                    for esq in range(len(p_at1)):
                        at1_right[esq] = p.transform.flip(at1_all[esq], True, False)
                    at1_all = at1_right[:]
                # Execução do golpe
                if ataque1 == True:
                    stop = False
                    if atk < len(p_at1):
                        atk += 0.8
                    if atk >= len(p_at1): 
                        atk = 0
                        stop = True
                        ataque1 = False
                    at1_all[int(atk)] = p.transform.scale(at1_all[int(atk)], (int(altura/multi_x), int(comprimento/multi_y)))
                    # Desenhar imagem
                    tela.blit(at1_all[int(atk)], (x_player, y_player))
                # Correção da direção
                if direita == False:
                    at1_right = at1_all[:]
                    for esq in range(len(p_at1)):
                        at1_right[esq] = p.transform.flip(at1_all[esq], True, False)
                    at1_all = at1_right[:]
                # Caso: ataque 2
                # Direção do golpe
                if direita == False:
                    at2_right = at2_all[:]
                    for esq in range(len(p_at2)):
                        at2_right[esq] = p.transform.flip(at2_all[esq], True, False)
                    at2_all = at2_right[:]
                # Execução do golpe
                if ataque2 == True:
                    stop = False
                    if atk < len(p_at2):
                        atk += 0.8
                    if atk >= len(p_at2): 
                        atk = 0
                        stop = True
                        ataque2 = False
                    at2_all[int(atk)] = p.transform.scale(at2_all[int(atk)], (int(altura/multi_x), int(comprimento/multi_y)))
                    # Desenhar imagem
                    tela.blit(at2_all[int(atk)], (x_player, y_player))
                # Correção da direção do golpe
                if direita == False:
                    at2_right = at2_all[:]
                    for esq in range(len(p_at2)):
                        at2_right[esq] = p.transform.flip(at2_all[esq], True, False)
                    at2_all = at2_right[:]
                # Caso: especial
                # Direção do golpe
                if direita == False:
                    special_right = special_all[:]
                    for esq in range(len(p_special)):
                        special_right[esq] = p.transform.flip(special_all[esq], True, False)
                    special_all = special_right[:]
                # Execução do golpe
                if v_special == True:
                    stop = False
                    if atk < len(p_special):
                        atk += 0.34
                    if atk >= len(p_special): 
                        atk = 0
                        stop = True
                        v_special = False
                    special_all[int(atk)] = p.transform.scale(special_all[int(atk)], (int(altura/multi_x), int(comprimento/multi_y)))
                    # Desenhar imagem
                    tela.blit(special_all[int(atk)], (x_player, y_player))
                # Correção da direção do golpe
                if direita == False:
                    special_right = special_all[:]
                    for esq in range(len(p_special)):
                        special_right[esq] = p.transform.flip(special_all[esq], True, False)
                    special_all = special_right[:]
                # Caso: Pulo
                # Definir direção do trajeto
                if direita == False:
                    jump_right = jump_all[:]
                    for esq in range(len(p_jump)):
                        jump_right[esq] = p.transform.flip(jump_all[esq], True, False)
                    jump_all = jump_right[:]
                # Pulo: subida
                if pulo == True:
                    stop = False
                    y_player -= 10
                    if y_player == chao - 10:
                        pulando = 0
                    else:
                        pulando = 1
                    if p.key.get_pressed()[p.K_RIGHT] == False and p.key.get_pressed()[p.K_LEFT] == False:
                        jump_all[int(pulando)] = p.transform.scale(jump_all[int(pulando)], (int(altura/multi_x), int(comprimento/multi_y)))
                    # Desenhar imagem
                        tela.blit(jump_all[int(pulando)], (x_player, y_player))
                # Pulo: apse
                if y_player == chao - 100:
                    pulo = False
                    pulando = 2
                    if p.key.get_pressed()[p.K_RIGHT] == False and p.key.get_pressed()[p.K_LEFT] == False:
                        jump_all[int(pulando)] = p.transform.scale(jump_all[int(pulando)], (int(altura/multi_x), int(comprimento/multi_y)))
                        # Desenhar imagem
                        tela.blit(jump_all[int(pulando)], (x_player, y_player))
                # Pulo descida
                if pulo == False and y_player <= chao:
                    y_player += 10
                    if y_player == chao - 50:
                        pulando = 3
                    else:
                        pulando = 4
                        stop = True
                    if p.key.get_pressed()[p.K_RIGHT] == False and p.key.get_pressed()[p.K_LEFT] == False:
                        jump_all[int(pulando)] = p.transform.scale(jump_all[int(pulando)], (int(altura/multi_x), int(comprimento/multi_y)))
                        # Desenhar imagem
                        tela.blit(jump_all[int(pulando)], (x_player, y_player))
                # Retorna imagem para formato original
                if direita == False:
                    jump_right = jump_all[:]
                    for esq in range(len(p_jump)):
                        jump_right[esq] = p.transform.flip(jump_all[esq], True, False)
                    jump_all = jump_right[:]
                # Dano do jogador
                if len(dano_geral) > 0:
                    for rep in range(len(dano_geral)):
                        vida -= dano_geral[rep]
                    if direita == True:
                        hit_all[0] = p.transform.scale(hit_all[0], (int(altura/multi_x), int(comprimento/multi_y)))
                        tela.blit(hit_all[0], (x_player, y_player))
                    if direita == False:
                        hit_all[0] = p.transform.flip(hit_all[0], True, False)
                        hit_all[0] = p.transform.scale(hit_all[0], (int(altura/multi_x), int(comprimento/multi_y)))
                        tela.blit(hit_all[0], (x_player, y_player))
                        hit_all[0] = p.transform.flip(hit_all[0], True, False)
                # Caso: Parado
                if p.key.get_pressed()[p.K_RIGHT] == False and p.key.get_pressed()[p.K_LEFT] == False and stop == True and len(dano_geral) == 0 and death_player == False:
                    if direita == False:
                        idle_right = idle_all[:]
                        for esq in range(len(p_idle)):
                            idle_right[esq] = p.transform.flip(idle_all[esq], True, False)
                        idle_all = idle_right[:]
                    if parado >= (len(idle_all)-1):
                        parado = 0
                    else:
                        parado += 0.34
                    idle_all[int(parado)] = p.transform.scale(idle_all[int(parado)], (int(altura/multi_x), int(comprimento/multi_y)))
                    tela.blit(idle_all[int(parado)], (x_player, y_player))
                    if direita == False:
                        idle_right = idle_all[:]
                        for esq in range(len(p_idle)):
                            idle_right[esq] = p.transform.flip(idle_all[esq], True, False)
                        idle_all = idle_right[:]
                 # CORRETOR DE DANO
                dano_geral.clear()
                # Invocação do boss
                if chefao == False:
                    # Entrada
                    fala2 = False
                    y_boss += 25
                    if y_boss >= 0 and y_boss < chao-100:
                        enter = 38
                    if y_boss >= chao-100 and y_boss < chao-50:
                        enter = 39
                    if y_boss >= chao:
                        y_boss = chao
                        enter = 30
                        count_fala += 1
                        if count_fala == 1:
                            x_final -= 10
                            y_final += 10
                        if count_fala == 3:
                            x_final += 10
                            y_final -= 10
                        if count_fala == 5:
                            x_final -= 10
                            y_final += 10
                        if count_fala == 7:
                            x_final += 10
                            y_final -= 10
                        if count_fala < 300:
                            gui_geral[3] = p.transform.scale(gui_geral[3], (size[0][0]/2.6, size[0][1]/7.2))
                            tela.blit(gui_geral[3], (450, (size[0][1]/2)-30))
                        if count_fala < 150:
                            tela.blit(fonte.render(fala_rei[4], False, black), (500, size[0][1]/2))
                        if count_fala > 150 and count_fala < 300:
                            tela.blit(fonte.render(fala_rei[5], False, (200,0,0)), (500, size[0][1]/2))
                        if count_fala > 300:
                            chefao = True
                            count_fala = 0
                    boss_sprites[int(enter)] = p.transform.scale(boss_sprites[int(enter)], (multi_x*150, multi_y*150))
                    tela.blit(boss_sprites[int(enter)], (x_boss, y_boss))
                # Parte jogável do boss
                if chefao == True:
                    # Condiciona o ataque
                    anterior += 1
                    if anterior > 25:
                        anterior = 0
                    # Longe
                    distancia = x_player - x_boss
                    if distancia < 0:
                        distancia = distancia * -1
                    if distancia > 50:
                        ande = True
                    if distancia <= 50:
                        ande = False
                    # Definição de direção
                    if x_player < x_boss and boss_morre == False:
                        boss_direita = False
                    if x_player > x_boss and boss_morre == False:
                        boss_direita = True
                    # Ações do boss
                    # Morte
                    if boss_vida <= 0 and finish == True:
                        boss_ataca = False
                        boss_anda = False
                        boss_sofre = False
                        boss_morre = True
                        result = 0
                        boss_vida = 0.1
                    if boss_morre == True:
                        # Efeito especial (fatality)
                        if finish == True:
                            tela.blit(fonte.render(fala_rei[6], True, white), (x_boss,y_boss-20))
                        if result == 0:
                            if boss_direita == True:
                                boss_sprites[30] = p.transform.scale(boss_sprites[30], (multi_x*150,multi_y*150))
                                tela.blit(boss_sprites[30], (x_boss,y_boss))
                            if boss_direita == False:
                                boss_sprites[30] = p.transform.scale(boss_sprites[30], (multi_x*150,multi_y*150))
                                boss_sprites[30] = p.transform.flip(boss_sprites[30], True, False)
                                tela.blit(boss_sprites[30], (x_boss,y_boss))
                                boss_sprites[30] = p.transform.flip(boss_sprites[30], True, False)
                        if v_special == True:
                            finish = False
                            result = 70
                            boss_action[7] += 0.3
                            if boss_action[7] >= 34:
                                boss_action[7] = 34
                            if boss_direita == True:
                                boss_sprites[int(boss_action[7])] = p.transform.scale(boss_sprites[int(boss_action[7])], (multi_x*150,multi_y*150))
                                tela.blit(boss_sprites[int(boss_action[7])], (x_boss,y_boss))
                            if boss_direita == False:
                                boss_sprites[int(boss_action[7])] = p.transform.scale(boss_sprites[int(boss_action[7])], (multi_x*150,multi_y*150))
                                boss_sprites[int(boss_action[7])] = p.transform.flip(boss_sprites[int(boss_action[7])], True, False)
                                tela.blit(boss_sprites[int(boss_action[7])], (x_boss,y_boss))
                                boss_sprites[int(boss_action[7])] = p.transform.flip(boss_sprites[int(boss_action[7])], True, False)
                        if finish == False:
                            nivel = 2
                            lista = [f"{nivel}", "80", "80", "30", "0", "0", f"{chao}"]
                            tela.blit(fonte.render("Siga em frente nobre guerreiro!", True, white), (x_boss,y_boss-20))
                            if x_player >= size[0][0]:
                                p.quit()
                                break
                            if boss_direita == True:
                                boss_sprites[34] = p.transform.scale(boss_sprites[34], (multi_x*150,multi_y*150))
                                tela.blit(boss_sprites[34], (x_boss,y_boss))
                            if boss_direita == False:
                                boss_sprites[34] = p.transform.scale(boss_sprites[34], (multi_x*150,multi_y*150))
                                boss_sprites[34] = p.transform.flip(boss_sprites[34], True, False)
                                tela.blit(boss_sprites[34], (x_boss,y_boss))
                                boss_sprites[34] = p.transform.flip(boss_sprites[34], True, False)
                    # Ações com base em distância (longe)
                    if ande == True:
                        boss_ataca = False
                        boss_sofre = False
                        boss_anda = True
                        # Correr + ataque 
                        # Andar
                        if boss_anda == True and boss_morre == False:
                            boss_action[1] += 0.2
                            if boss_action[1] >= 11:
                                boss_action[1] = 3
                            if boss_direita == True:
                                x_boss += 1
                                boss_sprites[int(boss_action[1])] = p.transform.scale(boss_sprites[int(boss_action[1])], (multi_x*150,multi_y*150))
                                tela.blit(boss_sprites[int(boss_action[1])], (x_boss,y_boss))
                            if boss_direita == False:
                                x_boss -= 1
                                boss_sprites[int(boss_action[1])] = p.transform.scale(boss_sprites[int(boss_action[1])], (multi_x*150,multi_y*150))
                                boss_sprites[int(boss_action[1])] = p.transform.flip(boss_sprites[int(boss_action[1])], True, False)
                                tela.blit(boss_sprites[int(boss_action[1])], (x_boss,y_boss))
                                boss_sprites[int(boss_action[1])] = p.transform.flip(boss_sprites[int(boss_action[1])], True, False)
                    # Parado
                    if boss_ataca == False and boss_anda == False and boss_sofre == False and boss_morre == False and boss_ataca_rapido == False:
                        boss_action[0] += 0.3
                        if boss_action[0] >= 3:
                            boss_action[0] = 0
                        if boss_direita == True:
                            boss_sprites[int(boss_action[0])] = p.transform.scale(boss_sprites[int(boss_action[0])], (multi_x*150,multi_y*150))
                            tela.blit(boss_sprites[int(boss_action[0])], (x_boss,y_boss))
                        if boss_direita == False:
                            boss_sprites[int(boss_action[0])] = p.transform.scale(boss_sprites[int(boss_action[0])], (multi_x*150,multi_y*150))
                            boss_sprites[int(boss_action[0])] = p.transform.flip(boss_sprites[int(boss_action[0])], True, False)
                            tela.blit(boss_sprites[int(boss_action[0])], (x_boss,y_boss))
                            boss_sprites[int(boss_action[0])] = p.transform.flip(boss_sprites[int(boss_action[0])], True, False)
                    # Ações com base em distância (perto)
                    if ande == False:
                        # Boss sofre dano
                        boss_anda = False
                        boss_ataca_rapido = False
                        if boss_sofre == True:
                            boss_action[6] += 0.3
                            if boss_action[6] >= 29:
                                # Seleciona qual ataque dá dano
                                if ataque1 == True:
                                    boss_vida -= dano1level
                                if ataque2 == True:
                                    boss_vida -= dano2level
                                if v_special == True:
                                    boss_vida -= atk_especial
                                boss_action[6] = 27
                                boss_sofre = False
                            if boss_direita == True:
                                boss_sprites[int(boss_action[6])] = p.transform.scale(boss_sprites[int(boss_action[6])], (multi_x*150,multi_y*150))
                                tela.blit(boss_sprites[int(boss_action[6])], (x_boss,y_boss))
                            if boss_direita == False:
                                boss_sprites[int(boss_action[6])] = p.transform.scale(boss_sprites[int(boss_action[6])], (multi_x*150,multi_y*150))
                                boss_sprites[int(boss_action[6])] = p.transform.flip(boss_sprites[int(boss_action[6])], True, False)
                                tela.blit(boss_sprites[int(boss_action[6])], (x_boss,y_boss))
                                boss_sprites[int(boss_action[6])] = p.transform.flip(boss_sprites[int(boss_action[6])], True, False)
                        # Ataques
                        if boss_sofre == False and boss_morre == False and anterior == 25:
                            boss_ataca = True
                        if boss_ataca == True:
                            if atk_chos == 5:
                                atk_chos = randint(1, 3)
                            # Atk 1
                            if atk_chos == 1:
                                boss_action[2] += 0.25
                                if boss_action[2] >= 15:
                                    boss_action[2] = 11
                                    atk_chos = 5
                                    boss_ataca = False
                                    dano_geral.append(danos_boss[0])
                                if boss_direita == True:
                                    boss_sprites[int(boss_action[2])] = p.transform.scale(boss_sprites[int(boss_action[2])], (multi_x*150,multi_y*150))
                                    tela.blit(boss_sprites[int(boss_action[2])], (x_boss,y_boss))
                                if boss_direita == False:
                                    boss_sprites[int(boss_action[2])] = p.transform.scale(boss_sprites[int(boss_action[2])], (multi_x*150,multi_y*150))
                                    boss_sprites[int(boss_action[2])] = p.transform.flip(boss_sprites[int(boss_action[2])], True, False)
                                    tela.blit(boss_sprites[int(boss_action[2])], (x_boss,y_boss))
                                    boss_sprites[int(boss_action[2])] = p.transform.flip(boss_sprites[int(boss_action[2])], True, False)
                            # Atk 2
                            if atk_chos == 2:
                                boss_action[3] += 0.25
                                if boss_action[3] >= 19:
                                    boss_action[3] = 16
                                    atk_chos = 5
                                    boss_ataca = False
                                    dano_geral.append(danos_boss[1])
                                if boss_direita == True:
                                    boss_sprites[int(boss_action[3])] = p.transform.scale(boss_sprites[int(boss_action[3])], (multi_x*150,multi_y*150))
                                    tela.blit(boss_sprites[int(boss_action[3])], (x_boss,y_boss))
                                if boss_direita == False:
                                    boss_sprites[int(boss_action[3])] = p.transform.scale(boss_sprites[int(boss_action[3])], (multi_x*150,multi_y*150))
                                    boss_sprites[int(boss_action[3])] = p.transform.flip(boss_sprites[int(boss_action[3])], True, False)
                                    tela.blit(boss_sprites[int(boss_action[3])], (x_boss,y_boss))
                                    boss_sprites[int(boss_action[3])] = p.transform.flip(boss_sprites[int(boss_action[3])], True, False)
                            # Atk 3
                            if atk_chos == 3:
                                boss_action[4] += 0.25
                                if boss_action[4] >= 24:
                                    boss_action[4] = 20
                                    atk_chos = 5
                                    boss_ataca = False
                                    dano_geral.append(danos_boss[2])
                                if boss_direita == True:
                                    boss_sprites[int(boss_action[4])] = p.transform.scale(boss_sprites[int(boss_action[4])], (multi_x*150,multi_y*150))
                                    tela.blit(boss_sprites[int(boss_action[4])], (x_boss,y_boss))
                                if boss_direita == False:
                                    boss_sprites[int(boss_action[4])] = p.transform.scale(boss_sprites[int(boss_action[4])], (multi_x*150,multi_y*150))
                                    boss_sprites[int(boss_action[4])] = p.transform.flip(boss_sprites[int(boss_action[4])], True, False)
                                    tela.blit(boss_sprites[int(boss_action[4])], (x_boss,y_boss))
                                    boss_sprites[int(boss_action[4])] = p.transform.flip(boss_sprites[int(boss_action[4])], True, False)
                if sair == True:
                    p.quit()
                    break
                # Morte
                if death_player == True:
                    break
                op_boss = size[0][0]/3.8*boss_vida/600
                op = size[0][0]/4*vida/hp_max
                if op < 0:
                    op = 0
                if op_boss < 0:
                    op_boss = 0
                gui_geral[0] = p.transform.scale(gui_geral[0], (size[0][0]/4, size[0][1]/6*0.8))
                gui_geral[1] = p.transform.scale(gui_geral[1], (op, size[0][1]/6*0.8))
                gui_geral[4] = p.transform.scale(gui_geral[4], (op_boss, size[0][1]/6*0.8))
                gui_geral[0] = p.transform.flip(gui_geral[0], True, False)
                gui_geral[4] = p.transform.flip(gui_geral[4], True, False)
                tela.blit(fonte.render("Rei Morto", True, (255,0,0)), (size[0][0]-300, 0))
                tela.blit(gui_geral[0], (size[0][0]-380, 10))
                tela.blit(gui_geral[4], (size[0][0]-op_boss-50, 10))
                gui_geral[4] = p.transform.flip(gui_geral[4], True, False)
                gui_geral[0] = p.transform.flip(gui_geral[0], True, False)
                # Barra de vida jogador
                tela.blit(gui_geral[0], (0, 0))
                tela.blit(gui_geral[1], (50,0))
                p.display.flip() # Atualiza a tela
            if sair==True:
                break
        if death_player == True:
            morto = death_screen()
            lista = ["1","50","30",f"{atk_especial}",f"{parte_chapter}",f"{cx}",f"{cy}"]
            if morto == False:
                break
    p.quit()
    # Padrão de lista: Capítulo, Max HP, HP atual, Dano especial, Arquivo mapa[], Coordenada x, Coordenada y
    return lista
def chapter2():
    return 3
def chapter3():
    return 4
def chapter4():
    return 5
def chapter5():
    return 0
def txt_control(nome):
    try: # Tenta acessar o arquivo.
        leitor = open(nome, "rt", encoding='utf-8')
    except: # Caso: arquivo inexistente, criar um.
        update = open(nome, "x", encoding='utf-8')
        update.close()
        leitor = open(nome, "rt", encoding="utf-8")
    finally: # Retorna uma lista com a situação do arquivo.
        return leitor
def capa():
    # Importações específicas
    import pygame as p
    from sys import exit
    # Declaração de variáveis 
    p.init()
    screen = p.display.set_mode((1000, 500)) # Cria tela
    p.display.set_caption("Capa(Cursed Kingdom)")
    tiktak = p.time.Clock() # Taxa de renderização da tela
    sprite_p = (320, 250)
    giro = 0
    x = 0
    ps = [(0, 0), (120, 0), (240, 0), (360, 0), (480, 0), (600, 0), (720, 0), (840, 0), (960, 0), (1080, 0)]
    rs = []
    font = p.font.SysFont("arial", 32, False, False) # Fonte do texto
    # Imagens do jogador e cenário
    cenario = [p.image.load("C:/Users/User/Documents/Cursed_Kingdom/Sprites jogo/Background/Cenário intro/11.png").convert_alpha(),
    p.image.load("C:/Users/User/Documents/Cursed_Kingdom/Sprites jogo/Background/Cenário intro/10.png").convert_alpha(),
    p.image.load("C:/Users/User/Documents/Cursed_Kingdom/Sprites jogo/Background/Cenário intro/09.png").convert_alpha(),
    p.image.load("C:/Users/User/Documents/Cursed_Kingdom/Sprites jogo/Background/Cenário intro/08.png").convert_alpha(),
    p.image.load("C:/Users/User/Documents/Cursed_Kingdom/Sprites jogo/Background/Cenário intro/07.png").convert_alpha(),
    p.image.load("C:/Users/User/Documents/Cursed_Kingdom/Sprites jogo/Background/Cenário intro/06.png").convert_alpha(),
    p.image.load("C:/Users/User/Documents/Cursed_Kingdom/Sprites jogo/Background/Cenário intro/05.png").convert_alpha(),
    p.image.load("C:/Users/User/Documents/Cursed_Kingdom/Sprites jogo/Background/Cenário intro/04.png").convert_alpha(),
    p.image.load("C:/Users/User/Documents/Cursed_Kingdom/Sprites jogo/Background/Cenário intro/03.png").convert_alpha(),
    p.image.load("C:/Users/User/Documents/Cursed_Kingdom/Sprites jogo/Background/Cenário intro/02.png").convert_alpha(),
    p.image.load("C:/Users/User/Documents/Cursed_Kingdom/Sprites jogo/Background/Cenário intro/01.png").convert_alpha(),
    p.image.load("C:/Users/User/Documents/Cursed_Kingdom/Sprites jogo/Background/Cenário intro/00.png").convert_alpha()]
    run = p.image.load("C:/Users/User/Documents/Cursed_Kingdom/Sprites jogo/Player/Player_run.png").convert_alpha()
    # Seleção das várias imagens
    for pos in range(len(ps)):
        st = run.subsurface(ps[pos], (120, 80))
        rs.append(st)
    # Loop para a tela
    while True:
        # Seletor de acontecimentos
        for event in p.event.get():
            if event.type == p.QUIT:
                p.quit()
                return True
                exit()
            if event.type == p.KEYDOWN:
                if event.key == p.K_SPACE:
                    # Parar a música (a fazer)
                    p.quit()
                    return True
                    exit()
        # Variáveis de controle de repetição
        giro += 1.5
        if giro >= 10:
            giro = 0
        x -= 30
        if x <= -1000:
            x = 0
        # Atualização da tela
        tiktak.tick(120)
        screen.fill((0, 0, 0))
        # Ciclo de cenário
        for sequence in range(0,11):
            cenario[sequence] = p.transform.scale(cenario[sequence], (1000, 600))
            screen.blit(cenario[sequence], (x, -120))
        for sequence in range(0,11):
            cenario[sequence] = p.transform.scale(cenario[sequence], (1000, 600))
            screen.blit(cenario[sequence], ((x+1000), -120)) 
        texto = "--Pressione ESPAÇO para começar--"
        write = font.render(texto, False, white)
        screen.blit(write, (270, 240))
        # Desenho do personagem
        rs[int(giro)] = p.transform.scale(rs[int(giro)], (120*2.5, 80*2.5))
        screen.blit(rs[int(giro)], sprite_p)
        p.display.flip()
