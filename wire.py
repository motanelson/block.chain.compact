
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import csv
import numpy as np
from tkinter import Tk, filedialog
import os
import time

def escolher_csv():
    root = Tk()
    root.withdraw()
    caminho = filedialog.askopenfilename(
        title="Selecionar ficheiro CSV",
        filetypes=[("Ficheiros CSV", "*.csv")]
    )
    root.destroy()
    return caminho

def ler_linhas_csv(caminho):
    linhas = []
    with open(caminho, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) < 6:
                continue
            try:
                p1 = list(map(float, row[0:3]))
                p2 = list(map(float, row[3:6]))
                linhas.append((p1, p2))
            except ValueError:
                continue
    return linhas

def desenhar_linhas(linhas):
    glColor3f(0, 0, 0)  # linhas pretas
    glBegin(GL_LINES)
    for p1, p2 in linhas:
        glVertex3fv(p1)
        glVertex3fv(p2)
    glEnd()

def main():
    caminho = escolher_csv()
    if not caminho or not os.path.exists(caminho):
        print("Ficheiro não encontrado.")
        return

    linhas = ler_linhas_csv(caminho)
    if not linhas:
        print("Nenhuma linha válida encontrada no ficheiro.")
        return

    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.display.set_caption("Visualizador 3D - Linhas do CSV")

    # Fundo amarelo
    glClearColor(1.0, 1.0, 0.0, 1.0)
    glEnable(GL_DEPTH_TEST)

    gluPerspective(45, (display[0] / display[1]), 0.1, 1000.0)
    glTranslatef(-10, -10, -50)

    angulo = 0
    tempo_ultima_rotacao = time.time()

    clock = pygame.time.Clock()
    running = True
    while running:
        clock.tick(60)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        for evento in pygame.event.get():
            if evento.type == QUIT:
                running = False

        # Rotação automática a cada 1.5 segundos
        tempo_atual = time.time()
        if tempo_atual - tempo_ultima_rotacao > 0.1:
            angulo += 1
            tempo_ultima_rotacao = tempo_atual

        glPushMatrix()
        glRotatef(angulo % 360, 0, 1, 0)  # rotaciona em torno de Y
        desenhar_linhas(linhas)
        glPopMatrix()

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
