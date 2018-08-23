import pygame
Ancho=400
Alto=400
VERDE=[0,255,0]
BLANCO=[255,255,255]
NEGRO=[0,0,0]

def triangulo(p,pos,pos1,pos2):
    pygame.draw.polygon(p, VERDE, [pos, pos1, pos2], 2)

def plano(p):
    pygame.draw.line(p, VERDE, [200, 0], [200,400])
    pygame.draw.line(p, VERDE, [0, 200], [400,200])
if __name__== '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([Ancho,Alto])
    pos=[100,100]
    pos1=[0,200]
    pos2=[200,200]
    var_x=0
    reloj = pygame.time.Clock()
    fin=False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    var_y=2
                if event.key == pygame.K_DOWN:
                    var_y=-2
                if event.key == pygame.K_LEFT:
                    var_x=-2
                if event.key == pygame.K_RIGHT:
                    var_x=2
                if event.key == pygame.K_a:
                    var_x=0

        pos[0]+=var_x
        pos1[0]+=var_x
        pos2[0]+=var_x
        pantalla.fill(NEGRO)
        plano(pantalla)
        triangulo(pantalla, pos, pos1, pos2)
        pygame.display.flip()
        reloj.tick(60)
