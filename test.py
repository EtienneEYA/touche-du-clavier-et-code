import pygame
from pygame.locals import *

pygame.init()

# Définition des dimensions de la fenêtre
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 400

# Création de la fenêtre graphique
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Affichage des codes et touches clavier")

# Définition de la police d'écriture
font = pygame.font.Font(None, 36)

# Liste pour stocker les codes et les touches
key_list = []

# Variables pour la gestion du défilement
scroll_position = 0
scroll_speed = 40  # Vitesse de défilement en pixels par pression de touche

# Boucle principale de l'application
running = True
while running:
    # Gestion des événements
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        elif event.type == KEYDOWN:
            # Récupération du code et de la touche pressée
            key_code = event.key
            key_name = pygame.key.name(key_code)

            # Ajout du code et de la touche à la liste
            key_list.append(f"Code: {key_code}   Touche: {key_name}")

            # Limitation de la liste à 10 éléments pour éviter un affichage trop long
            if len(key_list) > 10:
                key_list.pop(0)

            # Mise à jour de la position de défilement pour afficher la dernière ligne ajoutée
            scroll_position = max(0, len(key_list) * 40 - WINDOW_HEIGHT)

        elif event.type == KEYUP:
            if event.key == K_UP:
                # Défilement vers le haut lors de la relâche de la touche flèche haut
                scroll_position -= scroll_speed
            elif event.key == K_DOWN:
                # Défilement vers le bas lors de la relâche de la touche flèche bas
                scroll_position += scroll_speed

    # Effacement de la fenêtre
    window.fill((200, 200, 200))

    # Création d'une surface plus grande que la fenêtre visible
    surface = pygame.Surface((WINDOW_WIDTH, len(key_list) * 40))
    surface.fill((200, 200, 200))

    # Affichage des codes et des touches sur la surface
    y = 0
    for key_text in key_list:
        text_surface = font.render(key_text, True, (5, 5, 5))
        surface.blit(text_surface, (10, y))
        y += 40

    # Affichage de la portion de la surface correspondant à la fenêtre visible
    window.blit(surface, (0, -scroll_position))

    # Rafraîchissement de la fenêtre
    pygame.display.flip()

pygame.quit()