import pygame
import random
pygame.init()

# DEFINIR DIMENSOES DA TELA 
larguraTela = 500
alturaTela = 400
tela = pygame.display.set_mode((larguraTela, alturaTela)) #CRIA A JANELA 
pygame.display.set_caption("TDE - Jogo") #TITULO NA JANELA 


# DEFININDO AS CORES EM VARIAVEIS (RGB)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


# POSICAO INICIAL
tamanhoJogador = 50 #tamanho quadrado jogador
posicaoJogador = [larguraTela // 2, alturaTela // 2] #centraliza na tela, duas barras para sempre arredondar o valor


# POSICAO INICIAL ALVOS
tamanhoAlvo  = 50 #tamanho alvos
posicaoAlvo = [random.randint(0, larguraTela  - tamanhoAlvo), random.randint(0, alturaTela  - tamanhoAlvo)]
tamanhoObs = 70
posicaoObstaculo  = [random.randint(0, larguraTela  - tamanhoObs), random.randint(0, alturaTela  - tamanhoObs)]
#define a posição dos alvos em algum lugar aleatório da tela.


# velocidade 10px por movimento
velocidadeJogador = 11

#PONTUACOES
pontuacao  = 0
pontuacaoVitoria  = 5
fimDeJogo  = False #indica que o jogo terminou
fonte = pygame.font.Font(None, 28) #tamanho da fonte



rodando  = True 
while rodando :
    for event in pygame.event.get(): #verifica clique do mouse ou teclas
        if event.type == pygame.QUIT: #encerra o jogo se o evento for fechamento de tela 
            rodando = False

    teclas = pygame.key.get_pressed() #verifica as teclas que estao sendo pressionadas

    if teclas[pygame.K_LEFT]:
        posicaoJogador[0] -= velocidadeJogador   #esquerda
    if teclas[pygame.K_RIGHT]:
        posicaoJogador[0] += velocidadeJogador   #direita
    if teclas[pygame.K_UP]:
        posicaoJogador[1] -= velocidadeJogador   #cima
    if teclas[pygame.K_DOWN]:
        posicaoJogador[1] += velocidadeJogador   #baixo


    #mantem o player dentro da tela 
    posicaoJogador[0] = max(0, min(posicaoJogador[0], larguraTela  - tamanhoJogador))
    posicaoJogador[1] = max(0, min(posicaoJogador[1], alturaTela  - tamanhoJogador))

    #verificação de colisão com alvo verde
    if (posicaoJogador[0] < posicaoAlvo[0] < posicaoJogador[0] + tamanhoJogador or
        posicaoJogador[0] < posicaoAlvo[0] + tamanhoAlvo < posicaoJogador[0] + tamanhoJogador) and \
       (posicaoJogador[1] < posicaoAlvo[1] < posicaoJogador[1] + tamanhoJogador or
        posicaoJogador[1] < posicaoAlvo[1] + tamanhoAlvo < posicaoJogador[1] + tamanhoJogador):
        pontuacao += 1 #adiciona +1 para a pontuação

        #define novas posições
        posicaoAlvo = [random.randint(0, larguraTela - tamanhoAlvo), random.randint(0, alturaTela - tamanhoAlvo)]
        posicaoObstaculo = [random.randint(0, larguraTela - tamanhoObs), random.randint(0, alturaTela - tamanhoObs)]

    #colisão com alvo vermelho
    if (posicaoJogador[0] < posicaoObstaculo[0] < posicaoJogador[0] + tamanhoJogador or
        posicaoJogador[0] < posicaoObstaculo[0] + tamanhoObs < posicaoJogador[0] + tamanhoJogador) and \
       (posicaoJogador[1] < posicaoObstaculo[1] < posicaoJogador[1] + tamanhoJogador or
        posicaoJogador[1] < posicaoObstaculo[1] + tamanhoObs < posicaoJogador[1] + tamanhoJogador):
        fimDeJogo = True

    # fundo de tela
    tela.fill(BLACK)

    # jogador
    pygame.draw.rect(tela, BLUE, (posicaoJogador[0], posicaoJogador[1], tamanhoJogador, tamanhoJogador))

    # alvo verde
    pygame.draw.rect(tela, GREEN, (posicaoAlvo[0], posicaoAlvo[1], tamanhoAlvo, tamanhoAlvo))


    # alvo vermelho
    pygame.draw.rect(tela, RED, (posicaoObstaculo[0], posicaoObstaculo[1], tamanhoObs, tamanhoObs))

    # pontuação
    textoPontuacao = fonte.render(f"Pontuação: {pontuacao}", True, WHITE)
    tela.blit(textoPontuacao, (10, 10))

    #derrota
    if fimDeJogo:
        textoFimDeJogo = fonte.render("Você Perdeu!", True, WHITE)
        tela.blit(textoFimDeJogo, (larguraTela // 2 - 60, alturaTela // 2 - 20))
        pygame.display.flip()
        pygame.time.wait(2000)
        rodando = False
    #se o game over for TRUE, encerrao jogo após 2 seg e exibe VOCE PERDEU na tela 

    #vitória
    if pontuacao >= pontuacaoVitoria:
        textoVitoria = fonte.render("Você Venceu!", True, WHITE)
        tela.blit(textoVitoria, (larguraTela // 2 - 60, alturaTela // 2 - 20))
        pygame.display.flip()
        pygame.time.wait(2000)
        rodando = False
        # se a pontuação atingir 5 exibe VOCE VENCEU e encerra o jogo apos 2 seg

    #atualiza a tela 
    pygame.display.flip()

    pygame.time.Clock().tick(60) #60fps

pygame.quit()
