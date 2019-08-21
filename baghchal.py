import pygame
from playsound import playsound
import random
from numpy import empty
import os
import numpy

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0, 20)
RED = (251, 9, 43)
WHITE = [255, 255, 255]

pygame.init()
size = [1350, 800]
bg = pygame.image.load("board final.png")
gameDisplay = pygame.display.set_mode(size)
screen = pygame.Surface(gameDisplay.get_size())
pygame.display.set_caption("BAGHACHAAL")
gameDisplay.fill(WHITE)
rule = pygame.image.load("mainpage.png")
# -------------------------------------------------------------------------------------------------
pw_tig1 = pygame.sprite.Sprite()
pw_tig1.image = pygame.image.load("tiger fin.png")
pw_tig1.rect = pw_tig1.image.get_rect()

pw_tig2 = pygame.sprite.Sprite()
pw_tig2.image = pygame.image.load("tiger fin.png")
pw_tig2.rect = pw_tig2.image.get_rect()

pw_tig3 = pygame.sprite.Sprite()
pw_tig3.image = pygame.image.load("tiger fin.png")
pw_tig3.rect = pw_tig3.image.get_rect()


pw_got1 = pygame.sprite.Sprite()
pw_got1.image = pygame.image.load("goat final.png")
pw_got1.rect = pw_got1.image.get_rect()

pw_got2 = pygame.sprite.Sprite()
pw_got2.image = pygame.image.load("goat final.png")
pw_got2.rect = pw_got2.image.get_rect()

pw_got3 = pygame.sprite.Sprite()
pw_got3.image = pygame.image.load("goat final.png")
pw_got3.rect = pw_got3.image.get_rect()

pw_got4 = pygame.sprite.Sprite()
pw_got4.image = pygame.image.load("goat final.png")
pw_got4.rect = pw_got4.image.get_rect()

pw_got5 = pygame.sprite.Sprite()
pw_got5.image = pygame.image.load("goat final.png")
pw_got5.rect = pw_got5.image.get_rect()

pw_got6 = pygame.sprite.Sprite()
pw_got6.image = pygame.image.load("goat final.png")
pw_got6.rect = pw_got6.image.get_rect()

pw_got7 = pygame.sprite.Sprite()
pw_got7.image = pygame.image.load("goat final.png")
pw_got7.rect = pw_got7.image.get_rect()

pw_got8 = pygame.sprite.Sprite()
pw_got8.image = pygame.image.load("goat final.png")
pw_got8.rect = pw_got8.image.get_rect()

pw_got9 = pygame.sprite.Sprite()
pw_got9.image = pygame.image.load("goat final.png")
pw_got9.rect = pw_got9.image.get_rect()

pw_got10 = pygame.sprite.Sprite()
pw_got10.image = pygame.image.load("goat final.png")
pw_got10.rect = pw_got10.image.get_rect()

pw_got11 = pygame.sprite.Sprite()
pw_got11.image = pygame.image.load("goat final.png")
pw_got11.rect = pw_got11.image.get_rect()

pw_got12 = pygame.sprite.Sprite()
pw_got12.image = pygame.image.load("goat final.png")
pw_got12.rect = pw_got12.image.get_rect()

pw_got13 = pygame.sprite.Sprite()
pw_got13.image = pygame.image.load("goat final.png")
pw_got13.rect = pw_got13.image.get_rect()

pw_got14 = pygame.sprite.Sprite()
pw_got14.image = pygame.image.load("goat final.png")
pw_got14.rect = pw_got14.image.get_rect()

pw_got15 = pygame.sprite.Sprite()
pw_got15.image = pygame.image.load("goat final.png")
pw_got15.rect = pw_got15.image.get_rect()

pw_got = pygame.sprite.Sprite()
pw_got.image = pygame.image.load("goat final.png")
pw_got.rect = pw_got.image.get_rect()

pw_got_kill = pygame.sprite.Sprite()
pw_got_kill.image = pygame.image.load("kill goat.png")
pw_got_kill.rect = pw_got15.image.get_rect()
# ------------------------------------------------------------------------------------------


# ------------------------------------------------------------------------------------------

cor_x = 0
cor_y = 0
or_x = 0
or_y = 0
index = 0
index2 = 0

points = [[569, 11, 621, 56],
          [194, 240, 241, 285],
          [249, 240, 473, 285],
          [528, 240, 575, 285],
          [628, 240, 675, 285],
          [717, 240, 763, 285],
          [942, 240, 988, 285],
          [192, 350, 239, 394],
          [365, 350, 408, 394],
          [504, 350, 547, 394],
          [655, 350, 698, 394],
          [770, 350, 827, 394],
          [943, 350, 985, 394],
          [196, 456, 239, 498],
          [307, 456, 350, 498],
          [484, 456, 528, 498],
          [679, 456, 723, 498],
          [841, 456, 884, 498],
          [942, 456, 987, 498],
          [192, 651, 238, 700],
          [441, 651, 485, 700],
          [724, 651, 769, 700],
          [955, 651, 1004, 700]]
orginal_points = [[565, 10],
                  [188, 230],
                  [420, 230],
                  [515, 230],
                  [620, 230],
                  [710, 230],
                  [930, 240],
                  [190, 340],
                  [360, 340],
                  [498, 340],
                  [640, 340],
                  [770, 340],
                  [930, 340],
                  [185, 440],
                  [298, 440],
                  [475, 440],
                  [668, 440],
                  [830, 440],
                  [933, 440],
                  [190, 650],
                  [430, 650],
                  [720, 650],
                  [950, 650]]

possible_move = [[2, 3, 4, 5],
                 [2, 7, -1, -1],
                 [0, 1, 3, 8],
                 [0, 2, 4, 9],
                 [0, 3, 5, 10],
                 [0, 4, 6, 11],
                 [5, 12, -1, -1],
                 [1, 8, 13, -1],
                 [2, 7, 9, 14],
                 [3, 8, 10, 15],
                 [4, 9, 11, 16],
                 [5, 10, 12, 17],
                 [6, 11, 18, -1],
                 [7, 14, -1, -1],
                 [8, 13, 15, 19],
                 [9, 14, 16, 20],
                 [10, 15, 17, 21],
                 [11, 16, 18, 22],
                 [12, 17, -1, -1],
                 [14, 20, -1, -1],
                 [15, 19, 21, -1],
                 [16, 20, 22, -1],
                 [17, 21, -1, -1]]

occupied_tiger = [[565, 10],
                  [420, 230],
                  [710, 230]]
tiger_kill = [[[2, 8], [3, 9], [4, 10], [5, 11]],
              [[2, 3], [7, 13], [-1, -1], [-1, -1]],
              [[3, 4], [8, 14], [-1, -1], [-1, -1]],
              [[2, 1], [4, 5], [9, 15], [-1, -1]],
              [[3, 2], [5, 6], [10, 16], [-1, -1]],
              [[4, 3], [11, 17], [-1, -1], [-1, -1]],
              [[5, 4], [12, 18], [-1, -1], [-1, -1]],
              [[8, 9], [-1, -1], [-1, -1], [-1, -1]],
              [[2, 0], [9, 10], [14, 19], [-1, -1]],
              [[3, 0], [10, 11], [15, 20], [8, 7]],
              [[4, 0], [11, 12], [16, 21], [9, 8]],
              [[5, 0], [17, 22], [10, 9], [-1, -1]],
              [[11, 10], [-1, -1], [-1, -1], [-1, -1]],
              [[7, 1], [14, 15], [-1, -1], [-1, -1]],
              [[8, 2], [15, 16], [-1, -1], [-1, -1]],
              [[9, 3], [14, 13], [16, 17], [-1, -1]],
              [[10, 4], [15, 14], [17, 18], [-1, -1]],
              [[11, 5], [16, 15], [-1, -1], [-1, -1]],
              [[12, 6], [17, 16], [-1, -1], [-1, -1]],
              [[14, 8], [20, 21], [-1, -1], [-1, -1]],
              [[15, 9], [21, 22], [-1, -1], [-1, -1]],
              [[16, 10], [20, 19], [-1, -1], [-1, -1]],
              [[17, 11], [21, 20], [-1, -1], [-1, -1]]]
tiger_index = [0, 2, 5]
slist = [0, 1, 2]
gameExit = False
occupied_goat = [[0, 0],
                 [0, 0],
                 [0, 0],
                 [0, 0],
                 [0, 0],
                 [0, 0],
                 [0, 0],
                 [0, 0],
                 [0, 0],
                 [0, 0],
                 [0, 0],
                 [0, 0],
                 [0, 0],
                 [0, 0],
                 [0, 0]]
cnt = 0
ctr2 = 0

gtcnt = 0
background=pygame.image.load("background.png")
gwin=pygame.image.load("gwins.png")
twin=pygame.image.load("TWIN.png")
j = 0
q2 = 0
m2 = 0
flag = 0
flag4 = 0
x = 0
y = 0
pindex = 0
qindex = 0
qindex2 = 0
or_y3 = 0
or_x3 = 0
flag2 = 0
flag3 = 0
flag5 = 0
flag6 = 0
flag7 = 0
cnt2 = 0
ctr = 0
or_x2 = 0
or_y2 = 0

oc_point = 0
tindex = 0
o_point = 0
or_x4 = 0
or_y4 = 0
gindex = -1
or_x5 = 0
or_y5 = 0
oc_point2 = 0
cnt3 = 0
oc_point3 = 0
or_x6 = 0
or_y6 = 0
flag8 = 0
win_tiger = 0
flag11 = 0
cnt4 = 0
flag12 = 0
flag13 = 0
flag14 = 0
flag15 = 0
flag16 = 0
flag17 = 0
flag18 = 0
flag21 = 0
tindex2 = 0
tindex3 = 0
move_list = empty([1, 4], numpy.int32)
move = 0
flag22 = 0
flag23 = 0
or_x7 = 0
or_y7 = 0
move2 = 0
cnt5 = 0
flag24 = 0
cnt6 = 0
cnt7 = 0
cnt8 = 0
flag25 = 0
flag26 = 0
flag27 = 0
flag28 = 0
flag29 = 0
flag30 = 0
flag31=0
flag32=0
flag33=0
flag34=0
or_x9=0
or_y9=0
or_x10=0
or_y8=0
or_x8=0
or_y10=0
or_x11=0
or_x12=0
or_x13=0
or_x14=0
or_x15=0
or_x16=0
or_x17=0
or_x18=0
or_y11=0
or_y12=0
or_y13=0
or_y14=0
or_y15=0
or_y16=0
or_y17=0
or_y18=0
flag35=0
flag36=0
flag37=0
flag38=0
flag39=0
flag40=0
flag41=0
flag42=0
flag43=0
flag44=0
flag45=0
flag46=0
flag47=0
flag48=0
flag49=0
flag50=0
flag51=0
flag52=0
flag53=0
flag54=0
flag55=0
flag56=0
or_x19=0
or_x20=0
or_y19=0
or_y20=0
oc_point4=0
oc_point5=0
oc_point6=0
tindex7=0
tindex8=0
gindex2=0
gindex3=0
tindex4=0
or_x21=0
or_x22=0
or_y21=0
or_y22=0
move_list2=empty([1,4],numpy.int32)
tindex5=0
move_list3=empty([1,4],numpy.int32)
tindex6=0
move_list4=empty([1,4],numpy.int32)

c1 = pygame.time.Clock()


def goto2(l):
    global line2
    line2 = l


line2 = 1


def goto(linenum):
    global line
    line = linenum


line = 1


def goto3(l2):
    global line3
    line3 = l2


line3 = 1
def goto4(l4):
    global line4
    line4 = l4


line4 = 1
def goto5(l5):
    global line5
    line5 = l5


line5 = 1


