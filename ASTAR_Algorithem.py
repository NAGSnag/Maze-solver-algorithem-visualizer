import random
import math
import pygame

w=800
fps=60

win=pygame.display.set_mode((w,w))
clock=pygame.time.Clock()

black=(0,0,0)
blue=(0,0,255)
orange=(255,165,0)
white=(255,255,255)
purple=(160,32,240)
green=(124,252,0)
yellow=(255,255,0)
grey=(198,226,255)
mway=[]

openlist = []
closelist = []
flag=False
class box():
    def __init__(self,x,y,value=0):
        self.boxx=x
        self.boxy=y
        self.value=value
        self.h=(0,0)
    def draw(self):
        if self.value==0:
            pygame.draw.rect(win,white,pygame.Rect(self.boxx,self.boxy,8,8))
            self.boxcolor = 'w'
        if self.value==1:
            pygame.draw.rect(win, black, pygame.Rect(self.boxx, self.boxy, 8, 8))
            self.boxcolor = 'bl'
        if self.value=='a':
            pygame.draw.rect(win, blue, pygame.Rect(self.boxx, self.boxy, 8, 8))
            self.boxcolor = 'bl'
        if self.value=='b':
            pygame.draw.rect(win, orange, pygame.Rect(self.boxx, self.boxy, 8, 8))
            self.boxcolor = 'or'
        if self.value==2:
            pygame.draw.rect(win, green, pygame.Rect(self.boxx, self.boxy, 8, 8))
            self.boxcolor = 'g'
        if self.value==3:
            pygame.draw.rect(win, purple, pygame.Rect(self.boxx, self.boxy, 8, 8))
            self.boxcolor = 'p'
        if self.value==4:
            pygame.draw.rect(win, yellow, pygame.Rect(self.boxx, self.boxy, 8, 8))
            self.boxcolor = 'y'
        if self.value == 5:
            pygame.draw.rect(win, grey, pygame.Rect(self.boxx, self.boxy, 8, 8))
            self.boxcolor = 'y'

    def getcolor(self):
        return self.boxcolor
    def changevalue(self,value):
        self.value=value
    def changecolor(self,color):
        if color=='w':self.value=0
        if color=='b':self.value=1
        if color=='g':self.value=2
        if color=='p':self.value=3
        if color=='y':self.value=4
    def getvalue(self):
        return self.value

map=[]

for i in range(80):
    llobj = []
    for j in range(80):
        a = box( i * 10, j * 10)
        llobj.append(a)
    map.append(llobj)
    del llobj
for i in range(80):
    map[0][i].changecolor('b')
    map[79][i].changecolor('b')
for i in range(80):
    map[i][0].changecolor('b')
    map[i][79].changecolor('b')


def getclickpos(pos,row,width):
    gap=width//row
    y,x=pos

    row=y//gap
    col=x//gap
    return row,col
def checkb():
    e=False
    for i in map:
        for j in i:
            if j.getvalue()=='b':
                e=True
                break
    return e
def checka():
    e=False
    for i in map:
        for j in i:
            if j.getvalue()=='a':
                e=True
                break
    return e
def getapos():
    for i in range(80):
        for j in range(80):
            if map[i][j].getvalue()=='a':
                return int(i),int(j)
def getbpos():
    for i in range(80):
        for j in range(80):
            if map[i][j].getvalue()=='b':
                return i,j




def ypath():
    ypathl=[]
    ppathl=[]

    for i in range(2,78):
        for j in range(2,78):
            if map[i][j].getvalue()==3:
                ppathl.append((i,j))
            if map[i][j].getvalue()==4:
                ypathl.append((i,j))
    for i in range(2,78):
        for j in range(2,78):
            if map[i][j].getvalue()==3:
                if map[i][j-1].getvalue()==4:
                    b=ppathl.index((i,j-2))
                    a=ppathl.index((i,j))
                    for i in range(a,b):
                        ppathl.pop(i)
                    ppathl.append((i,j))
                    ppathl.append((i,j-2))
                    ppathl.append((i,j-1))





    return ypathl


def gen(item):
    mcur =item
    global mway
    map[item[0]][item[1]].changevalue(0)
    mpways = [(mcur[0], mcur[1] + 1), (mcur[0], mcur[1] - 1), (mcur[0] + 1, mcur[1]), (mcur[0] - 1, mcur[1])]
    random.shuffle(mpways)


    try:
        for item in mpways:
            try:
                # if item in mway:
                #     continue
                if item[0] >= 78 and item[0] <= 1 and item[1] >= 78 and item[1] <= 1:
                    item = (item[0], item[1] + 1)
                elif map[item[0]][item[1]].getvalue() == 0:
                    continue
                elif map[item[0] + 1][item[1]].getvalue() == 0:
                    continue
                elif map[item[0]][item[1] + 1].getvalue() == 0:
                    continue
                elif item[0] <= 77 and item[0] >= 1 and item[1] <= 77 and item[1] >= 1:
                    # map[mcur[0] + item[0] // 2][mcur[1] + item[1] // 2m].changevalue(0)
                    mway.append(item)


                gen(mway.pop())
                # if len(mway) == 0:
                #     return


            except Exception as e:

                print(e)

    except Exception as e:
        print(e)


