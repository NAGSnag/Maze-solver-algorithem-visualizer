import pickle
import random
import time
import pygame
w=800
fps=60
clock=pygame.time.Clock()
win=pygame.display.set_mode((w,w))
pygame.display.set_caption('pathfindergui')
black=(0,0,0)
blue=(0,0,255)
orange=(255,165,0)
white=(255,255,255)
purple=(160,32,240)
green=(124,252,0)
yellow=(255,255,0)
mway=[]

class box():
    def __init__(self,x,y,id,pos,value=0):
        self.boxx=x
        self.boxy=y
        self.value=value
        self.pos=pos
        self.id=id
        self.visit=False
        self.dictaddress={}
        self.neighbours={self.pos}
    def draw(self):
        if self.value==0:
            pygame.draw.rect(win,white,pygame.Rect(self.boxx,self.boxy,8,8))
            self.boxcolor = 'w'
        elif self.value==1:
            pygame.draw.rect(win, black, pygame.Rect(self.boxx, self.boxy, 8, 8))
            self.boxcolor = 'bl'
        elif self.value=='a':
            pygame.draw.rect(win, blue, pygame.Rect(self.boxx, self.boxy, 8, 8))
            self.boxcolor = 'bl'
        elif self.value=='b':
            pygame.draw.rect(win, orange, pygame.Rect(self.boxx, self.boxy, 8, 8))
            self.boxcolor = 'or'
        elif self.value==2:
            pygame.draw.rect(win, green, pygame.Rect(self.boxx, self.boxy, 8, 8))
            self.boxcolor = 'g'
        elif self.value==3:
            pygame.draw.rect(win, purple, pygame.Rect(self.boxx, self.boxy, 8, 8))
            self.boxcolor = 'p'
        elif self.value==4:
            pygame.draw.rect(win, yellow, pygame.Rect(self.boxx, self.boxy, 8, 8))
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
countn=0
for i in range(80):
    llobj = []
    for j in range(80):
        countn += 1
        a = box( i * 10, j * 10,str('A'+str(countn)),(i,j))
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

def getbpos():
    for i in range(80):
        for j in range(80):
            if map[i][j].getvalue()=='b':
                return map[i][j].pos

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
def penitrate(dic,apos):
    print(dic)
    for n in dic:
        a = dic[n]
        a = a[0]
        print(a)
    map[a[0]][a[1]].value = 3
    while map[a[0]][a[1]].value != 'a' and map[a[0]][a[1]].dictaddress:
        dic = map[a[0]][a[1]].dictaddress
        for n in dic:
            a = dic[n]
            a = a[0]
            map[a[0]][a[1]].value = 3
    map[apos[0]][apos[1]].value = 'a'




