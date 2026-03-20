import pygame

pygame.init()

# VELIKOST_LODE = 50



class Postavicka:
    def __init__(self):
        self.x = 450
        self.y = 600
        self.image = pygame.image.load("vojak.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

    def ukaz(self):
        okno.blit(self.image, self.rect)

    def pohyb(self):
        zmacknuti = pygame.key.get_pressed()
        self.dx = 0
        self.speed = 4
        if zmacknuti[pygame.K_d]:
            self.dx = 1
        if zmacknuti[pygame.K_a]:
            self.dx = -1
        self.x += self.dx * self.speed
        self.rect.topleft = (self.x, self.y)

class Lod:
    def __init__(self):
        self.x = 50
        self.y = 70
        self.rect = pygame.rect.Rect(self.x, self.y, 50, 50)
        self.pocitadlo_pohyb = 0
        self.pocitadlo_pusteni_jidla = 0
        self.smer = 1 
        self.image = pygame.image.load("obrazek.gif")
        self.scaled_image = pygame.transform.scale(self.image, (50, 50))

    def ukaz(self):
        okno.blit(self.scaled_image, (self.x, self.y))

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
        self.pocitadlo_pusteni_jidla += 1
        if self.pocitadlo_pusteni_jidla == 60:
            seznam_jidel.append(Jidlo(self.x,self.y))
            self.pocitadlo_pusteni_jidla = 0

class Score:
    def __init__(self):
        self.score = 0
    def vypis(self):
        text = font.render("score: " + str(self.score), True, (255, 255, 255))
        okno.blit(text, (20, 20))


class Jidlo:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rect = pygame.rect.Rect(self.x, self.y, 50, 50)
        self.pocitadlo = 0
        self.image = pygame.image.load("cervenyhrac.png")
        self.image = pygame.transform.scale(self.image,(50,50))

    def ukaz(self):
        okno.blit(self.image,self.rect)

    def pohyb(self):
        self.pocitadlo += 1
        if self.pocitadlo == 10:
            self.y += 10
            self.pocitadlo = 0
            self.rect = pygame.rect.Rect(self.x, self.y, 50, 50)

    def kolize_s_postavickou(self):
        global skore
        if self.rect.colliderect(postavicka.rect):
            score.score += 1
            seznam_jidel.remove(self)



seznam_jidel = []
postavicka = Postavicka()
lod= Lod()
score = Score()


okno = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
running = True

# pro vykresleni score
font = pygame.font.Font(None, 48)

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
    score.vypis()
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



    