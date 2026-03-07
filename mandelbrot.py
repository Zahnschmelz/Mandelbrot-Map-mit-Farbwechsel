import pygame
import sys
import math

# Initialisierung von Pygame
pygame.init()

# Bildschirmgröße und -einstellungen
WIDTH, HEIGHT = 768, 512
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mandelbrot Map mit Farbwechsel")

# Farbenpalette (dynamisch)
def get_color(iterations):
    # Einfache dynamische Farbpalette
    return (iterations % 256, iterations % 192, iterations % 256)

# Mandelbrot-Berechnung
def mandelbrot(c, max_iter):
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z*z + c
        n += 1
    return n

# Hauptloop
def main():
    clock = pygame.time.Clock()
    running = True
    max_iter = 25 #256
    zoom = 0.5
    offset_x, offset_y = -0.5, 0.0
    iteration_count = 1

    # RGB Startbereich

    r = 0
    g = 127
    b = 64

    #check RGB
    checkr = False
    checkg = False
    checkb = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Farbwechsel (außerhalb der Menge)
        iteration_count += 1

        # Farbwechsel (in der Menge)
        if r < 255 and checkr == False:
            r = r + 3
        elif r >= 255:
            checkr = True
        if checkr == True:
            r = r - 2
        if r <= 0:
            checkr = False

        if g < 255 and checkg == False:
            g = g + 2
        elif g >= 255:
            checkg = True
        if checkg == True:
            g = g - 4
        if g <= 0:
            checkg = False

        if b < 255 and checkb == False:
            b = b + 8
        elif b >= 255:
            checkb = True
        if checkb == True:
            b = b - 1
        if b <= 0:
            checkb = False

        # Überlauf
        if r > 255:
            r = 255
        if r < 0:
            r = 0
        if g > 255:
            g = 255
        if g < 0:
            g = 0
        if b > 255:
            b = 255
        if b < 0:
            b = 0

        print(checkr)
        print(checkg)
        print(checkb)


        screen.fill((r, g, b)) # Schwarz für Punkte außerhalb der Menge

        # Zeichnen der Mandelbrot-Menge
        for x in range(WIDTH):
            for y in range(HEIGHT):
                # Koordinatenberechnung
                zx = (x - WIDTH / 2) / (WIDTH / 4) * zoom + offset_x
                zy = (y - HEIGHT / 2) / (HEIGHT / 4) * zoom + offset_y

                c = complex(zx, zy)
                m = mandelbrot(c, max_iter)

                # Farbe basierend auf Iterationen
                if m == max_iter:
                    color = (r, g, b)  # Bunt für Punkte in der Menge
                else:
                    color = get_color(iteration_count + m)

                screen.set_at((x, y), color)

        pygame.display.flip()
        print("ticktack")
        clock.tick(60)  # 60 FPS
        print(color)
        print(r,g,b)
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()

if __name__ == "__main__":
    main()
