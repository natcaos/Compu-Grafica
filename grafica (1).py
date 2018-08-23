import pygame
Ancho=640
Alto=480
VERDE=[0,255,0]
BLANCO=[255,255,255]

if __name__== '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([Ancho,Alto])
    pygame.draw.line(pantalla,VERDE,[100,100],[200,200])
    pygame.display.flip()
    pygame.draw.polygon(pantalla,[0,0,255], [[100, 100], [0, 200], [200, 200]], 5)
    pygame.dispay.flip()
    fin=False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
                if event.type == pygame.KEYDOWN:
                    print 'tecla pulsada'