while not gameExit:
    if line5 == 1:
        for event2 in pygame.event.get():


                gameDisplay.blit(rule, (0, 0))
                pygame.display.update()
                if event2.type == pygame.MOUSEBUTTONDOWN:
                    x5, y5 = pygame.mouse.get_pos()
                    if x5 >= 971 and x5 <= 1250:
                        if y5 >= 639 and y5 <= 688:

                            goto5(2)
                if event2.type == pygame.QUIT:
                    gameExit = True
    if line5 == 2:
        cor_x = 0
        cor_y = 0
        or_x = 0
        or_y = 0
        index = 0
        index2 = 0

        points = [[569, 11, 621, 56],
                  [194, 240, 241, 285],
                  [249, 240, 473, 285],
                  [528, 240, 575, 285],
                  [628, 240, 675, 285],
                  [717, 240, 763, 285],
                  [942, 240, 988, 285],
                  [192, 350, 239, 394],
                  [365, 350, 408, 394],
                  [504, 350, 547, 394],
                  [655, 350, 698, 394],
                  [770, 350, 827, 394],
                  [943, 350, 985, 394],
                  [196, 456, 239, 498],
                  [307, 456, 350, 498],
                  [484, 456, 528, 498],
                  [679, 456, 723, 498],
                  [841, 456, 884, 498],
                  [942, 456, 987, 498],
                  [192, 651, 238, 700],
                  [441, 651, 485, 700],
                  [724, 651, 769, 700],
                  [955, 651, 1004, 700]]
        orginal_points = [[565, 10],
                          [188, 230],
                          [420, 230],
                          [515, 230],
                          [620, 230],
                          [710, 230],
                          [930, 240],
                          [190, 340],
                          [360, 340],
                          [498, 340],
                          [640, 340],
                          [770, 340],
                          [930, 340],
                          [185, 440],
                          [298, 440],
                          [475, 440],
                          [668, 440],
                          [830, 440],
                          [933, 440],
                          [190, 650],
                          [430, 650],
                          [720, 650],
                          [950, 650]]

        possible_move = [[2, 3, 4, 5],
                         [2, 7, -1, -1],
                         [0, 1, 3, 8],
                         [0, 2, 4, 9],
                         [0, 3, 5, 10],
                         [0, 4, 6, 11],
                         [5, 12, -1, -1],
                         [1, 8, 13, -1],
                         [2, 7, 9, 14],
                         [3, 8, 10, 15],
                         [4, 9, 11, 16],
                         [5, 10, 12, 17],
                         [6, 11, 18, -1],
                         [7, 14, -1, -1],
                         [8, 13, 15, 19],
                         [9, 14, 16, 20],
                         [10, 15, 17, 21],
                         [11, 16, 18, 22],
                         [12, 17, -1, -1],
                         [14, 20, -1, -1],
                         [15, 19, 21, -1],
                         [16, 20, 22, -1],
                         [17, 21, -1, -1]]

        occupied_tiger = [[565, 10],
                          [420, 230],
                          [710, 230]]
        tiger_kill = [[[2, 8], [3, 9], [4, 10], [5, 11]],
                      [[2, 3], [7, 13], [-1, -1], [-1, -1]],
                      [[3, 4], [8, 14], [-1, -1], [-1, -1]],
                      [[2, 1], [4, 5], [9, 15], [-1, -1]],
                      [[3, 2], [5, 6], [10, 16], [-1, -1]],
                      [[4, 3], [11, 17], [-1, -1], [-1, -1]],
                      [[5, 4], [12, 18], [-1, -1], [-1, -1]],
                      [[8, 9], [-1, -1], [-1, -1], [-1, -1]],
                      [[2, 0], [9, 10], [14, 19], [-1, -1]],
                      [[3, 0], [10, 11], [15, 20], [8, 7]],
                      [[4, 0], [11, 12], [16, 21], [9, 8]],
                      [[5, 0], [17, 22], [10, 9], [-1, -1]],
                      [[11, 10], [-1, -1], [-1, -1], [-1, -1]],
                      [[7, 1], [14, 15], [-1, -1], [-1, -1]],
                      [[8, 2], [15, 16], [-1, -1], [-1, -1]],
                      [[9, 3], [14, 13], [16, 17], [-1, -1]],
                      [[10, 4], [15, 14], [17, 18], [-1, -1]],
                      [[11, 5], [16, 15], [-1, -1], [-1, -1]],
                      [[12, 6], [17, 16], [-1, -1], [-1, -1]],
                      [[14, 8], [20, 21], [-1, -1], [-1, -1]],
                      [[15, 9], [21, 22], [-1, -1], [-1, -1]],
                      [[16, 10], [20, 19], [-1, -1], [-1, -1]],
                      [[17, 11], [21, 20], [-1, -1], [-1, -1]]]
        tiger_index = [0, 2, 5]
        slist = [0, 1, 2]
        gameExit = False
        occupied_goat = [[0, 0],
                         [0, 0],
                         [0, 0],
                         [0, 0],
                         [0, 0],
                         [0, 0],
                         [0, 0],
                         [0, 0],
                         [0, 0],
                         [0, 0],
                         [0, 0],
                         [0, 0],
                         [0, 0],
                         [0, 0],
                         [0, 0]]
        cnt = 0
        ctr2 = 0

        gtcnt = 0
        background = pygame.image.load("background.png")
        gwin = pygame.image.load("gwins.png")
        twin = pygame.image.load("TWIN.png")
        j = 0
        q2 = 0
        m2 = 0
        flag = 0
        flag4 = 0
        x = 0
        y = 0
        pindex = 0
        qindex = 0
        qindex2 = 0
        or_y3 = 0
        or_x3 = 0
        flag2 = 0
        flag3 = 0
        flag5 = 0
        flag6 = 0
        flag7 = 0
        cnt2 = 0
        ctr = 0
        or_x2 = 0
        or_y2 = 0

        oc_point = 0
        tindex = 0
        o_point = 0
        or_x4 = 0
        or_y4 = 0
        gindex = -1
        or_x5 = 0
        or_y5 = 0
        oc_point2 = 0
        cnt3 = 0
        oc_point3 = 0
        or_x6 = 0
        or_y6 = 0
        flag8 = 0
        win_tiger = 0
        flag11 = 0
        cnt4 = 0
        flag12 = 0
        flag13 = 0
        flag14 = 0
        flag15 = 0
        flag16 = 0
        flag17 = 0
        flag18 = 0
        flag21 = 0
        tindex2 = 0
        tindex3 = 0
        move_list = empty([1, 4], numpy.int32)
        move = 0
        flag22 = 0
        flag23 = 0
        or_x7 = 0
        or_y7 = 0
        move2 = 0
        cnt5 = 0
        flag24 = 0
        cnt6 = 0
        cnt7 = 0
        cnt8 = 0
        flag25 = 0
        flag26 = 0
        flag27 = 0
        flag28 = 0
        flag29 = 0
        flag30 = 0
        flag31 = 0
        flag32 = 0
        flag33 = 0
        flag34 = 0
        or_x9 = 0
        or_y9 = 0
        or_x10 = 0
        or_y8 = 0
        or_x8 = 0
        or_y10 = 0
        or_x11 = 0
        or_x12 = 0
        or_x13 = 0
        or_x14 = 0
        or_x15 = 0
        or_x16 = 0
        or_x17 = 0
        or_x18 = 0
        or_y11 = 0
        or_y12 = 0
        or_y13 = 0
        or_y14 = 0
        or_y15 = 0
        or_y16 = 0
        or_y17 = 0
        or_y18 = 0
        flag35 = 0
        flag36 = 0
        flag37 = 0
        flag38 = 0
        flag39 = 0
        flag40 = 0
        flag41 = 0
        flag42 = 0
        flag43 = 0
        flag44 = 0
        flag45 = 0
        flag46 = 0
        flag47 = 0
        flag48 = 0
        flag49 = 0
        flag50 = 0
        flag51 = 0
        flag52 = 0
        flag53 = 0
        flag54 = 0
        flag55 = 0
        flag56 = 0
        or_x19 = 0
        or_x20 = 0
        or_y19 = 0
        or_y20 = 0
        oc_point4 = 0
        oc_point5 = 0
        oc_point6 = 0
        tindex7 = 0
        tindex8 = 0
        gindex2 = 0
        gindex3 = 0
        tindex4 = 0
        or_x21 = 0
        or_x22 = 0
        or_y21 = 0
        or_y22 = 0
        move_list2 = empty([1, 4], numpy.int32)
        tindex5 = 0
        move_list3 = empty([1, 4], numpy.int32)
        tindex6 = 0
        move_list4 = empty([1, 4], numpy.int32)

        c1 = pygame.time.Clock()

        if gtcnt == 0:
            gameDisplay.blit(background, (0, 0))
            myfont = pygame.font.SysFont("Cosmic Sans", 100)
            text = myfont.render("0/15", True, WHITE)

            gameDisplay.blit(text, (1200, 350))

        if gtcnt == 1:
            gameDisplay.blit(background, (0, 0))
            myfont = pygame.font.SysFont("Cosmic Sans", 100)
            text = myfont.render("1/15", True, WHITE)

            gameDisplay.blit(text, (1200, 350))

        if gtcnt == 2:
            gameDisplay.blit(background, (0, 0))
            myfont = pygame.font.SysFont("Cosmic Sans", 100)
            text = myfont.render("2/15", True, WHITE)

            gameDisplay.blit(text, (1200, 350))

        if gtcnt == 3:
            gameDisplay.blit(background, (0, 0))
            myfont = pygame.font.SysFont("Cosmic Sans", 100)
            text = myfont.render("3/15", True, WHITE)

            gameDisplay.blit(text, (1200, 350))

        if gtcnt == 4:
            gameDisplay.blit(background, (0, 0))
            myfont = pygame.font.SysFont("Cosmic Sans", 100)
            text = myfont.render("4/15", True, WHITE)

            gameDisplay.blit(text, (1200, 350))

        if gtcnt == 5:
            gameDisplay.blit(background, (0, 0))
            myfont = pygame.font.SysFont("Cosmic Sans", 100)
            text = myfont.render("5/15", True, WHITE)

            gameDisplay.blit(text, (1200, 350))

        if gtcnt == 6:
            gameDisplay.blit(background, (0, 0))
            myfont = pygame.font.SysFont("Cosmic Sans", 100)
            text = myfont.render("6/15", True, WHITE)

            gameDisplay.blit(text, (1200, 350))

        if gtcnt == 7:
            gameDisplay.blit(background, (0, 0))
            myfont = pygame.font.SysFont("Cosmic Sans", 100)
            text = myfont.render("7/15", True, WHITE)

            gameDisplay.blit(text, (1200, 350))

        if gtcnt == 8:
            gameDisplay.blit(background, (0, 0))
            myfont = pygame.font.SysFont("Cosmic Sans", 100)
            text = myfont.render("8/15", True, WHITE)

            gameDisplay.blit(text, (1200, 350))

        if gtcnt == 9:
            gameDisplay.blit(background, (0, 0))
            myfont = pygame.font.SysFont("Cosmic Sans", 100)
            text = myfont.render("9/15", True, WHITE)

            gameDisplay.blit(text, (1200, 350))

        if gtcnt == 10:
            gameDisplay.blit(background, (0, 0))
            myfont = pygame.font.SysFont("Cosmic Sans", 100)
            text = myfont.render("10/15", True, WHITE)

            gameDisplay.blit(text, (1200, 350))

        if gtcnt == 11:
            gameDisplay.blit(background, (0, 0))
            myfont = pygame.font.SysFont("Cosmic Sans", 100)
            text = myfont.render("11/15", True, WHITE)

            gameDisplay.blit(text, (1200, 350))

        if gtcnt == 12:
            gameDisplay.blit(background, (0, 0))
            myfont = pygame.font.SysFont("Cosmic Sans", 100)
            text = myfont.render("12/15", True, WHITE)

            gameDisplay.blit(text, (1200, 350))

        if gtcnt == 13:
            gameDisplay.blit(background, (0, 0))
            myfont = pygame.font.SysFont("Cosmic Sans", 100)
            text = myfont.render("13/15", True, WHITE)

            gameDisplay.blit(text, (1200, 350))

        if gtcnt == 14:
            gameDisplay.blit(background, (0, 0))
            myfont = pygame.font.SysFont("Cosmic Sans", 100)
            text = myfont.render("14/15", True, WHITE)

            gameDisplay.blit(text, (1200, 350))

        if gtcnt == 15:
            gameDisplay.blit(background, (0, 0))
            myfont = pygame.font.SysFont("Cosmic Sans", 100)
            text = myfont.render("15/15", True, WHITE)

            gameDisplay.blit(text, (1200, 350))

        if win_tiger == 0:
            myfont = pygame.font.SysFont("Cosmic Sans", 100)
            text = myfont.render("0/5", True, WHITE)

            gameDisplay.blit(text, (1200, 200))

        if win_tiger == 1:
            myfont = pygame.font.SysFont("Cosmic Sans", 100)
            text = myfont.render("1/5", True, WHITE)

            gameDisplay.blit(text, (1200, 200))



        if win_tiger == 2:
            myfont = pygame.font.SysFont("Cosmic Sans", 100)
            text = myfont.render("2/5", True, WHITE)

            gameDisplay.blit(text, (1200, 200))



        if win_tiger == 3:
            myfont = pygame.font.SysFont("Cosmic Sans", 100)
            text = myfont.render("3/5", True, WHITE)

            gameDisplay.blit(text, (1200, 200))



        if win_tiger == 4:
            myfont = pygame.font.SysFont("Cosmic Sans", 100)
            text = myfont.render("4/5", True, WHITE)

            gameDisplay.blit(text, (1200, 200))



        if win_tiger == 5:
            myfont = pygame.font.SysFont("Cosmic Sans", 100)
            text = myfont.render("5/5", True, WHITE)

            gameDisplay.blit(text, (1200, 200))



        gameDisplay.blit(bg, (0, 0))
        gameDisplay.blit(pw_got.image, (1100, 350))
        gameDisplay.blit(pw_got_kill.image, (1100, 200))

        for i in range(0, 15):

            if i == 0:
                if occupied_goat[i][0] > 0 and occupied_goat[i][1] > 0:
                    gameDisplay.blit(pw_got1.image,
                                     (occupied_goat[i][0], occupied_goat[i][1]))
                # pygame.display.update()
                # clock.tick(50000)

            if i == 1:
                if occupied_goat[i][0] > 0 and occupied_goat[i][1] > 0:
                    gameDisplay.blit(pw_got2.image,
                                     (occupied_goat[i][0], occupied_goat[i][1]))
                # pygame.display.update()
                # clock.tick(50000)

            if i == 2:
                if occupied_goat[i][0] > 0 and occupied_goat[i][1] > 0:
                    gameDisplay.blit(pw_got3.image,
                                     (occupied_goat[i][0], occupied_goat[i][1]))
                # pygame.display.update()
                # clock.tick(50000)

            if i == 3:
                if occupied_goat[i][0] > 0 and occupied_goat[i][1] > 0:
                    gameDisplay.blit(pw_got4.image,
                                     (occupied_goat[i][0], occupied_goat[i][1]))
                # pygame.display.update()
                # clock.tick(50000)

            if i == 4:
                if occupied_goat[i][0] > 0 and occupied_goat[i][1] > 0:
                    gameDisplay.blit(pw_got5.image,
                                     (occupied_goat[i][0], occupied_goat[i][1]))
                # pygame.display.update()
                # clock.tick(50000)

            if i == 5:
                if occupied_goat[i][0] > 0 and occupied_goat[i][1] > 0:
                    gameDisplay.blit(pw_got6.image,
                                     (occupied_goat[i][0], occupied_goat[i][1]))
                # pygame.display.update()
                # clock.tick(50000)

            if i == 6:
                if occupied_goat[i][0] > 0 and occupied_goat[i][1] > 0:
                    gameDisplay.blit(pw_got7.image,
                                     (occupied_goat[i][0], occupied_goat[i][1]))
                # pygame.display.update()
                # clock.tick(50000)

            if i == 7:
                if occupied_goat[i][0] > 0 and occupied_goat[i][1] > 0:
                    gameDisplay.blit(pw_got8.image,
                                     (occupied_goat[i][0], occupied_goat[i][1]))
                # pygame.display.update()
                # clock.tick(50000)

            if i == 8:
                if occupied_goat[i][0] > 0 and occupied_goat[i][1] > 0:
                    gameDisplay.blit(pw_got9.image,
                                     (occupied_goat[i][0], occupied_goat[i][1]))
                # pygame.display.update()
                # clock.tick(50000)

            if i == 9:
                if occupied_goat[i][0] > 0 and occupied_goat[i][1] > 0:
                    gameDisplay.blit(pw_got10.image,
                                     (occupied_goat[i][0], occupied_goat[i][1]))
                # pygame.display.update()
                # clock.tick(50000)

            if i == 10:
                if occupied_goat[i][0] > 0 and occupied_goat[i][1] > 0:
                    gameDisplay.blit(pw_got11.image,
                                     (occupied_goat[i][0], occupied_goat[i][1]))
                # pygame.display.update()
                # clock.tick(50000)

            if i == 11:
                if occupied_goat[i][0] > 0 and occupied_goat[i][1] > 0:
                    gameDisplay.blit(pw_got12.image,
                                     (occupied_goat[i][0], occupied_goat[i][1]))
                # pygame.display.update()
                # clock.tick(50000)

            if i == 12:
                if occupied_goat[i][0] > 0 and occupied_goat[i][1] > 0:
                    gameDisplay.blit(pw_got13.image,
                                     (occupied_goat[i][0], occupied_goat[i][1]))
                # pygame.display.update()
                # clock.tick(50000)

            if i == 13:
                if occupied_goat[i][0] > 0 and occupied_goat[i][1] > 0:
                    gameDisplay.blit(pw_got14.image,
                                     (occupied_goat[i][0], occupied_goat[i][1]))
                # pygame.display.update()
                # clock.tick(50000)

            if i == 14:
                if occupied_goat[i][0] > 0 and occupied_goat[i][1] > 0:
                    gameDisplay.blit(pw_got15.image,
                                     (occupied_goat[i][0], occupied_goat[i][1]))
                # pygame.display.update()
                # clock.tick(50000)
        for e in range(0, 3):
            if e == 0:
                gameDisplay.blit(pw_tig1.image,
                                 (occupied_tiger[e][0], occupied_tiger[e][1]))
            if e == 1:
                gameDisplay.blit(pw_tig2.image,
                                 (occupied_tiger[e][0], occupied_tiger[e][1]))
            if e == 2:
                gameDisplay.blit(pw_tig3.image,
                                 (occupied_tiger[e][0], occupied_tiger[e][1]))
            # clock.tick(50000)

        pygame.display.update()
        goto5(3)

    if line5 == 3:



        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                gameExit = True
            if line2 == 1:

                    flag21 = 0
                    cnt3 = 0
                    cnt4 = 0
                    cnt6 = 0
                    if event.type == pygame.MOUSEBUTTONDOWN:

                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if flag4 == 1:
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    flag4 = 0
                                    flag5 = 0
                                    flag3 = 0
                                    or_x3 = 0
                                    or_y3 = 0
                                    qindex2 = 0
                                    q2 = 0

                                    flag7 = 0
                                    goto(1)

                            if line == 1:
                                if x != 0 and y != 0:

                                    cor_x3, cor_y3 = pygame.mouse.get_pos()

                                    for q2 in range(0, 23):
                                        if cor_x3 >= points[q2][0] and cor_x3 <= points[q2][2]:
                                            if cor_y3 >= points[q2][1] and cor_y3 <= points[q2][3]:
                                                qindex2 = q2
                                                or_x3 = orginal_points[qindex2][0]
                                                or_y3 = orginal_points[qindex2][1]
                                                if pindex == 14:
                                                    for w in range(0, 3):
                                                        if or_x3 == occupied_tiger[w][0] and or_y3 == occupied_tiger[w][
                                                            1]:
                                                            flag5 = 1
                                                    for n in range(0, 15):

                                                        if or_x3 == occupied_goat[n][0] and or_y3 == occupied_goat[n][
                                                            1]:
                                                            flag3 = 1

                                                    if flag3 == 0 and flag5 == 0:
                                                        for l in range(0, 23):
                                                            if qindex == l:
                                                                if qindex2 == possible_move[l][0] or qindex2 == \
                                                                        possible_move[l][1] or qindex2 == \
                                                                        possible_move[l][2] or qindex2 == \
                                                                        possible_move[l][3]:
                                                                    occupied_goat[pindex][0] = or_x3
                                                                    occupied_goat[pindex][1] = or_y3

                                                                    gameDisplay.blit(bg, (0, 0))
                                                                    break
                                                                else:
                                                                    flag7 = 1

                                                    if flag3 == 1 or flag5 == 1 or flag7 == 1:
                                                        flag4 = 1

                                                # pygame.display.update()
                                                # clock.tick(50000)

                                                if pindex == 13:

                                                    for w in range(0, 3):
                                                        if or_x3 == occupied_tiger[w][0] and or_y3 == occupied_tiger[w][
                                                            1]:
                                                            flag5 = 1
                                                    for n in range(0, 15):

                                                        if or_x3 == occupied_goat[n][0] and or_y3 == occupied_goat[n][
                                                            1]:
                                                            flag3 = 1

                                                    if flag3 == 0 and flag5 == 0:
                                                        for l in range(0, 23):
                                                            if qindex == l:
                                                                if qindex2 == possible_move[l][0] or qindex2 == \
                                                                        possible_move[l][1] or qindex2 == \
                                                                        possible_move[l][2] or qindex2 == \
                                                                        possible_move[l][3]:
                                                                    occupied_goat[pindex][0] = or_x3
                                                                    occupied_goat[pindex][1] = or_y3

                                                                    gameDisplay.blit(bg, (0, 0))
                                                                    break
                                                                else:
                                                                    flag7 = 1

                                                    if flag3 == 1 or flag5 == 1 or flag7 == 1:
                                                        flag4 = 1

                                                # clock.tick(50000)

                                                if pindex == 12:

                                                    for w in range(0, 3):
                                                        if or_x3 == occupied_tiger[w][0] and or_y3 == occupied_tiger[w][
                                                            1]:
                                                            flag5 = 1
                                                    for n in range(0, 15):

                                                        if or_x3 == occupied_goat[n][0] and or_y3 == occupied_goat[n][
                                                            1]:
                                                            flag3 = 1

                                                    if flag3 == 0 and flag5 == 0:
                                                        for l in range(0, 23):
                                                            if qindex == l:
                                                                if qindex2 == possible_move[l][0] or qindex2 == \
                                                                        possible_move[l][1] or qindex2 == \
                                                                        possible_move[l][2] or qindex2 == \
                                                                        possible_move[l][3]:
                                                                    occupied_goat[pindex][0] = or_x3
                                                                    occupied_goat[pindex][1] = or_y3

                                                                    gameDisplay.blit(bg, (0, 0))
                                                                    break
                                                                else:
                                                                    flag7 = 1

                                                    if flag3 == 1 or flag5 == 1 or flag7 == 1:
                                                        flag4 = 1

                                                # clock.tick(50000)

                                                if pindex == 11:

                                                    for w in range(0, 3):
                                                        if or_x3 == occupied_tiger[w][0] and or_y3 == occupied_tiger[w][
                                                            1]:
                                                            flag5 = 1
                                                    for n in range(0, 15):

                                                        if or_x3 == occupied_goat[n][0] and or_y3 == occupied_goat[n][
                                                            1]:
                                                            flag3 = 1

                                                    if flag3 == 0 and flag5 == 0:
                                                        for l in range(0, 23):
                                                            if qindex == l:
                                                                if qindex2 == possible_move[l][0] or qindex2 == \
                                                                        possible_move[l][1] or qindex2 == \
                                                                        possible_move[l][2] or qindex2 == \
                                                                        possible_move[l][3]:
                                                                    occupied_goat[pindex][0] = or_x3
                                                                    occupied_goat[pindex][1] = or_y3

                                                                    gameDisplay.blit(bg, (0, 0))
                                                                    break
                                                                else:
                                                                    flag7 = 1

                                                    if flag3 == 1 or flag5 == 1 or flag7 == 1:
                                                        flag4 = 1

                                                # pygame.display.update()
                                                # clock.tick(50000)

                                                if pindex == 10:

                                                    for w in range(0, 3):
                                                        if or_x3 == occupied_tiger[w][0] and or_y3 == occupied_tiger[w][
                                                            1]:
                                                            flag5 = 1
                                                    for n in range(0, 15):

                                                        if or_x3 == occupied_goat[n][0] and or_y3 == occupied_goat[n][
                                                            1]:
                                                            flag3 = 1

                                                    if flag3 == 0 and flag5 == 0:
                                                        for l in range(0, 23):
                                                            if qindex == l:
                                                                if qindex2 == possible_move[l][0] or qindex2 == \
                                                                        possible_move[l][1] or qindex2 == \
                                                                        possible_move[l][2] or qindex2 == \
                                                                        possible_move[l][3]:
                                                                    occupied_goat[pindex][0] = or_x3
                                                                    occupied_goat[pindex][1] = or_y3

                                                                    gameDisplay.blit(bg, (0, 0))
                                                                    break
                                                                else:
                                                                    flag7 = 1

                                                    if flag3 == 1 or flag5 == 1 or flag7 == 1:
                                                        flag4 = 1

                                                # pygame.display.update()
                                                # clock.tick(50000)

                                                if pindex == 9:

                                                    for w in range(0, 3):
                                                        if or_x3 == occupied_tiger[w][0] and or_y3 == occupied_tiger[w][
                                                            1]:
                                                            flag5 = 1
                                                    for n in range(0, 15):

                                                        if or_x3 == occupied_goat[n][0] and or_y3 == occupied_goat[n][
                                                            1]:
                                                            flag3 = 1

                                                    if flag3 == 0 and flag5 == 0:
                                                        for l in range(0, 23):
                                                            if qindex == l:
                                                                if qindex2 == possible_move[l][0] or qindex2 == \
                                                                        possible_move[l][1] or qindex2 == \
                                                                        possible_move[l][2] or qindex2 == \
                                                                        possible_move[l][3]:
                                                                    occupied_goat[pindex][0] = or_x3
                                                                    occupied_goat[pindex][1] = or_y3

                                                                    gameDisplay.blit(bg, (0, 0))
                                                                    break
                                                                else:
                                                                    flag7 = 1

                                                    if flag3 == 1 or flag5 == 1 or flag7 == 1:
                                                        flag4 = 1

                                                if pindex == 8:

                                                    for w in range(0, 3):
                                                        if or_x3 == occupied_tiger[w][0] and or_y3 == occupied_tiger[w][
                                                            1]:
                                                            flag5 = 1
                                                    for n in range(0, 15):

                                                        if or_x3 == occupied_goat[n][0] and or_y3 == occupied_goat[n][
                                                            1]:
                                                            flag3 = 1

                                                    if flag3 == 0 and flag5 == 0:
                                                        for l in range(0, 23):
                                                            if qindex == l:
                                                                if qindex2 == possible_move[l][0] or qindex2 == \
                                                                        possible_move[l][1] or qindex2 == \
                                                                        possible_move[l][2] or qindex2 == \
                                                                        possible_move[l][3]:
                                                                    occupied_goat[pindex][0] = or_x3
                                                                    occupied_goat[pindex][1] = or_y3

                                                                    gameDisplay.blit(bg, (0, 0))
                                                                    break
                                                                else:
                                                                    flag7 = 1

                                                    if flag3 == 1 or flag5 == 1 or flag7 == 1:
                                                        flag4 = 1

                                                if pindex == 7:

                                                    for w in range(0, 3):
                                                        if or_x3 == occupied_tiger[w][0] and or_y3 == occupied_tiger[w][
                                                            1]:
                                                            flag5 = 1
                                                    for n in range(0, 15):

                                                        if or_x3 == occupied_goat[n][0] and or_y3 == occupied_goat[n][
                                                            1]:
                                                            flag3 = 1

                                                    if flag3 == 0 and flag5 == 0:
                                                        for l in range(0, 23):
                                                            if qindex == l:
                                                                if qindex2 == possible_move[l][0] or qindex2 == \
                                                                        possible_move[l][1] or qindex2 == \
                                                                        possible_move[l][2] or qindex2 == \
                                                                        possible_move[l][3]:
                                                                    occupied_goat[pindex][0] = or_x3
                                                                    occupied_goat[pindex][1] = or_y3

                                                                    gameDisplay.blit(bg, (0, 0))
                                                                    break
                                                                else:
                                                                    flag7 = 1

                                                    if flag3 == 1 or flag5 == 1 or flag7 == 1:
                                                        flag4 = 1

                                                if pindex == 6:

                                                    for w in range(0, 3):
                                                        if or_x3 == occupied_tiger[w][0] and or_y3 == occupied_tiger[w][
                                                            1]:
                                                            flag5 = 1
                                                    for n in range(0, 15):

                                                        if or_x3 == occupied_goat[n][0] and or_y3 == occupied_goat[n][
                                                            1]:
                                                            flag3 = 1

                                                    if flag3 == 0 and flag5 == 0:
                                                        for l in range(0, 23):
                                                            if qindex == l:
                                                                if qindex2 == possible_move[l][0] or qindex2 == \
                                                                        possible_move[l][1] or qindex2 == \
                                                                        possible_move[l][2] or qindex2 == \
                                                                        possible_move[l][3]:
                                                                    occupied_goat[pindex][0] = or_x3
                                                                    occupied_goat[pindex][1] = or_y3

                                                                    gameDisplay.blit(bg, (0, 0))
                                                                    break
                                                                else:
                                                                    flag7 = 1

                                                    if flag3 == 1 or flag5 == 1 or flag7 == 1:
                                                        flag4 = 1

                                                if pindex == 5:

                                                    for w in range(0, 3):
                                                        if or_x3 == occupied_tiger[w][0] and or_y3 == occupied_tiger[w][
                                                            1]:
                                                            flag5 = 1
                                                    for n in range(0, 15):

                                                        if or_x3 == occupied_goat[n][0] and or_y3 == occupied_goat[n][
                                                            1]:
                                                            flag3 = 1

                                                    if flag3 == 0 and flag5 == 0:
                                                        for l in range(0, 23):
                                                            if qindex == l:
                                                                if qindex2 == possible_move[l][0] or qindex2 == \
                                                                        possible_move[l][1] or qindex2 == \
                                                                        possible_move[l][2] or qindex2 == \
                                                                        possible_move[l][3]:
                                                                    occupied_goat[pindex][0] = or_x3
                                                                    occupied_goat[pindex][1] = or_y3

                                                                    gameDisplay.blit(bg, (0, 0))
                                                                    break
                                                                else:
                                                                    flag7 = 1

                                                    if flag3 == 1 or flag5 == 1 or flag7 == 1:
                                                        flag4 = 1

                                                if pindex == 4:

                                                    for w in range(0, 3):
                                                        if or_x3 == occupied_tiger[w][0] and or_y3 == occupied_tiger[w][
                                                            1]:
                                                            flag5 = 1
                                                    for n in range(0, 15):

                                                        if or_x3 == occupied_goat[n][0] and or_y3 == occupied_goat[n][
                                                            1]:
                                                            flag3 = 1

                                                    if flag3 == 0 and flag5 == 0:
                                                        for l in range(0, 23):
                                                            if qindex == l:
                                                                if qindex2 == possible_move[l][0] or qindex2 == \
                                                                        possible_move[l][1] or qindex2 == \
                                                                        possible_move[l][2] or qindex2 == \
                                                                        possible_move[l][3]:
                                                                    occupied_goat[pindex][0] = or_x3
                                                                    occupied_goat[pindex][1] = or_y3

                                                                    gameDisplay.blit(bg, (0, 0))
                                                                    break
                                                                else:
                                                                    flag7 = 1

                                                    if flag3 == 1 or flag5 == 1 or flag7 == 1:
                                                        flag4 = 1

                                                if pindex == 3:

                                                    for w in range(0, 3):
                                                        if or_x3 == occupied_tiger[w][0] and or_y3 == occupied_tiger[w][
                                                            1]:
                                                            flag5 = 1
                                                    for n in range(0, 15):

                                                        if or_x3 == occupied_goat[n][0] and or_y3 == occupied_goat[n][
                                                            1]:
                                                            flag3 = 1

                                                    if flag3 == 0 and flag5 == 0:
                                                        for l in range(0, 23):
                                                            if qindex == l:
                                                                if qindex2 == possible_move[l][0] or qindex2 == \
                                                                        possible_move[l][1] or qindex2 == \
                                                                        possible_move[l][2] or qindex2 == \
                                                                        possible_move[l][3]:
                                                                    occupied_goat[pindex][0] = or_x3
                                                                    occupied_goat[pindex][1] = or_y3

                                                                    gameDisplay.blit(bg, (0, 0))
                                                                    break
                                                                else:
                                                                    flag7 = 1

                                                    if flag3 == 1 or flag5 == 1 or flag7 == 1:
                                                        flag4 = 1

                                                if pindex == 2:

                                                    for w in range(0, 3):
                                                        if or_x3 == occupied_tiger[w][0] and or_y3 == occupied_tiger[w][
                                                            1]:
                                                            flag5 = 1
                                                    for n in range(0, 15):

                                                        if or_x3 == occupied_goat[n][0] and or_y3 == occupied_goat[n][
                                                            1]:
                                                            flag3 = 1

                                                    if flag3 == 0 and flag5 == 0:
                                                        for l in range(0, 23):
                                                            if qindex == l:
                                                                if qindex2 == possible_move[l][0] or qindex2 == \
                                                                        possible_move[l][1] or qindex2 == \
                                                                        possible_move[l][2] or qindex2 == \
                                                                        possible_move[l][3]:
                                                                    occupied_goat[pindex][0] = or_x3
                                                                    occupied_goat[pindex][1] = or_y3

                                                                    gameDisplay.blit(bg, (0, 0))
                                                                    break
                                                                else:
                                                                    flag7 = 1

                                                    if flag3 == 1 or flag5 == 1 or flag7 == 1:
                                                        flag4 = 1

                                                if pindex == 1:

                                                    for w in range(0, 3):
                                                        if or_x3 == occupied_tiger[w][0] and or_y3 == occupied_tiger[w][
                                                            1]:
                                                            flag5 = 1
                                                    for n in range(0, 15):

                                                        if or_x3 == occupied_goat[n][0] and or_y3 == occupied_goat[n][
                                                            1]:
                                                            flag3 = 1

                                                    if flag3 == 0 and flag5 == 0:
                                                        for l in range(0, 23):
                                                            if qindex == l:
                                                                if qindex2 == possible_move[l][0] or qindex2 == \
                                                                        possible_move[l][1] or qindex2 == \
                                                                        possible_move[l][2] or qindex2 == \
                                                                        possible_move[l][3]:
                                                                    occupied_goat[pindex][0] = or_x3
                                                                    occupied_goat[pindex][1] = or_y3

                                                                    gameDisplay.blit(bg, (0, 0))
                                                                    break
                                                                else:
                                                                    flag7 = 1

                                                    if flag3 == 1 or flag5 == 1 or flag7 == 1:
                                                        flag4 = 1

                                                if pindex == 0:

                                                    for w in range(0, 3):
                                                        if or_x3 == occupied_tiger[w][0] and or_y3 == occupied_tiger[w][
                                                            1]:
                                                            flag5 = 1
                                                    for n in range(0, 15):

                                                        if or_x3 == occupied_goat[n][0] and or_y3 == occupied_goat[n][
                                                            1]:
                                                            flag3 = 1

                                                    if flag3 == 0 and flag5 == 0:
                                                        for l in range(0, 23):
                                                            if qindex == l:
                                                                if qindex2 == possible_move[l][0] or qindex2 == \
                                                                        possible_move[l][1] or qindex2 == \
                                                                        possible_move[l][2] or qindex2 == \
                                                                        possible_move[l][3]:
                                                                    occupied_goat[pindex][0] = or_x3
                                                                    occupied_goat[pindex][1] = or_y3

                                                                    gameDisplay.blit(bg, (0, 0))
                                                                    break
                                                                else:
                                                                    flag7 = 1

                                                    if flag3 == 1 or flag5 == 1 or flag7 == 1:
                                                        flag4 = 1
                                                if flag7 != 1:
                                                        if gtcnt == 0:
                                                            gameDisplay.blit(background, (0, 0))
                                                            myfont = pygame.font.SysFont("Cosmic Sans", 100)
                                                            text = myfont.render("0/15", True, WHITE)

                                                            gameDisplay.blit(text, (1200, 350))

                                                        if gtcnt == 1:
                                                            gameDisplay.blit(background, (0, 0))
                                                            myfont = pygame.font.SysFont("Cosmic Sans", 100)
                                                            text = myfont.render("1/15", True, WHITE)

                                                            gameDisplay.blit(text, (1200, 350))

                                                        if gtcnt == 2:
                                                            gameDisplay.blit(background, (0, 0))
                                                            myfont = pygame.font.SysFont("Cosmic Sans", 100)
                                                            text = myfont.render("2/15", True, WHITE)

                                                            gameDisplay.blit(text, (1200, 350))

                                                        if gtcnt == 3:
                                                            gameDisplay.blit(background, (0, 0))
                                                            myfont = pygame.font.SysFont("Cosmic Sans", 100)
                                                            text = myfont.render("3/15", True, WHITE)

                                                            gameDisplay.blit(text, (1200, 350))

                                                        if gtcnt == 4:
                                                            gameDisplay.blit(background, (0, 0))
                                                            myfont = pygame.font.SysFont("Cosmic Sans", 100)
                                                            text = myfont.render("4/15", True, WHITE)

                                                            gameDisplay.blit(text, (1200, 350))

                                                        if gtcnt == 5:
                                                            gameDisplay.blit(background, (0, 0))
                                                            myfont = pygame.font.SysFont("Cosmic Sans", 100)
                                                            text = myfont.render("5/15", True, WHITE)

                                                            gameDisplay.blit(text, (1200, 350))

                                                        if gtcnt == 6:
                                                            gameDisplay.blit(background, (0, 0))
                                                            myfont = pygame.font.SysFont("Cosmic Sans", 100)
                                                            text = myfont.render("6/15", True, WHITE)

                                                            gameDisplay.blit(text, (1200, 350))

                                                        if gtcnt == 7:
                                                            gameDisplay.blit(background, (0, 0))
                                                            myfont = pygame.font.SysFont("Cosmic Sans", 100)
                                                            text = myfont.render("7/15", True, WHITE)

                                                            gameDisplay.blit(text, (1200, 350))

                                                        if gtcnt == 8:
                                                            gameDisplay.blit(background, (0, 0))
                                                            myfont = pygame.font.SysFont("Cosmic Sans", 100)
                                                            text = myfont.render("8/15", True, WHITE)

                                                            gameDisplay.blit(text, (1200, 350))

                                                        if gtcnt == 9:
                                                            gameDisplay.blit(background, (0, 0))
                                                            myfont = pygame.font.SysFont("Cosmic Sans", 100)
                                                            text = myfont.render("9/15", True, WHITE)

                                                            gameDisplay.blit(text, (1200, 350))

                                                        if gtcnt == 10:
                                                            gameDisplay.blit(background, (0, 0))
                                                            myfont = pygame.font.SysFont("Cosmic Sans", 100)
                                                            text = myfont.render("10/15", True, WHITE)

                                                            gameDisplay.blit(text, (1200, 350))

                                                        if gtcnt == 11:
                                                            gameDisplay.blit(background, (0, 0))
                                                            myfont = pygame.font.SysFont("Cosmic Sans", 100)
                                                            text = myfont.render("11/15", True, WHITE)

                                                            gameDisplay.blit(text, (1200, 350))

                                                        if gtcnt == 12:
                                                            gameDisplay.blit(background, (0, 0))
                                                            myfont = pygame.font.SysFont("Cosmic Sans", 100)
                                                            text = myfont.render("12/15", True, WHITE)

                                                            gameDisplay.blit(text, (1200, 350))

                                                        if gtcnt == 13:
                                                            gameDisplay.blit(background, (0, 0))
                                                            myfont = pygame.font.SysFont("Cosmic Sans", 100)
                                                            text = myfont.render("13/15", True, WHITE)

                                                            gameDisplay.blit(text, (1200, 350))

                                                        if gtcnt == 14:
                                                            gameDisplay.blit(background, (0, 0))
                                                            myfont = pygame.font.SysFont("Cosmic Sans", 100)
                                                            text = myfont.render("14/15", True, WHITE)

                                                            gameDisplay.blit(text, (1200, 350))

                                                        if gtcnt == 15:
                                                            gameDisplay.blit(background, (0, 0))
                                                            myfont = pygame.font.SysFont("Cosmic Sans", 100)
                                                            text = myfont.render("15/15", True, WHITE)

                                                            gameDisplay.blit(text, (1200, 350))

                                                        if win_tiger == 0:
                                                            myfont = pygame.font.SysFont("Cosmic Sans", 100)
                                                            text = myfont.render("0/5", True, WHITE)

                                                            gameDisplay.blit(text, (1200, 200))

                                                        if win_tiger == 1:
                                                            myfont = pygame.font.SysFont("Cosmic Sans", 100)
                                                            text = myfont.render("1/5", True, WHITE)

                                                            gameDisplay.blit(text, (1200, 200))

                                                        if win_tiger == 2:
                                                            myfont = pygame.font.SysFont("Cosmic Sans", 100)
                                                            text = myfont.render("2/5", True, WHITE)

                                                            gameDisplay.blit(text, (1200, 200))

                                                        if win_tiger == 3:
                                                            myfont = pygame.font.SysFont("Cosmic Sans", 100)
                                                            text = myfont.render("3/5", True, WHITE)

                                                            gameDisplay.blit(text, (1200, 200))

                                                        if win_tiger == 4:
                                                            myfont = pygame.font.SysFont("Cosmic Sans", 100)
                                                            text = myfont.render("4/5", True, WHITE)

                                                            gameDisplay.blit(text, (1200, 200))

                                                        if win_tiger == 5:
                                                            myfont = pygame.font.SysFont("Cosmic Sans", 100)
                                                            text = myfont.render("5/5", True, WHITE)

                                                            gameDisplay.blit(text, (1200, 200))

                                                        gameDisplay.blit(bg, (0, 0))
                                                        gameDisplay.blit(pw_got.image, (1100, 350))
                                                        gameDisplay.blit(pw_got_kill.image, (1100, 200))
                                                        for i in range(0, 15):

                                                            if i == 0:
                                                                gameDisplay.blit(pw_got1.image,
                                                                                 (occupied_goat[i][0],
                                                                                  occupied_goat[i][1]))
                                                                # pygame.display.update()
                                                                # clock.tick(50000)

                                                            if i == 1:
                                                                gameDisplay.blit(pw_got2.image,
                                                                                 (occupied_goat[i][0],
                                                                                  occupied_goat[i][1]))
                                                                # pygame.display.update()
                                                                # clock.tick(50000)

                                                            if i == 2:
                                                                gameDisplay.blit(pw_got3.image,
                                                                                 (occupied_goat[i][0],
                                                                                  occupied_goat[i][1]))
                                                                # pygame.display.update()
                                                                # clock.tick(50000)

                                                            if i == 3:
                                                                gameDisplay.blit(pw_got4.image,
                                                                                 (occupied_goat[i][0],
                                                                                  occupied_goat[i][1]))
                                                                # pygame.display.update()
                                                                # clock.tick(50000)

                                                            if i == 4:
                                                                gameDisplay.blit(pw_got5.image,
                                                                                 (occupied_goat[i][0],
                                                                                  occupied_goat[i][1]))
                                                                # pygame.display.update()
                                                                # clock.tick(50000)

                                                            if i == 5:
                                                                gameDisplay.blit(pw_got6.image,
                                                                                 (occupied_goat[i][0],
                                                                                  occupied_goat[i][1]))
                                                            # pygame.display.update()
                                                            # clock.tick(50000)

                                                            if i == 6:
                                                                gameDisplay.blit(pw_got7.image,
                                                                                 (occupied_goat[i][0],
                                                                                  occupied_goat[i][1]))
                                                                # pygame.display.update()
                                                            # clock.tick(50000)

                                                            if i == 7:
                                                                gameDisplay.blit(pw_got8.image,
                                                                                 (occupied_goat[i][0],
                                                                                  occupied_goat[i][1]))
                                                                # pygame.display.update()
                                                                # clock.tick(50000)

                                                            if i == 8:
                                                                gameDisplay.blit(pw_got9.image,
                                                                                 (occupied_goat[i][0],
                                                                                  occupied_goat[i][1]))
                                                                # pygame.display.update()
                                                                # clock.tick(50000)

                                                            if i == 9:
                                                                gameDisplay.blit(pw_got10.image,
                                                                                 (occupied_goat[i][0],
                                                                                  occupied_goat[i][1]))
                                                                ##pygame.display.update()
                                                                # clock.tick(50000)

                                                            if i == 10:
                                                                gameDisplay.blit(pw_got11.image,
                                                                                 (occupied_goat[i][0],
                                                                                  occupied_goat[i][1]))
                                                                # pygame.display.update()
                                                            # clock.tick(50000)

                                                            if i == 11:
                                                                gameDisplay.blit(pw_got12.image,
                                                                                 (occupied_goat[i][0],
                                                                                  occupied_goat[i][1]))
                                                                # pygame.display.update()
                                                                # clock.tick(50000)

                                                            if i == 12:
                                                                gameDisplay.blit(pw_got13.image,
                                                                                 (occupied_goat[i][0],
                                                                                  occupied_goat[i][1]))
                                                            # pygame.display.update()
                                                            # clock.tick(50000)

                                                            if i == 13:
                                                                gameDisplay.blit(pw_got14.image,
                                                                                 (occupied_goat[i][0],
                                                                                  occupied_goat[i][1]))
                                                                # pygame.display.update()
                                                            # clock.tick(50000)

                                                            if i == 14:
                                                                gameDisplay.blit(pw_got15.image,
                                                                                 (occupied_goat[i][0],
                                                                                  occupied_goat[i][1]))
                                                            # pygame.display.update()
                                                            # clock.tick(50000)

                                                        for j in range(0, 3):
                                                            if j == 0:
                                                                gameDisplay.blit(pw_tig1.image,
                                                                                 (occupied_tiger[j][0],
                                                                                  occupied_tiger[j][1]))
                                                            if j == 1:
                                                                gameDisplay.blit(pw_tig2.image,
                                                                                 (occupied_tiger[j][0],
                                                                                  occupied_tiger[j][1]))
                                                            if j == 2:
                                                                gameDisplay.blit(pw_tig3.image,
                                                                                 (occupied_tiger[j][0],
                                                                                  occupied_tiger[j][1]))
                                                            # clock.tick(50000)

                                                        pygame.display.update()
                                                        playsound(
                                                            'Goat-noise.mp3')
                                                        goto2(2)

                        if gtcnt == 15:

                                if x == 0 and y == 0:


                                    cor_x2, cor_y2 = pygame.mouse.get_pos()
                                    or_x2 = 0
                                    or_y2 = 0

                                    for q in range(23):
                                        if cor_x2 >= points[q][0] and cor_x2 <= points[q][2]:
                                            if cor_y2 >= points[q][1] and cor_y2 <= points[q][3]:
                                                qindex = q
                                                or_x2 = orginal_points[qindex][0]
                                                or_y2 = orginal_points[qindex][1]

                                    for m in range(0, 15):
                                        if or_x2 == occupied_goat[m][0]:
                                            if or_y2 == occupied_goat[m][1]:
                                                flag2 = 1
                                                pindex = m

                                    if flag2 == 1:
                                        pos = [orginal_points[qindex][0] + 34, orginal_points[qindex][1] + 34]
                                        pygame.draw.circle(gameDisplay, WHITE, pos, 40, 5)
                                        pygame.display.update()
                                        x = orginal_points[qindex][0] + 34
                                        y = orginal_points[qindex][1] + 34

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if gtcnt < 15:
                            cor_x, cor_y = pygame.mouse.get_pos()

                            for i in range(23):
                                flag = 0

                                if cor_x >= points[i][0] and cor_x <= points[i][2]:
                                    if cor_y >= points[i][1] and cor_y <= points[i][3]:
                                        index = i
                                        or_x = orginal_points[index][0]
                                        or_y = orginal_points[index][1]

                                        if gtcnt == 0:
                                            for h in range(0, 3):
                                                if or_x == occupied_tiger[h][0] and or_y == occupied_tiger[h][1]:
                                                    flag6 = 1

                                            # print(occupied_goat[ctr-1][0],occupied_goat[ctr-1][1])
                                            if flag6 == 0:
                                                gameDisplay.blit(pw_got1.image, (or_x, or_y))
                                                occupied_goat[0][0] = or_x
                                                occupied_goat[0][1] = or_y

                                                pygame.display.update()
                                                playsound('Goat-noise.mp3')
                                                goto2(2)
                                            if flag6 == 1:
                                                gtcnt = gtcnt - 1

                                        if gtcnt == 1:
                                            # print(occupied_goat[ctr-1][0],occupied_goat[ctr-1][1])
                                            for h in range(0, 3):

                                                if or_x == occupied_tiger[h][0] and or_y == occupied_tiger[h][1]:
                                                    flag6 = 1

                                            for j in range(0, gtcnt):
                                                if or_x == occupied_goat[j][0]:
                                                    if or_y == occupied_goat[j][1]:
                                                        flag = 1
                                            if flag == 0:
                                                if flag6 == 0:
                                                    gameDisplay.blit(pw_got2.image, (or_x, or_y))
                                                    occupied_goat[1][0] = or_x
                                                    occupied_goat[1][1] = or_y
                                                    pygame.display.update()
                                                    playsound(
                                                        'Goat-noise.mp3')
                                                    goto2(2)
                                            if flag == 1 or flag6 == 1:
                                                gtcnt = gtcnt - 1

                                        if gtcnt == 2:
                                            # print(occupied_goat[ctr-1][0],occupied_goat[ctr-1][1])
                                            for h in range(0, 3):
                                                if or_x == occupied_tiger[h][0] and or_y == occupied_tiger[h][1]:
                                                    flag6 = 1
                                            for j in range(0, gtcnt):
                                                if or_x == occupied_goat[j][0]:
                                                    if or_y == occupied_goat[j][1]:
                                                        flag = 1
                                            if flag == 0 and flag6 == 0:
                                                gameDisplay.blit(pw_got3.image, (or_x, or_y))
                                                occupied_goat[2][0] = or_x
                                                occupied_goat[2][1] = or_y
                                                pygame.display.update()
                                                playsound('Goat-noise.mp3')
                                                goto2(2)
                                            if flag == 1 or flag6 == 1:
                                                gtcnt = gtcnt - 1
                                        if gtcnt == 3:
                                            # print(occupied_goat[ctr-1][0],occupied_goat[ctr-1][1])
                                            for h in range(0, 3):
                                                if or_x == occupied_tiger[h][0] and or_y == occupied_tiger[h][1]:
                                                    flag6 = 1
                                            for j in range(0, gtcnt):
                                                if or_x == occupied_goat[j][0]:
                                                    if or_y == occupied_goat[j][1]:
                                                        flag = 1
                                            if flag == 0 and flag6 == 0:
                                                gameDisplay.blit(pw_got4.image, (or_x, or_y))
                                                occupied_goat[3][0] = or_x
                                                occupied_goat[3][1] = or_y
                                                pygame.display.update()
                                                playsound('Goat-noise.mp3')
                                                goto2(2)
                                            if flag == 1 or flag6 == 1:
                                                gtcnt = gtcnt - 1
                                        if gtcnt == 4:
                                            # print(occupied_goat[ctr-1][0],occupied_goat[ctr-1][1])
                                            for h in range(0, 3):
                                                if or_x == occupied_tiger[h][0] and or_y == occupied_tiger[h][1]:
                                                    flag6 = 1
                                            for j in range(0, gtcnt):
                                                if or_x == occupied_goat[j][0]:
                                                    if or_y == occupied_goat[j][1]:
                                                        flag = 1
                                            if flag == 0 and flag6 == 0:
                                                gameDisplay.blit(pw_got5.image, (or_x, or_y))
                                                occupied_goat[4][0] = or_x
                                                occupied_goat[4][1] = or_y
                                                pygame.display.update()
                                                playsound('F:\\parthwork\\4th year\\python\\copy 10\\Goat-noise.mp3')
                                                goto2(2)
                                            if flag == 1 or flag6 == 1:
                                                gtcnt = gtcnt - 1
                                        if gtcnt == 5:
                                            # print(occupied_goat[ctr-1][0],occupied_goat[ctr-1][1])
                                            for h in range(0, 3):
                                                if or_x == occupied_tiger[h][0] and or_y == occupied_tiger[h][1]:
                                                    flag6 = 1
                                            for j in range(0, gtcnt):
                                                if or_x == occupied_goat[j][0]:
                                                    if or_y == occupied_goat[j][1]:
                                                        flag = 1
                                            if flag == 0 and flag6 == 0:
                                                gameDisplay.blit(pw_got6.image, (or_x, or_y))
                                                occupied_goat[5][0] = or_x
                                                occupied_goat[5][1] = or_y
                                                pygame.display.update()
                                                playsound('F:\\parthwork\\4th year\\python\\copy 10\\Goat-noise.mp3')
                                                goto2(2)
                                            if flag == 1 or flag6 == 1:
                                                gtcnt = gtcnt - 1
                                        if gtcnt == 6:
                                            # print(occupied_goat[ctr-1][0],occupied_goat[ctr-1][1])
                                            for h in range(0, 3):
                                                if or_x == occupied_tiger[h][0] and or_y == occupied_tiger[h][1]:
                                                    flag6 = 1
                                            for j in range(0, gtcnt):
                                                if or_x == occupied_goat[j][0]:
                                                    if or_y == occupied_goat[j][1]:
                                                        flag = 1
                                            if flag == 0 and flag6 == 0:
                                                gameDisplay.blit(pw_got7.image, (or_x, or_y))
                                                occupied_goat[6][0] = or_x
                                                occupied_goat[6][1] = or_y
                                                pygame.display.update()
                                                playsound('F:\\parthwork\\4th year\\python\\copy 10\\Goat-noise.mp3')
                                                goto2(2)
                                            if flag == 1 or flag6 == 1:
                                                gtcnt = gtcnt - 1
                                        if gtcnt == 7:
                                            # print(occupied_goat[ctr-1][0],occupied_goat[ctr-1][1])
                                            for h in range(0, 3):
                                                if or_x == occupied_tiger[h][0] and or_y == occupied_tiger[h][1]:
                                                    flag6 = 1
                                            for j in range(0, gtcnt):
                                                if or_x == occupied_goat[j][0]:
                                                    if or_y == occupied_goat[j][1]:
                                                        flag = 1
                                            if flag == 0 and flag6 == 0:
                                                gameDisplay.blit(pw_got8.image, (or_x, or_y))
                                                occupied_goat[7][0] = or_x
                                                occupied_goat[7][1] = or_y
                                                pygame.display.update()
                                                playsound('F:\\parthwork\\4th year\\python\\copy 10\\Goat-noise.mp3')
                                                goto2(2)
                                            if flag == 1 or flag6 == 1:
                                                gtcnt = gtcnt - 1
                                        if gtcnt == 8:
                                            # print(occupied_goat[ctr-1][0],occupied_goat[ctr-1][1])
                                            for h in range(0, 3):
                                                if or_x == occupied_tiger[h][0] and or_y == occupied_tiger[h][1]:
                                                    flag6 = 1
                                            for j in range(0, gtcnt):
                                                if or_x == occupied_goat[j][0]:
                                                    if or_y == occupied_goat[j][1]:
                                                        flag = 1
                                            if flag == 0 and flag6 == 0:
                                                gameDisplay.blit(pw_got9.image, (or_x, or_y))
                                                occupied_goat[8][0] = or_x
                                                occupied_goat[8][1] = or_y
                                                pygame.display.update()
                                                playsound('F:\\parthwork\\4th year\\python\\copy 10\\Goat-noise.mp3')
                                                goto2(2)
                                            if flag == 1 or flag6 == 1:
                                                gtcnt = gtcnt - 1
                                        if gtcnt == 9:
                                            # print(occupied_goat[ctr-1][0],occupied_goat[ctr-1][1])
                                            for h in range(0, 3):
                                                if or_x == occupied_tiger[h][0] and or_y == occupied_tiger[h][1]:
                                                    flag6 = 1
                                            for j in range(0, gtcnt):
                                                if or_x == occupied_goat[j][0]:
                                                    if or_y == occupied_goat[j][1]:
                                                        flag = 1
                                            if flag == 0 and flag6 == 0:
                                                gameDisplay.blit(pw_got10.image, (or_x, or_y))
                                                occupied_goat[9][0] = or_x
                                                occupied_goat[9][1] = or_y
                                                pygame.display.update()
                                                playsound('F:\\parthwork\\4th year\\python\\copy 10\\Goat-noise.mp3')
                                                goto2(2)
                                            if flag == 1 or flag6 == 1:
                                                gtcnt = gtcnt - 1
                                        if gtcnt == 10:
                                            # print(occupied_goat[ctr-1][0],occupied_goat[ctr-1][1])
                                            for h in range(0, 3):
                                                if or_x == occupied_tiger[h][0] and or_y == occupied_tiger[h][1]:
                                                    flag6 = 1
                                            for j in range(0, gtcnt):
                                                if or_x == occupied_goat[j][0]:
                                                    if or_y == occupied_goat[j][1]:
                                                        flag = 1
                                            if flag == 0 and flag6 == 0:
                                                gameDisplay.blit(pw_got11.image, (or_x, or_y))
                                                occupied_goat[10][0] = or_x
                                                occupied_goat[10][1] = or_y
                                                pygame.display.update()
                                                playsound('F:\\parthwork\\4th year\\python\\copy 10\\Goat-noise.mp3')
                                                goto2(2)
                                            if flag == 1 or flag6 == 1:
                                                gtcnt = gtcnt - 1
                                        if gtcnt == 11:
                                            # print(occupied_goat[ctr-1][0],occupied_goat[ctr-1][1])
                                            for h in range(0, 3):
                                                if or_x == occupied_tiger[h][0] and or_y == occupied_tiger[h][1]:
                                                    flag6 = 1
                                            for j in range(0, gtcnt):
                                                if or_x == occupied_goat[j][0]:
                                                    if or_y == occupied_goat[j][1]:
                                                        flag = 1
                                            if flag == 0 and flag6 == 0:
                                                gameDisplay.blit(pw_got12.image, (or_x, or_y))
                                                occupied_goat[11][0] = or_x
                                                occupied_goat[11][1] = or_y
                                                pygame.display.update()
                                                playsound('F:\\parthwork\\4th year\\python\\copy 10\\Goat-noise.mp3')
                                                goto2(2)
                                            if flag == 1 or flag6 == 1:
                                                gtcnt = gtcnt - 1
                                        if gtcnt == 12:
                                            # print(occupied_goat[ctr-1][0],occupied_goat[ctr-1][1])
                                            for h in range(0, 3):
                                                if or_x == occupied_tiger[h][0] and or_y == occupied_tiger[h][1]:
                                                    flag6 = 1
                                            for j in range(0, gtcnt):
                                                if or_x == occupied_goat[j][0]:
                                                    if or_y == occupied_goat[j][1]:
                                                        flag = 1
                                            if flag == 0 and flag6 == 0:
                                                gameDisplay.blit(pw_got13.image, (or_x, or_y))
                                                occupied_goat[12][0] = or_x
                                                occupied_goat[12][1] = or_y
                                                pygame.display.update()
                                                playsound('F:\\parthwork\\4th year\\python\\copy 10\\Goat-noise.mp3')
                                                goto2(2)
                                            if flag == 1 or flag6 == 1:
                                                gtcnt = gtcnt - 1
                                        if gtcnt == 13:
                                            # print(occupied_goat[ctr-1][0],occupied_goat[ctr-1][1])
                                            for h in range(0, 3):
                                                if or_x == occupied_tiger[h][0] and or_y == occupied_tiger[h][1]:
                                                    flag6 = 1
                                            for j in range(0, gtcnt):
                                                if or_x == occupied_goat[j][0]:
                                                    if or_y == occupied_goat[j][1]:
                                                        flag = 1
                                            if flag == 0 and flag6 == 0:
                                                gameDisplay.blit(pw_got14.image, (or_x, or_y))
                                                occupied_goat[13][0] = or_x
                                                occupied_goat[13][1] = or_y
                                                pygame.display.update()
                                                playsound('F:\\parthwork\\4th year\\python\\copy 10\\Goat-noise.mp3')
                                                goto2(2)
                                            if flag == 1 or flag6 == 1:
                                                gtcnt = gtcnt - 1
                                        if gtcnt == 14:
                                            # print(occupied_goat[ctr-1][0],occupied_goat[ctr-1][1])
                                            for h in range(0, 3):
                                                if or_x == occupied_tiger[h][0] and or_y == occupied_tiger[h][1]:
                                                    flag6 = 1
                                            for j in range(0, gtcnt):
                                                if or_x == occupied_goat[j][0]:
                                                    if or_y == occupied_goat[j][1]:
                                                        flag = 1
                                            if flag == 0 and flag6 == 0:
                                                gameDisplay.blit(pw_got15.image, (or_x, or_y))
                                                occupied_goat[14][0] = or_x
                                                occupied_goat[14][1] = or_y
                                                pygame.display.update()
                                                playsound('F:\\parthwork\\4th year\\python\\copy 10\\Goat-noise.mp3')
                                                goto2(2)
                                            if flag == 1 or flag6 == 1:
                                                gtcnt = gtcnt - 1

                                        gtcnt = gtcnt + 1

                                        flag6 = 0

        if line2 == 2:
                cnt3 = 1

                x = 0
                y = 0
                flag8 = 0
                flag11 = 0
                line3 = 0
                flag27 = 0
                flag28 = 0
                flag29 = 0
                flag30 = 0
                flag31 = 0
                flag32 = 0
                flag33 = 0
                flag34 = 0
                flag16 = 0
                flag51=0
                flag52 = 0
                flag53 = 0
                flag54 = 0
                flag55 = 0
                flag56 = 0
                if win_tiger < 5:


                    if cnt3 == 1:
                        for h in range(0, 3):
                            tindex = tiger_index[h]
                            for g in range(0, 4):

                                oc_point = tiger_kill[tindex][g][0]
                                or_x4 = orginal_points[oc_point][0]
                                or_y4 = orginal_points[oc_point][1]

                                for v in range(0, 15):
                                    if occupied_goat[v][0] == or_x4 and occupied_goat[v][1] == or_y4:

                                        oc_point2 = tiger_kill[tindex][g][1]
                                        or_x5 = orginal_points[oc_point2][0]
                                        or_y5 = orginal_points[oc_point2][1]
                                        gindex = v
                                        flag11 = 1

                                        break
                                    else:
                                        flag11 = 2

                                if flag11 == 1 and flag21 == 0:
                                    for f in range(0, 15):
                                        if occupied_goat[f][0] == or_x5 and occupied_goat[f][1] == or_y5:
                                            flag8 = 1
                                    for s in range(0, 3):
                                        if occupied_tiger[s][0] == or_x5 and occupied_tiger[s][1] == or_y5:
                                            flag16 = 1

                                    if flag8 == 0 and flag16 == 0:

                                        occupied_tiger[h][0] = or_x5
                                        occupied_tiger[h][1] = or_y5
                                        tiger_index[h] = oc_point2
                                        occupied_goat[gindex][0] = -1000
                                        occupied_goat[gindex][1] = -1000
                                        win_tiger = win_tiger + 1
                                        flag21 = 1
                                        if gtcnt == 0:
                                            gameDisplay.blit(background, (0, 0))
                                            myfont = pygame.font.SysFont("Cosmic Sans", 100)
                                            text = myfont.render("0/15", True, WHITE)

                                            gameDisplay.blit(text, (1200, 350))

                                        if gtcnt == 1:
                                            gameDisplay.blit(background, (0, 0))
                                            myfont = pygame.font.SysFont("Cosmic Sans", 100)
                                            text = myfont.render("1/15", True, WHITE)

                                            gameDisplay.blit(text, (1200, 350))

                                        if gtcnt == 2:
                                            gameDisplay.blit(background, (0, 0))
                                            myfont = pygame.font.SysFont("Cosmic Sans", 100)
                                            text = myfont.render("2/15", True, WHITE)

                                            gameDisplay.blit(text, (1200, 350))

                                        if gtcnt == 3:
                                            gameDisplay.blit(background, (0, 0))
                                            myfont = pygame.font.SysFont("Cosmic Sans", 100)
                                            text = myfont.render("3/15", True, WHITE)

                                            gameDisplay.blit(text, (1200, 350))

                                        if gtcnt == 4:
                                            gameDisplay.blit(background, (0, 0))
                                            myfont = pygame.font.SysFont("Cosmic Sans", 100)
                                            text = myfont.render("4/15", True, WHITE)

                                            gameDisplay.blit(text, (1200, 350))

                                        if gtcnt == 5:
                                            gameDisplay.blit(background, (0, 0))
                                            myfont = pygame.font.SysFont("Cosmic Sans", 100)
                                            text = myfont.render("5/15", True, WHITE)

                                            gameDisplay.blit(text, (1200, 350))

                                        if gtcnt == 6:
                                            gameDisplay.blit(background, (0, 0))
                                            myfont = pygame.font.SysFont("Cosmic Sans", 100)
                                            text = myfont.render("6/15", True, WHITE)

                                            gameDisplay.blit(text, (1200, 350))

                                        if gtcnt == 7:
                                            gameDisplay.blit(background, (0, 0))
                                            myfont = pygame.font.SysFont("Cosmic Sans", 100)
                                            text = myfont.render("7/15", True, WHITE)

                                            gameDisplay.blit(text, (1200, 350))

                                        if gtcnt == 8:
                                            gameDisplay.blit(background, (0, 0))
                                            myfont = pygame.font.SysFont("Cosmic Sans", 100)
                                            text = myfont.render("8/15", True, WHITE)

                                            gameDisplay.blit(text, (1200, 350))

                                        if gtcnt == 9:
                                            gameDisplay.blit(background, (0, 0))
                                            myfont = pygame.font.SysFont("Cosmic Sans", 100)
                                            text = myfont.render("9/15", True, WHITE)

                                            gameDisplay.blit(text, (1200, 350))

                                        if gtcnt == 10:
                                            gameDisplay.blit(background, (0, 0))
                                            myfont = pygame.font.SysFont("Cosmic Sans", 100)
                                            text = myfont.render("10/15", True, WHITE)

                                            gameDisplay.blit(text, (1200, 350))

                                        if gtcnt == 11:
                                            gameDisplay.blit(background, (0, 0))
                                            myfont = pygame.font.SysFont("Cosmic Sans", 100)
                                            text = myfont.render("11/15", True, WHITE)

                                            gameDisplay.blit(text, (1200, 350))

                                        if gtcnt == 12:
                                            gameDisplay.blit(background, (0, 0))
                                            myfont = pygame.font.SysFont("Cosmic Sans", 100)
                                            text = myfont.render("12/15", True, WHITE)

                                            gameDisplay.blit(text, (1200, 350))

                                        if gtcnt == 13:
                                            gameDisplay.blit(background, (0, 0))
                                            myfont = pygame.font.SysFont("Cosmic Sans", 100)
                                            text = myfont.render("13/15", True, WHITE)

                                            gameDisplay.blit(text, (1200, 350))

                                        if gtcnt == 14:
                                            gameDisplay.blit(background, (0, 0))
                                            myfont = pygame.font.SysFont("Cosmic Sans", 100)
                                            text = myfont.render("14/15", True, WHITE)

                                            gameDisplay.blit(text, (1200, 350))

                                        if gtcnt == 15:
                                            gameDisplay.blit(background, (0, 0))
                                            myfont = pygame.font.SysFont("Cosmic Sans", 100)
                                            text = myfont.render("15/15", True, WHITE)

                                            gameDisplay.blit(text, (1200, 350))

                                        if win_tiger == 0:
                                            myfont = pygame.font.SysFont("Cosmic Sans", 100)
                                            text = myfont.render("0/5", True, WHITE)

                                            gameDisplay.blit(text, (1200, 200))

                                        if win_tiger == 1:
                                            myfont = pygame.font.SysFont("Cosmic Sans", 100)
                                            text = myfont.render("1/5", True, WHITE)

                                            gameDisplay.blit(text, (1200, 200))

                                        if win_tiger == 2:
                                            myfont = pygame.font.SysFont("Cosmic Sans", 100)
                                            text = myfont.render("2/5", True, WHITE)

                                            gameDisplay.blit(text, (1200, 200))

                                        if win_tiger == 3:
                                            myfont = pygame.font.SysFont("Cosmic Sans", 100)
                                            text = myfont.render("3/5", True, WHITE)

                                            gameDisplay.blit(text, (1200, 200))

                                        if win_tiger == 4:
                                            myfont = pygame.font.SysFont("Cosmic Sans", 100)
                                            text = myfont.render("4/5", True, WHITE)

                                            gameDisplay.blit(text, (1200, 200))

                                        if win_tiger == 5:
                                            myfont = pygame.font.SysFont("Cosmic Sans", 100)
                                            text = myfont.render("5/5", True, WHITE)

                                            gameDisplay.blit(text, (1200, 200))

                                        gameDisplay.blit(bg, (0, 0))
                                        gameDisplay.blit(pw_got.image, (1100, 350))
                                        gameDisplay.blit(pw_got_kill.image, (1100, 200))
                                        for i in range(0, 15):

                                            if i == 0:
                                                if occupied_goat[i][0] > 0 and occupied_goat[i][1] > 0:
                                                    gameDisplay.blit(pw_got1.image,
                                                                     (occupied_goat[i][0], occupied_goat[i][1]))
                                                # pygame.display.update()
                                                # clock.tick(50000)

                                            if i == 1:
                                                if occupied_goat[i][0] > 0 and occupied_goat[i][1] > 0:
                                                    gameDisplay.blit(pw_got2.image,
                                                                     (occupied_goat[i][0], occupied_goat[i][1]))
                                                # pygame.display.update()
                                                # clock.tick(50000)

                                            if i == 2:
                                                if occupied_goat[i][0] > 0 and occupied_goat[i][1] > 0:
                                                    gameDisplay.blit(pw_got3.image,
                                                                     (occupied_goat[i][0], occupied_goat[i][1]))
                                                # pygame.display.update()
                                                # clock.tick(50000)

                                            if i == 3:
                                                if occupied_goat[i][0] > 0 and occupied_goat[i][1] > 0:
                                                    gameDisplay.blit(pw_got4.image,
                                                                     (occupied_goat[i][0], occupied_goat[i][1]))
                                                # pygame.display.update()
                                                # clock.tick(50000)

                                            if i == 4:
                                                if occupied_goat[i][0] > 0 and occupied_goat[i][1] > 0:
                                                    gameDisplay.blit(pw_got5.image,
                                                                     (occupied_goat[i][0], occupied_goat[i][1]))
                                                # pygame.display.update()
                                                # clock.tick(50000)

                                            if i == 5:
                                                if occupied_goat[i][0] > 0 and occupied_goat[i][1] > 0:
                                                    gameDisplay.blit(pw_got6.image,
                                                                     (occupied_goat[i][0], occupied_goat[i][1]))
                                                # pygame.display.update()
                                                # clock.tick(50000)

                                            if i == 6:
                                                if occupied_goat[i][0] > 0 and occupied_goat[i][1] > 0:
                                                    gameDisplay.blit(pw_got7.image,
                                                                     (occupied_goat[i][0], occupied_goat[i][1]))
                                                # pygame.display.update()
                                                # clock.tick(50000)

                                            if i == 7:
                                                if occupied_goat[i][0] > 0 and occupied_goat[i][1] > 0:
                                                    gameDisplay.blit(pw_got8.image,
                                                                     (occupied_goat[i][0], occupied_goat[i][1]))
                                                # pygame.display.update()
                                                # clock.tick(50000)

                                            if i == 8:
                                                if occupied_goat[i][0] > 0 and occupied_goat[i][1] > 0:
                                                    gameDisplay.blit(pw_got9.image,
                                                                     (occupied_goat[i][0], occupied_goat[i][1]))
                                                # pygame.display.update()
                                                # clock.tick(50000)

                                            if i == 9:
                                                if occupied_goat[i][0] > 0 and occupied_goat[i][1] > 0:
                                                    gameDisplay.blit(pw_got10.image,
                                                                     (occupied_goat[i][0], occupied_goat[i][1]))
                                                # pygame.display.update()
                                                # clock.tick(50000)

                                            if i == 10:
                                                if occupied_goat[i][0] > 0 and occupied_goat[i][1] > 0:
                                                    gameDisplay.blit(pw_got11.image,
                                                                     (occupied_goat[i][0], occupied_goat[i][1]))
                                                # pygame.display.update()
                                                # clock.tick(50000)

                                            if i == 11:
                                                if occupied_goat[i][0] > 0 and occupied_goat[i][1] > 0:
                                                    gameDisplay.blit(pw_got12.image,
                                                                     (occupied_goat[i][0], occupied_goat[i][1]))
                                                # pygame.display.update()
                                                # clock.tick(50000)

                                            if i == 12:
                                                if occupied_goat[i][0] > 0 and occupied_goat[i][1] > 0:
                                                    gameDisplay.blit(pw_got13.image,
                                                                     (occupied_goat[i][0], occupied_goat[i][1]))
                                                # pygame.display.update()
                                                # clock.tick(50000)

                                            if i == 13:
                                                if occupied_goat[i][0] > 0 and occupied_goat[i][1] > 0:
                                                    gameDisplay.blit(pw_got14.image,
                                                                     (occupied_goat[i][0], occupied_goat[i][1]))
                                                # pygame.display.update()
                                                # clock.tick(50000)

                                            if i == 14:
                                                if occupied_goat[i][0] > 0 and occupied_goat[i][1] > 0:
                                                    gameDisplay.blit(pw_got15.image,
                                                                     (occupied_goat[i][0], occupied_goat[i][1]))
                                                # pygame.display.update()
                                                # clock.tick(50000)
                                        for e in range(0, 3):
                                            if e == 0:
                                                gameDisplay.blit(pw_tig1.image,
                                                                 (occupied_tiger[e][0], occupied_tiger[e][1]))
                                            if e == 1:
                                                gameDisplay.blit(pw_tig2.image,
                                                                 (occupied_tiger[e][0], occupied_tiger[e][1]))
                                            if e == 2:
                                                gameDisplay.blit(pw_tig3.image,
                                                                 (occupied_tiger[e][0], occupied_tiger[e][1]))
                                            # clock.tick(50000)
                                        pygame.display.update()
                                        playsound('F:\\parthwork\\4th year\\python\\copy 10\\prey3.mp3')

                                        goto2(1)

                        if flag11 == 2 or flag8 == 1 or flag16 == 1:
                                cnt3 = 2



                    if cnt3 == 2 :
                        flag27 = 0
                        flag28 = 0
                        flag29 = 0
                        flag30 = 0
                        flag31 = 0
                        flag32 = 0
                        flag33 = 0
                        flag34 = 0
                        flag35 = 0
                        flag36 = 0
                        flag37 = 0
                        flag38 = 0
                        flag39 = 0
                        flag40 = 0
                        flag41 = 0
                        flag42 = 0
                        flag43 = 0
                        flag44 = 0
                        flag45 = 0
                        flag46 = 0
                        flag47 = 0
                        flag48 = 0
                        flag49 = 0
                        flag50 = 0
                        tindex4 = tiger_index[0]
                        move_list2 = possible_move[tindex4]

                        or_x7 = orginal_points[move_list2[0]][0]
                        or_y7 = orginal_points[move_list2[0]][1]
                        for n in range(0, 15):
                            if occupied_goat[n][0] == or_x7 and occupied_goat[n][1] == or_y7:
                                flag27 = 1
                        if flag27 != 1:
                            for g in range(0, 3):
                                if occupied_tiger[g][0] == or_x7 and occupied_tiger[g][1] == or_y7:
                                    flag28 = 1
                                    flag27 = 1
                        else:
                            flag28 = 1

                        or_x8 = orginal_points[move_list2[1]][0]
                        or_y8 = orginal_points[move_list2[1]][1]
                        for n1 in range(0, 15):
                            if occupied_goat[n1][0] == or_x8 and occupied_goat[n1][1] == or_y8:
                                flag29 = 1
                        if flag29 != 1:
                            for g1 in range(0, 3):
                                if occupied_tiger[g1][0] == or_x8 and occupied_tiger[g1][1] == or_y8:
                                    flag30 = 1
                                    flag29 = 1
                        else:
                            flag30 = 1

                        if move_list2[2] != -1:
                            or_x9 = orginal_points[move_list2[2]][0]
                            or_y9 = orginal_points[move_list2[2]][1]
                            for n2 in range(0, 15):
                                if occupied_goat[n2][0] == or_x9 and occupied_goat[n2][1] == or_y9:
                                    flag31 = 1
                            if flag31 != 1:
                                for g2 in range(0, 3):
                                    if occupied_tiger[g2][0] == or_x9 and occupied_tiger[g2][1] == or_y9:
                                        flag32 = 1
                                        flag31 = 1
                            else:
                                flag32 = 1
                        else:
                            flag31 = 1
                            flag32 = 1
                        if move_list2[3] != -1:
                            or_x10 = orginal_points[move_list2[3]][0]
                            or_y10 = orginal_points[move_list2[3]][1]
                            for n3 in range(0, 15):
                                if occupied_goat[n3][0] == or_x10 and occupied_goat[n3][1] == or_y10:
                                    flag33 = 1
                            if flag33 != 1:
                                for g4 in range(0, 3):
                                    if occupied_tiger[g4][0] == or_x10 and occupied_tiger[g4][1] == or_y10:
                                        flag34 = 1
                                        flag33 = 1
                            else:
                                flag34 = 1
                        else:
                            flag33 = 1
                            flag34 = 1
                        tindex5 = tiger_index[1]
                        move_list3 = possible_move[tindex5]

                        or_x11 = orginal_points[move_list3[0]][0]
                        or_y11 = orginal_points[move_list3[0]][1]
                        for n5 in range(0, 15):
                            if occupied_goat[n5][0] == or_x11 and occupied_goat[n5][1] == or_y11:
                                flag35 = 1
                        if flag35 != 1:
                            for g5 in range(0, 3):
                                if occupied_tiger[g5][0] == or_x11 and occupied_tiger[g5][1] == or_y11:
                                    flag36 = 1
                                    flag35 = 1
                        else:
                            flag36 = 1

                        or_x12 = orginal_points[move_list3[1]][0]
                        or_y12 = orginal_points[move_list3[1]][1]
                        for n6 in range(0, 15):
                            if occupied_goat[n6][0] == or_x12 and occupied_goat[n6][1] == or_y12:
                                flag37 = 1
                        if flag37 != 1:
                            for g6 in range(0, 3):
                                if occupied_tiger[g6][0] == or_x12 and occupied_tiger[g6][1] == or_y12:
                                    flag38 = 1
                                    flag37 = 1
                        else:
                            flag38 = 1
                        if move_list3[2] != -1:
                            or_x13 = orginal_points[move_list3[2]][0]
                            or_y13 = orginal_points[move_list3[2]][1]
                            for n7 in range(0, 15):
                                if occupied_goat[n7][0] == or_x13 and occupied_goat[n7][1] == or_y13:
                                    flag39 = 1
                            if flag39 != 1:
                                for g7 in range(0, 3):
                                    if occupied_tiger[g7][0] == or_x13 and occupied_tiger[g7][1] == or_y13:
                                        flag40 = 1
                                        flag39 = 1
                            else:
                                flag40 = 1
                        else:
                            flag39 = 1
                            flag40 = 1
                        if move_list3[3] != 1:
                            or_x14 = orginal_points[move_list3[3]][0]
                            or_y14 = orginal_points[move_list3[3]][1]
                            for n8 in range(0, 15):
                                if occupied_goat[n8][0] == or_x14 and occupied_goat[n8][1] == or_y14:
                                    flag41 = 1
                            if flag41 != 1:
                                for g8 in range(0, 3):
                                    if occupied_tiger[g8][0] == or_x14 and occupied_tiger[g8][1] == or_y14:
                                        flag42 = 1
                                        flag41 = 1
                            else:
                                flag42 = 1
                        else:
                            flag41 = 1
                            flag42 = 1
                        tindex6 = tiger_index[2]
                        move_list4 = possible_move[tindex6]

                        or_x15 = orginal_points[move_list4[0]][0]
                        or_y15 = orginal_points[move_list4[0]][1]
                        for n9 in range(0, 15):
                            if occupied_goat[n9][0] == or_x15 and occupied_goat[n9][1] == or_y15:
                                flag43 = 1
                        if flag43 != 1:
                            for g9 in range(0, 3):
                                if occupied_tiger[g9][0] == or_x15 and occupied_tiger[g9][1] == or_y15:
                                    flag44 = 1
                                    flag43 = 1
                        else:
                            flag44 = 1

                        or_x16 = orginal_points[move_list4[1]][0]
                        or_y16 = orginal_points[move_list4[1]][1]
                        for n10 in range(0, 15):
                            if occupied_goat[n10][0] == or_x16 and occupied_goat[n10][1] == or_y16:
                                flag45 = 1
                        if flag45 != 1:
                            for g10 in range(0, 3):
                                if occupied_tiger[g10][0] == or_x16 and occupied_tiger[g10][1] == or_y16:
                                    flag46 = 1
                                    flag45 = 1
                        else:
                            flag46 = 1
                        if move_list4[2] != -1:
                            or_x17 = orginal_points[move_list4[2]][0]
                            or_y17 = orginal_points[move_list4[2]][1]
                            for n11 in range(0, 15):
                                if occupied_goat[n11][0] == or_x17 and occupied_goat[n11][1] == or_y17:
                                    flag47 = 1
                            if flag47 != 1:
                                for g11 in range(0, 3):
                                    if occupied_tiger[g11][0] == or_x17 and occupied_tiger[g11][1] == or_y17:
                                        flag48 = 1
                                        flag47 = 1
                            else:
                                flag48 = 1
                        else:
                            flag47 = 1
                            flag48 = 1
                        if move_list4[3] != -1:
                            or_x18 = orginal_points[move_list4[3]][0]
                            or_y18 = orginal_points[move_list4[3]][1]
                            for n12 in range(0, 15):
                                if occupied_goat[n12][0] == or_x18 and occupied_goat[n12][1] == or_y18:
                                    flag49 = 1
                            if flag49 != 1:
                                for g12 in range(0, 3):
                                    if occupied_tiger[g12][0] == or_x18 and occupied_tiger[g12][1] == or_y18:
                                        flag50 = 1
                                        flag49 = 1
                            else:
                                flag50 = 1
                        else:
                            flag49 = 1
                            flag50 = 1


                    else:
                        goto2(1)
                    if flag27 == 1 and flag28 == 1 and flag29 == 1 and flag30 == 1 and flag31 == 1 and flag32 == 1 and flag33 == 1 and flag34 == 1 and flag35 == 1 and flag36 == 1 and flag37 == 1 and flag38 == 1 and flag39 == 1 and flag40 == 1and flag41 == 1 and flag42 == 1 and flag43 == 1 and flag44 == 1 and flag45 == 1 and flag46 == 1 and flag47 == 1 and flag48 == 1 and flag49 == 1 and flag50 == 1  :
                        goto5(4)


                    else:
                        if flag21 == 0:
                            line3 = 1

                            if line3 == 1 :

                                flag22 = 0
                                flag23 = 0
                                flag24 = 0
                                cnt5 = 0
                                random.shuffle(slist)
                                tindex3 = slist[0]
                                tindex2 = tiger_index[tindex3]
                                move_list = possible_move[tindex2]
                                goto3(2)
                                if line3 == 2:


                                        random.shuffle(move_list)

                                        move = move_list[0]
                                        if move == -1:
                                            goto3(2)
                                        else:
                                            or_x6 = orginal_points[move][0]
                                            or_y6 = orginal_points[move][1]
                                            for b in range(0, 15):
                                                if occupied_goat[b][0] == or_x6 and occupied_goat[b][1] == or_y6:
                                                    flag22 = 1
                                            for z in range(0, 3):
                                                if occupied_tiger[z][0] == or_x6 and occupied_tiger[z][1] == or_y6:
                                                    flag23 = 1
                                            if flag22 == 0 and flag23 == 0:
                                                occupied_tiger[tindex3][0] = or_x6
                                                occupied_tiger[tindex3][1] = or_y6
                                                tiger_index[tindex3] = move
                                                flag24 = 1

                                                if gtcnt == 0:
                                                    gameDisplay.blit(background, (0, 0))
                                                    myfont = pygame.font.SysFont("Cosmic Sans", 100)
                                                    text = myfont.render("0/15", True, WHITE)

                                                    gameDisplay.blit(text, (1200, 350))

                                                if gtcnt == 1:
                                                    gameDisplay.blit(background, (0, 0))
                                                    myfont = pygame.font.SysFont("Cosmic Sans", 100)
                                                    text = myfont.render("1/15", True, WHITE)

                                                    gameDisplay.blit(text, (1200, 350))

                                                if gtcnt == 2:
                                                    gameDisplay.blit(background, (0, 0))
                                                    myfont = pygame.font.SysFont("Cosmic Sans", 100)
                                                    text = myfont.render("2/15", True, WHITE)

                                                    gameDisplay.blit(text, (1200, 350))

                                                if gtcnt == 3:
                                                    gameDisplay.blit(background, (0, 0))
                                                    myfont = pygame.font.SysFont("Cosmic Sans", 100)
                                                    text = myfont.render("3/15", True, WHITE)

                                                    gameDisplay.blit(text, (1200, 350))

                                                if gtcnt == 4:
                                                    gameDisplay.blit(background, (0, 0))
                                                    myfont = pygame.font.SysFont("Cosmic Sans", 100)
                                                    text = myfont.render("4/15", True, WHITE)

                                                    gameDisplay.blit(text, (1200, 350))

                                                if gtcnt == 5:
                                                    gameDisplay.blit(background, (0, 0))
                                                    myfont = pygame.font.SysFont("Cosmic Sans", 100)
                                                    text = myfont.render("5/15", True, WHITE)

                                                    gameDisplay.blit(text, (1200, 350))

                                                if gtcnt == 6:
                                                    gameDisplay.blit(background, (0, 0))
                                                    myfont = pygame.font.SysFont("Cosmic Sans", 100)
                                                    text = myfont.render("6/15", True, WHITE)

                                                    gameDisplay.blit(text, (1200, 350))

                                                if gtcnt == 7:
                                                    gameDisplay.blit(background, (0, 0))
                                                    myfont = pygame.font.SysFont("Cosmic Sans", 100)
                                                    text = myfont.render("7/15", True, WHITE)

                                                    gameDisplay.blit(text, (1200, 350))

                                                if gtcnt == 8:
                                                    gameDisplay.blit(background, (0, 0))
                                                    myfont = pygame.font.SysFont("Cosmic Sans", 100)
                                                    text = myfont.render("8/15", True, WHITE)

                                                    gameDisplay.blit(text, (1200, 350))

                                                if gtcnt == 9:
                                                    gameDisplay.blit(background, (0, 0))
                                                    myfont = pygame.font.SysFont("Cosmic Sans", 100)
                                                    text = myfont.render("9/15", True, WHITE)

                                                    gameDisplay.blit(text, (1200, 350))

                                                if gtcnt == 10:
                                                    gameDisplay.blit(background, (0, 0))
                                                    myfont = pygame.font.SysFont("Cosmic Sans", 100)
                                                    text = myfont.render("10/15", True, WHITE)

                                                    gameDisplay.blit(text, (1200, 350))

                                                if gtcnt == 11:
                                                    gameDisplay.blit(background, (0, 0))
                                                    myfont = pygame.font.SysFont("Cosmic Sans", 100)
                                                    text = myfont.render("11/15", True, WHITE)

                                                    gameDisplay.blit(text, (1200, 350))

                                                if gtcnt == 12:
                                                    gameDisplay.blit(background, (0, 0))
                                                    myfont = pygame.font.SysFont("Cosmic Sans", 100)
                                                    text = myfont.render("12/15", True, WHITE)

                                                    gameDisplay.blit(text, (1200, 350))

                                                if gtcnt == 13:
                                                    gameDisplay.blit(background, (0, 0))
                                                    myfont = pygame.font.SysFont("Cosmic Sans", 100)
                                                    text = myfont.render("13/15", True, WHITE)

                                                    gameDisplay.blit(text, (1200, 350))

                                                if gtcnt == 14:
                                                    gameDisplay.blit(background, (0, 0))
                                                    myfont = pygame.font.SysFont("Cosmic Sans", 100)
                                                    text = myfont.render("14/15", True, WHITE)

                                                    gameDisplay.blit(text, (1200, 350))

                                                if gtcnt == 15:
                                                    gameDisplay.blit(background, (0, 0))
                                                    myfont = pygame.font.SysFont("Cosmic Sans", 100)
                                                    text = myfont.render("15/15", True, WHITE)

                                                    gameDisplay.blit(text, (1200, 350))

                                                if win_tiger == 0:
                                                    myfont = pygame.font.SysFont("Cosmic Sans", 100)
                                                    text = myfont.render("0/5", True, WHITE)

                                                    gameDisplay.blit(text, (1200, 200))

                                                if win_tiger == 1:
                                                    myfont = pygame.font.SysFont("Cosmic Sans", 100)
                                                    text = myfont.render("1/5", True, WHITE)

                                                    gameDisplay.blit(text, (1200, 200))

                                                if win_tiger == 2:
                                                    myfont = pygame.font.SysFont("Cosmic Sans", 100)
                                                    text = myfont.render("2/5", True, WHITE)

                                                    gameDisplay.blit(text, (1200, 200))

                                                if win_tiger == 3:
                                                    myfont = pygame.font.SysFont("Cosmic Sans", 100)
                                                    text = myfont.render("3/5", True, WHITE)

                                                    gameDisplay.blit(text, (1200, 200))

                                                if win_tiger == 4:
                                                    myfont = pygame.font.SysFont("Cosmic Sans", 100)
                                                    text = myfont.render("4/5", True, WHITE)

                                                    gameDisplay.blit(text, (1200, 200))

                                                if win_tiger == 5:
                                                    myfont = pygame.font.SysFont("Cosmic Sans", 100)
                                                    text = myfont.render("5/5", True, WHITE)

                                                    gameDisplay.blit(text, (1200, 200))

                                                gameDisplay.blit(bg, (0, 0))
                                                gameDisplay.blit(pw_got.image, (1100, 350))
                                                gameDisplay.blit(pw_got_kill.image, (1100, 200))
                                                for i in range(0, 15):

                                                    if i == 0:
                                                        if occupied_goat[i][0] > 0 and occupied_goat[i][1] > 0:
                                                            gameDisplay.blit(pw_got1.image,
                                                                             (occupied_goat[i][0], occupied_goat[i][1]))
                                                        # pygame.display.update()
                                                        # clock.tick(50000)

                                                    if i == 1:
                                                        if occupied_goat[i][0] > 0 and occupied_goat[i][1] > 0:
                                                            gameDisplay.blit(pw_got2.image,
                                                                             (occupied_goat[i][0], occupied_goat[i][1]))
                                                        # pygame.display.update()
                                                        # clock.tick(50000)

                                                    if i == 2:
                                                        if occupied_goat[i][0] > 0 and occupied_goat[i][1] > 0:
                                                            gameDisplay.blit(pw_got3.image,
                                                                             (occupied_goat[i][0], occupied_goat[i][1]))
                                                        # pygame.display.update()
                                                        # clock.tick(50000)

                                                    if i == 3:
                                                        if occupied_goat[i][0] > 0 and occupied_goat[i][1] > 0:
                                                            gameDisplay.blit(pw_got4.image,
                                                                             (occupied_goat[i][0], occupied_goat[i][1]))
                                                        # pygame.display.update()
                                                        # clock.tick(50000)

                                                    if i == 4:
                                                        if occupied_goat[i][0] > 0 and occupied_goat[i][1] > 0:
                                                            gameDisplay.blit(pw_got5.image,
                                                                             (occupied_goat[i][0], occupied_goat[i][1]))
                                                        # pygame.display.update()
                                                        # clock.tick(50000)

                                                    if i == 5:
                                                        if occupied_goat[i][0] > 0 and occupied_goat[i][1] > 0:
                                                            gameDisplay.blit(pw_got6.image,
                                                                             (occupied_goat[i][0], occupied_goat[i][1]))
                                                        # pygame.display.update()
                                                        # clock.tick(50000)

                                                    if i == 6:
                                                        if occupied_goat[i][0] > 0 and occupied_goat[i][1] > 0:
                                                            gameDisplay.blit(pw_got7.image,
                                                                             (occupied_goat[i][0], occupied_goat[i][1]))
                                                        # pygame.display.update()
                                                        # clock.tick(50000)

                                                    if i == 7:
                                                        if occupied_goat[i][0] > 0 and occupied_goat[i][1] > 0:
                                                            gameDisplay.blit(pw_got8.image,
                                                                             (occupied_goat[i][0], occupied_goat[i][1]))
                                                        # pygame.display.update()
                                                        # clock.tick(50000)

                                                    if i == 8:
                                                        if occupied_goat[i][0] > 0 and occupied_goat[i][1] > 0:
                                                            gameDisplay.blit(pw_got9.image,
                                                                             (occupied_goat[i][0], occupied_goat[i][1]))
                                                        # pygame.display.update()
                                                        # clock.tick(50000)

                                                    if i == 9:
                                                        if occupied_goat[i][0] > 0 and occupied_goat[i][1] > 0:
                                                            gameDisplay.blit(pw_got10.image,
                                                                             (occupied_goat[i][0], occupied_goat[i][1]))
                                                        # pygame.display.update()
                                                        # clock.tick(50000)

                                                    if i == 10:
                                                        if occupied_goat[i][0] > 0 and occupied_goat[i][1] > 0:
                                                            gameDisplay.blit(pw_got11.image,
                                                                             (occupied_goat[i][0], occupied_goat[i][1]))
                                                        # pygame.display.update()
                                                        # clock.tick(50000)

                                                    if i == 11:
                                                        if occupied_goat[i][0] > 0 and occupied_goat[i][1] > 0:
                                                            gameDisplay.blit(pw_got12.image,
                                                                             (occupied_goat[i][0], occupied_goat[i][1]))
                                                        # pygame.display.update()
                                                        # clock.tick(50000)

                                                    if i == 12:
                                                        if occupied_goat[i][0] > 0 and occupied_goat[i][1] > 0:
                                                            gameDisplay.blit(pw_got13.image,
                                                                             (occupied_goat[i][0], occupied_goat[i][1]))
                                                        # pygame.display.update()
                                                        # clock.tick(50000)

                                                    if i == 13:
                                                        if occupied_goat[i][0] > 0 and occupied_goat[i][1] > 0:
                                                            gameDisplay.blit(pw_got14.image,
                                                                             (occupied_goat[i][0], occupied_goat[i][1]))
                                                        # pygame.display.update()
                                                        # clock.tick(50000)

                                                    if i == 14:
                                                        if occupied_goat[i][0] > 0 and occupied_goat[i][1] > 0:
                                                            gameDisplay.blit(pw_got15.image,
                                                                             (occupied_goat[i][0], occupied_goat[i][1]))
                                                        # pygame.display.update()
                                                        # clock.tick(50000)
                                                for e in range(0, 3):
                                                    if e == 0:
                                                        gameDisplay.blit(pw_tig1.image,
                                                                         (occupied_tiger[e][0], occupied_tiger[e][1]))
                                                    if e == 1:
                                                        gameDisplay.blit(pw_tig2.image,
                                                                         (occupied_tiger[e][0], occupied_tiger[e][1]))
                                                    if e == 2:
                                                        gameDisplay.blit(pw_tig3.image,
                                                                         (occupied_tiger[e][0], occupied_tiger[e][1]))
                                                    # clock.tick(50000)
                                                pygame.display.update()
                                                playsound('F:\\parthwork\\4th year\\python\\copy 10\\tiger-roar4.mp3')
                                                goto2(1)
                                            if flag22 == 1 or flag23 == 1:
                                                cnt5 += 1

                                        if cnt5 < 4 and flag24 == 0:
                                            goto3(2)
                                        if cnt5 == 4:
                                            goto3(1)

                if win_tiger == 5:
                    goto5(5)
    if line5 == 4:
        gameDisplay.blit(gwin, (0, 0))
        pygame.display.update()
        for event3 in pygame.event.get():
            if event3.type == pygame.MOUSEBUTTONDOWN:
                cor_x5, cor_y5 = pygame.mouse.get_pos()
                if cor_x5 >= 467 and cor_x5 <= 875:
                    if cor_y5 >= 278 and cor_y5 <= 354:
                        goto5(2)

                if cor_x5 >= 481 and cor_x5 <= 445:
                    if cor_y5 >= 861 and cor_y5 <= 521:
                        pygame.quit()
                        quit()


            if event3.type == pygame.QUIT:
                gameExit = True

    if line5 == 5:
        gameDisplay.blit(twin, (0, 0))
        pygame.display.update()
        for event4 in pygame.event.get():
            if event4.type == pygame.MOUSEBUTTONDOWN:
                cor_x6, cor_y6 = pygame.mouse.get_pos()

                if cor_x6 >= 467 and cor_x6 <= 875:
                    if cor_y6 >= 278 and cor_y6 <= 354:
                        goto5(2)
                if cor_x6 >= 481 and cor_x6 <= 445:
                    if cor_y6 >= 861 and cor_y6 <= 521:
                        print("hii")
                        pygame.quit()
                        quit()

            if event4.type == pygame.QUIT:
                gameExit = True

pygame.quit()
quit()
