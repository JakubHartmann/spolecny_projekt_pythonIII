import pygame

pygame.init()


class Postavicka:
    def __init__(self):
        self.x = 450
        self.y = 600
        self.rect = pygame.rect.Rect(self.x, self.y, 50, 50)
        self.image = None


    def ukaz(self):
        pass

    def pohyb(self, smer):
        pass

class Lod:
    def __init__(self):
        self.x = 50
        self.y = 70
        self.rect = pygame.rect.Rect(self.x, self.y, 50, 50)
        self.pocitadlo_pohyb = 0
        self.pocitadlo_pusteni_jidla = 0
        self.smer = 1 
        self.image = pygame.image.load("ovoce.png")# change afterwards

    def ukaz(self):
        okno.blit(self.image, self.rect)# delete 

    def pohyb(self):
        
        self.pocitadlo_pohyb += 1
        
        if self.x >= 770:
         self.smer = -1
        elif self.x <= 70:
            self.smer = 1


        if self.pocitadlo_pohyb == 10:
            if self.smer == 1:
                self.x += 50
            elif self.smer == -1:
                self.x -= 50
            self.pocitadlo_pohyb = 0
        
        self.rect = pygame.rect.Rect(self.x, self.y, 50, 50) 

    def pusteni_jidla(self):
        pass


class Jidlo:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rect = pygame.rect.Rect(self.x, self.y, 50, 50)
        self.pocitadlo = 0
        self.image = None

    def ukaz(self):
        pass

    def pohyb(self):
        pass

    def kolize_s_postavickou(self):
        pass



skore = 0
seznam_jidel = []
postavicka = Postavicka()
lod= Lod()

okno = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    zmacknuti = pygame.key.get_pressed()

    okno.fill("Black")
    postavicka.ukaz()
    lod.ukaz()
    lod.pusteni_jidla()
    lod.pohyb()
    for jidlo in seznam_jidel:
        jidlo.ukaz()
        jidlo.pohyb()
        jidlo.kolize_s_postavickou()


    clock.tick(60)
    pygame.display.update()


# vytvoreni textury a zobrazeni pro 3 tridy
# udelani pohybu postavicky
# udelani pohybu lode
# udelani pohybu jidla
# vypisovani skore
# vyreseni kolize jidla a postavicky
# pusteni jidla



    