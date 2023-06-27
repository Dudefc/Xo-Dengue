import pygame
import random
import os

# Inicialização do Pygame
pygame.init()

# Definição das constantes do jogo
LARGURA_TELA = 1280
ALTURA_TELA = 720
TAMANHO_JOGADOR = 100
TAMANHO_MOSQUITO = 150
TAMANHO_FOCUS = 120
MAX_VIDAS = 1
TEMPO_JOGO = 30  # em segundos

# Definição das cores utilizadas no jogo
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)

# Definição da fonte utilizada para exibir o tempo e a pontuação
FONTE = pygame.font.SysFont('Arial', 30)

# Criação da janela do jogo
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption('Xô Dengue')

# Carregamento das imagens
diretorio_imagens = 'focus'  # Diretório que contém as imagens dos objetos de foco
imagens_focus = []  # Lista para armazenar as imagens dos objetos de foco
for nome_arquivo in os.listdir(diretorio_imagens):
    if nome_arquivo.endswith('.png'):
        caminho_imagem = os.path.join(diretorio_imagens, nome_arquivo)
        imagem = pygame.image.load(caminho_imagem).convert_alpha()
        imagens_focus.append(imagem)

# Redimensionamento das imagens
jogador_imagem = pygame.image.load('imagem/jogador.png').convert_alpha()
jogador_imagem = pygame.transform.scale(jogador_imagem, (TAMANHO_JOGADOR, TAMANHO_JOGADOR))
mosquito_imagem = pygame.image.load('imagem/mosquito.png').convert_alpha()
mosquito_imagem = pygame.transform.scale(mosquito_imagem, (TAMANHO_MOSQUITO, TAMANHO_MOSQUITO))

# Redimensionamento das imagens de foco
imagens_focus_redimensionadas = []
for imagem_focus in imagens_focus:
    imagem_focus_redimensionada = pygame.transform.scale(imagem_focus, (TAMANHO_FOCUS, TAMANHO_FOCUS))
    imagens_focus_redimensionadas.append(imagem_focus_redimensionada)


# Criação do jogador e do mosquito
jogador_x = LARGURA_TELA // 2
jogador_y = ALTURA_TELA - TAMANHO_JOGADOR
mosquito_x = random.randint(0, LARGURA_TELA - TAMANHO_MOSQUITO)
mosquito_y = random.randint(0, ALTURA_TELA - TAMANHO_MOSQUITO)

# Criação dos objetos de foco da dengue
lista_focus = []
for i in range(1):
    focus_x = random.randint(0, LARGURA_TELA - TAMANHO_FOCUS)
    focus_y = random.randint(0, ALTURA_TELA - TAMANHO_FOCUS)
    imagem_focus = random.choice(imagens_focus)  # Seleciona uma imagem aleatória da lista
    lista_focus.append((focus_x, focus_y, imagem_focus))

# Inicialização das variáveis do jogo
pontuacao = 0
vidas = MAX_VIDAS
tempo_jogo = TEMPO_JOGO * 1000  # em milissegundos
tempo_inicial = pygame.time.get_ticks()

# Classe para criar um botão
class Botao:
    def __init__(self, x, y, largura, altura, texto, cor):
        self.retangulo = pygame.Rect(x, y, largura, altura)
        self.texto = texto
        self.cor = cor

    def desenhar(self, tela):
        pygame.draw.rect(tela, self.cor, self.retangulo)
        fonte = pygame.font.SysFont('Arial', 24)
        texto = fonte.render(self.texto, True, PRETO)
        texto_retangulo = texto.get_rect(center=self.retangulo.center)
        tela.blit(texto, texto_retangulo)

    def foi_clicado(self, posicao):
        return self.retangulo.collidepoint(posicao)

