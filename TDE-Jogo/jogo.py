import pygame
import random

# Inicializando o Pygame
pygame.init()

# Definindo as dimensões da tela
screen_width = 500
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("TDE - Jogo")

# Definindo as cores
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Definindo a posição inicial do jogador
player_size = 50
player_pos = [screen_width // 2, screen_height // 2]

# Definindo a posição inicial dos alvos verdes e obstáculos vermelhos
target_size = 50
target_pos = [random.randint(0, screen_width - target_size), random.randint(0, screen_height - target_size)]
obstacle_pos = [random.randint(0, screen_width - target_size), random.randint(0, screen_height - target_size)]

# Definindo a velocidade do jogador
player_speed = 10

# Inicializando a pontuação e as condições de vitória/derrota
score = 0
win_score = 5
game_over = False

# Configurando a fonte para exibir a pontuação
font = pygame.font.Font(None, 28)

# Loop principal do jogo
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player_pos[0] -= player_speed
    if keys[pygame.K_RIGHT]:
        player_pos[0] += player_speed
    if keys[pygame.K_UP]:
        player_pos[1] -= player_speed
    if keys[pygame.K_DOWN]:
        player_pos[1] += player_speed

    # Garantindo que o jogador não saia da tela
    player_pos[0] = max(0, min(player_pos[0], screen_width - player_size))
    player_pos[1] = max(0, min(player_pos[1], screen_height - player_size))

    # Verificando se o jogador pegou o alvo verde
    if (player_pos[0] < target_pos[0] < player_pos[0] + player_size or player_pos[0] < target_pos[0] + target_size < player_pos[0] + player_size) and \
       (player_pos[1] < target_pos[1] < player_pos[1] + player_size or player_pos[1] < target_pos[1] + target_size < player_pos[1] + player_size):
        score += 1
        target_pos = [random.randint(0, screen_width - target_size), random.randint(0, screen_height - target_size)]
        obstacle_pos = [random.randint(0, screen_width - target_size), random.randint(0, screen_height - target_size)]

    # Verificando se o jogador tocou em um obstáculo vermelho
    if (player_pos[0] < obstacle_pos[0] < player_pos[0] + player_size or player_pos[0] < obstacle_pos[0] + target_size < player_pos[0] + player_size) and \
       (player_pos[1] < obstacle_pos[1] < player_pos[1] + player_size or player_pos[1] < obstacle_pos[1] + target_size < player_pos[1] + player_size):
        game_over = True

    # Preenchendo a tela com a cor preta
    screen.fill(BLACK)

    # Desenhando o jogador
    pygame.draw.rect(screen, BLUE, (player_pos[0], player_pos[1], player_size, player_size))

    # Desenhando o alvo verde
    pygame.draw.rect(screen, GREEN, (target_pos[0], target_pos[1], target_size, target_size))

    # Desenhando o obstáculo vermelho
    pygame.draw.rect(screen, RED, (obstacle_pos[0], obstacle_pos[1], target_size, target_size))

    # Exibindo a pontuação
    score_text = font.render(f"Pontuação: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    # Exibindo a condição de derrota
    if game_over:
        game_over_text = font.render("Você Perdeu!", True, WHITE)
        screen.blit(game_over_text, (screen_width // 2 - 60, screen_height // 2 - 20))
        pygame.display.flip()
        pygame.time.wait(2000)
        running = False

    # Verificando condição de vitória
    if score >= win_score:
        victory_text = font.render("Você Venceu!", True, WHITE)
        screen.blit(victory_text, (screen_width // 2 - 60, screen_height // 2 - 20))
        pygame.display.flip()
        pygame.time.wait(2000)
        running = False

    # Atualizando a tela
    pygame.display.flip()

    # Controlando a taxa de atualização
    pygame.time.Clock().tick(30)

# Encerrando o Pygame
pygame.quit()