def main():
    global a,clock
    run=True
    mflag=False
    flag=False
    queue = []
    record=[]
    while run:
        clock.tick()
        pygame.display.set_caption(f'FPS:{int(clock.get_fps())}   DijitsraPathFinderGui')
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
        left, middle, right = pygame.mouse.get_pressed()
        if left:
            pos = pygame.mouse.get_pos()
            col,row = getclickpos(pos, 80, 800)
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

        if right:
            pos = pygame.mouse.get_pos()
            col,row=getclickpos(pos,80,800)
            map[col][row].changevalue(0)
        keypressed = pygame.key.get_pressed()
        if keypressed[pygame.K_m]:
            mx, my = 1, 1
            #mpath.append((mx, my))
            for i in map:
                for j in i:
                    j.changevalue(1)
            mflag = True
        if keypressed[pygame.K_r]:
            for i in range(1,79):
                for j in range(2,79,2):
                    map[i][j].changevalue(1)
                    choice = random.choice(list(range(2,79,2)))
                    map[j][choice].changevalue(0)
        if mflag:
            gen((mx,my))
            gen((30,3))
            for i in range(2,79):
                for j in range(30):
                    ch=random.choice(list(range(2,79)))
                    map[i][ch].changevalue(0)
            mflag=False
        ##################main################################ if runned
        if keypressed[pygame.K_SPACE]:
            # getneb()
            for i in map:
                for j in i:
                    if j.getvalue() == 'a':
                        queue.append(j.pos)
                        # list1.append(j.pos)
                        a = j.pos
                        apos=j.pos
                        aid = j.id
                        flag = True
                        break
    ########################################################################################################################## just change for all direction
        try:
            if flag == True:
                i,j=queue.pop(0)
                if (i,j) in queue:
                    pass

                else:
                    if map[i-1][j].getvalue()==0 or map[i-1][j].getvalue()=='b':
                        queue.append(tuple((i-1,j)))
                        record.append(tuple((i-1,j)))
                        map[i-1][j].dictaddress.update({(i-1,j):[(i,j)]})
                    map[i][j].value=2
                    if map[i - 1][j].value == 'b':
                        flag=False
                        penitrate(map[i-1][j].dictaddress,apos)
    #############
                    if map[i + 1][j].getvalue() == 0 or map[i + 1][j].getvalue() == 'b':
                        queue.append(tuple((i + 1, j)))
                        record.append(tuple((i + 1, j)))
                        map[i + 1][j].dictaddress.update({(i + 1, j): [(i, j)]})
                    map[i][j].value = 2
                    if map[i + 1][j].value == 'b':
                        flag = False
                        penitrate(map[i + 1][j].dictaddress, apos)
    #############
                    if map[i][j+1].getvalue() == 0 or map[i][j+1].getvalue() == 'b':
                        queue.append(tuple((i, j+1)))
                        record.append(tuple((i, j+1)))
                        map[i][j+1].dictaddress.update({(i, j+1): [(i, j)]})
                    map[i][j].value = 2
                    if map[i][j+1].value == 'b':
                        flag = False
                        penitrate(map[i][j+1].dictaddress, apos)
    ##########
                    if map[i+1][j].value==1 and map[i][j+1].value==1:
                        pass
                    else:
                        if map[i+1][j+1].getvalue() == 0 or map[i+1][j+1].getvalue() == 'b':
                            queue.append(tuple((i+1, j+1)))
                            record.append(tuple((i+1, j+1)))
                            map[i + 1][j+1].dictaddress.update({(i+1, j+1): [(i, j)]})
                        map[i][j].value = 2
                        if map[i+1][j+1].value == 'b':
                            flag = False
                            penitrate(map[i+1][j+1].dictaddress, apos)
    ##########
                    if map[i-1][j].value==1 and map[i][j-1].value==1:
                        pass
                    else:
                        if map[i-1][j-1].getvalue() == 0 or map[i-1][j-1].getvalue() == 'b':
                            queue.append(tuple((i-1, j-1)))
                            record.append(tuple((i-1, j-1)))
                            map[i - 1][j-1].dictaddress.update({(i-1, j-1): [(i, j)]})
                        map[i][j].value = 2
                        if map[i-1][j-1].value == 'b':
                            flag = False
                            penitrate(map[i-1][j-1].dictaddress, apos)
############

                    if map[i][j-1].getvalue() == 0 or map[i][j-1].getvalue() == 'b':
                        queue.append(tuple((i, j-1)))
                        record.append(tuple((i, j-1)))
                        map[i][j-1].dictaddress.update({(i, j-1): [(i, j)]})
                    map[i][j].value = 2
                    if map[i][j-1].value == 'b':
                        flag = False
                        penitrate(map[i][j-1].dictaddress, apos)
    ##########
                    if map[i+1][j].value==1 and map[i][j-1].value==1:
                        pass
                    else:
                        if map[i+1][j-1].getvalue() == 0 or map[i+1][j-1].getvalue() == 'b':
                            queue.append(tuple((i+1, j-1)))
                            record.append(tuple((i+1, j-1)))
                            map[i+1][j-1].dictaddress.update({(i+1, j-1): [(i, j)]})
                        map[i][j].value = 2
                        if map[i+1][j-1].value == 'b':
                            flag = False
                            penitrate(map[i+1][j-1].dictaddress, apos)
##################
                    if map[i-1][j].value==1 and map[i][j+1].value==1:
                        pass
                    else:
                        if map[i-1][j+1].getvalue() == 0 or map[i-1][j+1].getvalue() == 'b':
                            queue.append(tuple((i-1, j+1)))
                            record.append(tuple((i-1, j+1)))
                            map[i - 1][j+1].dictaddress.update({(i-1, j+1): [(i, j)]})
                        map[i][j].value = 2
                        if map[i-1][j+1].value == 'b':
                            flag = False
                            penitrate(map[i-1][j+1].dictaddress, apos)


        except Exception as e :
            print(e)

        for i in map:
            for j in i:
                j.draw()
        pygame.display.update()
    pygame.quit()

if __name__=='__main__':
    main()