# Criação do botão de reiniciar
botao_reiniciar = Botao(LARGURA_TELA // 2 - 75, ALTURA_TELA // 2 + 30, 150, 50, 'Reiniciar', VERDE)

# Criação do botão de iniciar
botao_iniciar = Botao(LARGURA_TELA // 2 - 75, ALTURA_TELA // 2 + 50, 150, 50, 'Iniciar', VERDE)

# Criação do botão dos programadores
botao_creditos = Botao(LARGURA_TELA // 2 - 75, ALTURA_TELA // 2 + 150, 150, 50, 'Créditos', VERDE)


# Loop da tela inicial
tela_inicial = True
exibir_creditos = False

while tela_inicial:
    # Verificação dos eventos da tela inicial
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            tela_inicial = False
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            posicao_mouse = pygame.mouse.get_pos()
            if botao_iniciar.foi_clicado(posicao_mouse):
                tela_inicial = False
            elif botao_creditos.foi_clicado(posicao_mouse):
                exibir_creditos = True

    # Desenho da tela inicial
    tela.fill(BRANCO)
    texto_titulo = FONTE.render('Xô Dengue', True, PRETO)
    tela.blit(texto_titulo, (LARGURA_TELA // 2 - texto_titulo.get_width() // 2, ALTURA_TELA // 2 - 100))
    texto_instrucoes = FONTE.render('Instruções: Use as setas para mover o jogador.', True, PRETO)
    tela.blit(texto_instrucoes, (LARGURA_TELA // 2 - texto_instrucoes.get_width() // 2, ALTURA_TELA // 2 - 50))
    botao_iniciar.desenhar(tela)
    botao_creditos.desenhar(tela)
    pygame.display.flip()

    while exibir_creditos:
        tela.fill(BRANCO)
        texto_creditos = FONTE.render('Programadores:', True, PRETO)
        tela.blit(texto_creditos, (LARGURA_TELA // 2 - texto_creditos.get_width() // 2, ALTURA_TELA // 2 - 300))
        texto_nomes = FONTE.render('Isla de Oliveira', True, PRETO)
        tela.blit(texto_nomes, (LARGURA_TELA // 2 - texto_nomes.get_width() // 2, ALTURA_TELA // 2 - 150))
        texto_nomes = FONTE.render('Rodrigo de Azevedo', True, PRETO)
        tela.blit(texto_nomes, (LARGURA_TELA // 2 - texto_nomes.get_width() // 2, ALTURA_TELA // 2 - 100))
        texto_nomes = FONTE.render('Rodrigo Feliz', True, PRETO)
        tela.blit(texto_nomes, (LARGURA_TELA // 2 - texto_nomes.get_width() // 2, ALTURA_TELA // 2 - 50))
        
        
        texto_voltar = FONTE.render('Clique para voltar ao menu principal', True, PRETO)
        tela.blit(texto_voltar, (LARGURA_TELA // 2 - texto_voltar.get_width() // 2, ALTURA_TELA // 2 + 80))
        pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                tela_inicial = False
                exibir_creditos = False
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                posicao_mouse = pygame.mouse.get_pos()
                exibir_creditos = False

# Loop da tela inicial
jogando = True
fim_jogo = False

while jogando:
    # Verificação dos eventos do jogo
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jogando = False

    # Atualização da posição do jogador com base nas teclas pressionadas
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT] and jogador_x > 0:
        jogador_x -= 0.5
    if teclas[pygame.K_RIGHT] and jogador_x < LARGURA_TELA - TAMANHO_JOGADOR:
        jogador_x += 0.5
    if teclas[pygame.K_UP] and jogador_y > 0:
        jogador_y -= 0.5
    if teclas[pygame.K_DOWN] and jogador_y < ALTURA_TELA - TAMANHO_JOGADOR:
        jogador_y += 0.5

    # Atualização da posição do mosquito de forma aleatória
    mosquito_x += random.randint(-5, 5)
    mosquito_y += random.randint(-5, 5)
    if mosquito_x < 0:
        mosquito_x = 0
    elif mosquito_x > LARGURA_TELA - TAMANHO_MOSQUITO:
        mosquito_x = LARGURA_TELA - TAMANHO_MOSQUITO
    if mosquito_y < 0:
        mosquito_y = 0
    elif mosquito_y > ALTURA_TELA - TAMANHO_MOSQUITO:
        mosquito_y = ALTURA_TELA - TAMANHO_MOSQUITO

    # Desenho dos objetos na tela
    tela.fill(BRANCO)
    tela.blit(jogador_imagem, (jogador_x, jogador_y))
    tela.blit(mosquito_imagem, (mosquito_x, mosquito_y))
    for focus in lista_focus:
        focus_x, focus_y, imagem_focus = focus
        tela.blit(imagem_focus, (focus_x, focus_y))

    # Verificação da colisão do jogador com o mosquito ou com um objeto de foco da dengue
    jogador_retangulo = pygame.Rect(jogador_x, jogador_y, TAMANHO_JOGADOR, TAMANHO_JOGADOR)
    mosquito_retangulo = pygame.Rect(mosquito_x, mosquito_y, TAMANHO_MOSQUITO, TAMANHO_MOSQUITO)
    for focus in lista_focus:
        focus_x, focus_y, _ = focus
        focus_retangulo = pygame.Rect(focus_x, focus_y, TAMANHO_FOCUS, TAMANHO_FOCUS)
        if jogador_retangulo.colliderect(mosquito_retangulo):
            vidas -= 1
            mosquito_x = random.randint(0, LARGURA_TELA - TAMANHO_MOSQUITO)
            mosquito_y = random.randint(0, ALTURA_TELA - TAMANHO_MOSQUITO)
            # Piscar a tela em vermelho
            for _ in range(4):
                tela.fill(VERMELHO)
                pygame.display.flip()
                pygame.time.wait(80)
                tela.fill(BRANCO)
                pygame.display.flip()
                pygame.time.wait(80)
        elif jogador_retangulo.colliderect(focus_retangulo):
            pontuacao += 1
            lista_focus.remove(focus)
            focus_x = random.randint(0, LARGURA_TELA - TAMANHO_FOCUS)
            focus_y = random.randint(0, ALTURA_TELA - TAMANHO_FOCUS)
            imagem_focus = random.choice(imagens_focus)
            lista_focus.append((focus_x, focus_y, imagem_focus))

   # Exibição da pontuação e do tempo na tela
    texto_pontuacao = FONTE.render(f'Pontuação: {pontuacao}', True, PRETO)
    tela.blit(texto_pontuacao, (10, 10))
    texto_vidas = FONTE.render(f'Vidas: {vidas}', True, PRETO)
    tela.blit(texto_vidas, (1180, 10))
    tempo_atual = pygame.time.get_ticks()
    tempo_restante = max(0, (tempo_jogo - (tempo_atual - tempo_inicial)) // 1000)
    texto_tempo = FONTE.render(f'Tempo Restante: {tempo_restante}', True, PRETO)
    tela.blit(texto_tempo, (LARGURA_TELA - texto_tempo.get_width() - 480, 10))

    # Verificação do fim do jogo
    if tempo_restante == 0 or vidas == 0:
        fim_jogo = True

    # Atualização da tela
    pygame.display.flip()

    # Verificação dos eventos de fim de jogo
    # Verificação do fim do jogo
    
    if tempo_restante == 0 or vidas == 0:
        fim_jogo = True


    # Verificação dos eventos de fim de jogo
    while fim_jogo:
        tela.fill(BRANCO)
        texto_fim_jogo = FONTE.render('Fim de jogo!', True, VERMELHO)
        tela.blit(texto_fim_jogo, (LARGURA_TELA // 2 - texto_fim_jogo.get_width() // 2, ALTURA_TELA // 2 - 50))
        texto_pontuacao_final = FONTE.render(f'Pontuação final: {pontuacao}', True, PRETO)
        tela.blit(texto_pontuacao_final, (LARGURA_TELA // 2 - texto_pontuacao_final.get_width() // 2, ALTURA_TELA // 2))
        botao_reiniciar.desenhar(tela)
        pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                jogando = False
                fim_jogo = False
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                posicao_mouse = pygame.mouse.get_pos()
                if botao_reiniciar.foi_clicado(posicao_mouse):
                    # Reiniciar o jogo
                    jogador_x = LARGURA_TELA // 2
                    jogador_y = ALTURA_TELA - TAMANHO_JOGADOR
                    mosquito_x = random.randint(0, LARGURA_TELA - TAMANHO_MOSQUITO)
                    mosquito_y = random.randint(0, ALTURA_TELA - TAMANHO_MOSQUITO)
                    lista_focus = []
                    for i in range(1):
                        focus_x = random.randint(0, LARGURA_TELA - TAMANHO_FOCUS)
                        focus_y = random.randint(0, ALTURA_TELA - TAMANHO_FOCUS)
                        imagem_focus = random.choice(imagens_focus)
                        lista_focus.append((focus_x, focus_y, imagem_focus))
                    pontuacao = 0
                    vidas = MAX_VIDAS
                    tempo_inicial = pygame.time.get_ticks()
                    fim_jogo = False    
                    
pygame.quit()