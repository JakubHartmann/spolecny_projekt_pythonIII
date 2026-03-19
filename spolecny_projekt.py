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

    def pohyb(self):
        zmacknuti = pygame.key.get_pressed()

        if zmacknuti[pygame.K_a]:
            self.x -= 10
        if zmacknuti[pygame.K_d]:
            self.x += 10

        self.rect =  pygame.rect.Rect(self.x, self.y, 50, 50)

class Lod:
    def __init__(self):
        self.x = 450
        self.y = 100
        self.rect = pygame.rect.Rect(self.x, self.y, 50, 50)
        self.pocitadlo_pohyb = 0
        self.pocitadlo_pusteni_jidla = 0
        self.image = None

    def ukaz(self):
        pass

    def pohyb(self):
        pass

    def pusteni_jidla(self):
        pass


class Jidlo:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rect = pygame.rect.Rect(self.x, self.y, 50, 50)
        self.pocitadlo = 0
        self.image = None

    def ukaz():
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

    okno.fill("Black")
    postavicka.ukaz()
    postavicka.pohyb()
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

# adam : pusteni jidla
# lukas : pohyb lode
# david : textura postavicky
# vojta : zbutek lode
# sebastian : zbytek jidla



    