def h():
    destx,desty=getbpos()
    for i in range(80):
        for j in range(80):
            map[i][j].h=math.sqrt((i-destx)**2+(j-desty)**2)#calculate dist btw current and destination pos
    global white
    white=(224,224,224)




def algo():
    global openlist,closelist,flag
    openlist = sorted(openlist, key=lambda i:map[i[0]][i[1]].h )
    node=openlist.pop(0)
    closelist.append(node)
    surround=[(node[0]+1,node[1]),(node[0]-1,node[1]),(node[0],node[1]+1),(node[0],node[1]-1),(node[0]+1,node[1]+1),(node[0]-1,node[1]-1),(node[0]-1,node[1]+1),(node[0]+1,node[1]-1)]
    corners=[(node[0]+1,node[1]+1),(node[0]-1,node[1]-1),(node[0]-1,node[1]+1),(node[0]+1,node[1]-1)]
    for i in surround:
        if map[i[0]][i[1]].value == 'b' or map[i[0]][i[1]].h==0:
            for i in closelist:
                map[i[0]][i[1]].value = 3
                flag = False
        if map[i[0]][i[1]].value==0:
            if i in corners:
                if i==(node[0]+1,node[1]+1):
                    if map[i[0] + 1][i[1]].value == 1 and map[i[0]][i[1] + 1].value == 1:
                        continue
                if i==(node[0]-1,node[1]-1):
                    if map[i[0]-1][i[1]].value==1 and map[i[0]][i[1]-1].value==1:
                        continue
                if i==(node[0]-1,node[1]+1):
                    if map[i[0]-1][i[1]].value==1 and map[i[0]][i[1]+1].value==1 :
                        continue
                if i==(node[0]+1,node[1]-1):
                    if map[i[0]+1][i[1]].value==1 and map[i[0]][i[1]-1].value==1:
                        continue
            # if map[i[0]+1][i[1]].value==1 and map[i[0]][i[1]+1].value==1 or map[i[0]+1][i[1]].value==1 and map[i[0]][i[1]-1].value==1 or map[i[0]-1][i[1]].value==1 and map[i[0]][i[1]+1].value==1 or map[i[0]-1][i[1]].value==1 and map[i[0]][i[1]-1].value==1:
            #     pass
            else:
                if i in openlist or i in closelist:pass
                else:
                    openlist.append(i)
                    map[i[0]][i[1]].value=2



#########################################################################################################################
#########################################################################################################################
def main():
    global clock
    run=True
    path =[]
    mflag=False
    global flag
    while run:
        clock.tick(fps)
        pygame.display.set_caption(f'FPS:{int(clock.get_fps())}   pathfindergui')
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
        left, middle, right = pygame.mouse.get_pressed()
        if left:
            try:
                pos = pygame.mouse.get_pos()
                col,row = getclickpos(pos, 80, 800)
                #print(col,row)
                if checka() !=True:
                    map[col][row].changevalue('a')

                elif checkb() !=True:
                    map[col][row].changevalue('b')

                else:
                    if map[col][row].getcolor()=='bl':
                        continue
                    if map[col][row].getcolor()=='or':
                         continue
                    map[col][row].changevalue(1)
            except Exception:pass

        if right:
            pos = pygame.mouse.get_pos()
            col,row=getclickpos(pos,80,800)
            map[col][row].changevalue(0)
            print(map[col][row].h)

###########################################################################################################
        keypressed = pygame.key.get_pressed()

        if keypressed[pygame.K_r]:
            for i in range(1,79):
                for j in range(2,79,2):
                    map[i][j].changevalue(1)
                    choice = random.choice(list(range(2,79,2)))
                    map[j][choice].changevalue(0)

        if keypressed[pygame.K_h]:
            h()

        if keypressed[pygame.K_m]:
            mx, my = 1, 1
            #mpath.append((mx, my))
            for i in map:
                for j in i:
                    j.changevalue(1)
            mflag = True

        if mflag:
            gen((mx,my))
            gen((30,3))
            for i in range(2,79):
                for j in range(30):
                    ch=random.choice(list(range(2,79)))
                    map[i][ch].changevalue(0)
            mflag=False


        if keypressed[pygame.K_SPACE]:      #############################
            h()
            x, y = getapos()
            path.append((x,y))
            openlist.append((getapos()))
            flag=True
        try:
            if flag:
                algo()
        except Exception as e :pass


###########################################################################################################
#display
        for i in map:
            for j in i:
                j.draw()
        pygame.display.update()
    pygame.quit()

if __name__=='__main__':
    main()




