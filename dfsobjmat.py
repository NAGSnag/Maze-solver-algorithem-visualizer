import pickle
import random
import time
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
mway=[]

class box():
    def __init__(self,x,y,value=0):
        self.boxx=x
        self.boxy=y
        self.value=value
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
                return (i,j)
def getbpos():
    for i in range(80):
        for j in range(80):
            if map[i][j].getvalue()=='b':
                return i,j

def yshort():
    ydpath=[]
    print('mapshort')
    for i in range(2,78):
        for j in range(2,78):
            if map[i][j].getvalue()==3:
                if map[i][j+2].getvalue()==3:
                    if map[i][j+1].getvalue()==2:
                        #map[i][j+1].changevalue(4)
                        ydpath.append((i,j+1))
    return ydpath



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



    # print('ypath')
    # path=shortpath[:]
    # counter=1
    # for item in path:
    #     if map[item[0]+1][item[1]].getcolor()==4:
    #         print(map[item[0]][item[1]+2],item)
    #     if map[item[0]][item[1]+1].getcolor() == 4:
    #         print(map[item[0]][item[1]], map[item[0]][item[1] + 2])
    #         # a=path.index(item)
    #         # b=path.index((item[0]+2,item[1]))
    #         # if a-b>0:counter=-1
    #         # for i in range(path.index(item),b,counter):
    #         #     path.pop(i)
    #         # path.append(item)
    #         # path.append((item[0]+2,item[1]))
    #         # path.append((item[0]+1,item[1]))
    #
    # return path
    #
    #
    #
    #

    # for i in range(3,78):
    #     for j in range(3,78):
    #         try:
    #             if map[i][j].getvalue() == 3:
    #                 if map[i][j + 2].getvalue() == 3:
    #                     if map[i][j + 1].getvalue() == 4:
    #                         a = path.index((i, j))
    #                         b = path.index((i, j + 2))
    #                         if b-a>0:
    #                             counter=1
    #                         else:counter=-1
    #                         for i in range(a, b,counter):
    #                             path.pop(i)
    #                         path.append((i, j))
    #                         path.append((i, j + 1))
    #                         path.append((i, j + 2))
    #         except Exception as e:
    #             print(e)
    # return path


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








def short(shortpath):
    short = shortpath[:]
    for item in shortpath:
        try:
            if map[item[0] + 2][item[1]].getvalue()==3 and map[item[0] + 1][item[1]].getvalue()==2:
                geta = short.index(item)
                x, y = item[0] + 2, item[1]
                temp = (x, y)
                if temp in short:
                    getb = short.index(temp)
                    for i in range(geta, getb):
                        short.pop(i)
                    short.append(item)
                    x1, y1 = item[0] + 1, item[1]
                    temp2 = (x1, y1)
                    short.append(temp2)
                    print(f'done link {(x, y), item}')

            elif map[item[0] - 2][item[1]].getvalue()==3 and map[item[0] - 1][item[1]].getvalue()== 2:
                x, y = item[0] - 2, item[1]
                #
                geta = short.index(item)
                x, y = item[0] - 2, item[1]
                temp = (x, y)
                if temp in short:
                    getb = short.index(temp)
                    for i in range(geta, getb):
                        short.pop(i)
                    short.append(item)
                    x1, y1 = item[0] - 1, item[1]
                    temp2 = (x1, y1)
                    short.append(temp2)
                    print(f'done link {(x, y), item}')

            if map[item[0] + 1][item[1]].getvalue()== 3:
                geta = short.index(item)
                x, y = item[0] + 1, item[1]
                temp = (x, y)
                if temp in short:
                    getb = short.index(temp)
                    for i in range(geta, getb):
                        short.pop(i)
                    short.append(item)
            elif map[item[0] - 1][item[1]].getvalue()== 3:
                geta = short.index(item)
                x, y = item[0] - 1, item[1]
                temp = (x, y)
                if temp in short:
                    getb = short.index(temp)
                    for i in range(geta, getb):
                        short.pop(i)
                    short.append(item)
                    print(f'done link {(x, y), item}')

        except Exception as e:
            print(e)
            print('not done')
            pass
    return short






#########################################################################################################################
#########################################################################################################################
def main():
    counter = 0
    global clock
    run=True
    path =[]
    shortpath=[]
    mflag=False
    flag=False
    mpath=[]


    while run:
        clock.tick(fps)
        pygame.display.set_caption(f'FPS:{int(clock.get_fps())}   pathfindergui')



        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
        left, middle, right = pygame.mouse.get_pressed()
        if left:
            pos = pygame.mouse.get_pos()
            col,row = getclickpos(pos, 80, 800)
            print(col,row)
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

###########################################################################################################
        keypressed = pygame.key.get_pressed()
        if keypressed[pygame.K_s]:
            with open('map.pickle', 'wb') as file:
                obj = map[:]
                pickle.dump(obj, file)
            print('saved')


        if keypressed[pygame.K_r]:
            for i in range(1,79):
                for j in range(2,79,2):
                    map[i][j].changevalue(1)
                    choice = random.choice(list(range(2,79,2)))
                    map[j][choice].changevalue(0)





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


            # rand = random.choice([0, -1,])
            # mcur = mpath.pop()
            # mway=[]
            #
            # mpways = [(mcur[0], mcur[1] + 1), (mcur[0], mcur[1] - 1), (mcur[0] + 1, mcur[1]), (mcur[0] - 1, mcur[1])]
            # random.shuffle(mpways)
            # cnt=0
            #
            # # while mpath:
            # #     mcur = mpath.pop()
            # #     mpways = [(mcur[0], mcur[1] + 1), (mcur[0], mcur[1] - 1), (mcur[0] + 1, mcur[1]),(mcur[0] - 1, mcur[1])]
            # #     random.shuffle(mpways)
            # #     for item in mpways:
            # #         if item[0] <= 78 and item[0] >= 3 and item[1] <= 78 and item[1] >= 3:
            # #             if map[item[0]][item[1]].getvalue() == 1:
            # #                 map[item[0]][item[1]].changevalue(0)
            # #                 map[mcur[0] + item[0] // 2][mcur[1] + item[1] // 2].changevalue(0)
            # #                 mpath.append(item)
            #
            #
            # for item in mpways:
            #
            #     if item in mpath:
            #         continue
            #     elif  map[item[0]][item[1]].getvalue()==0:
            #         continue
            #     elif item[0] <= 78 and item[0] >= 3 and item[1] <= 78 and item[1] >= 3:
            #         if map[item[0]][item[1]].getvalue()==1:
            #
            #             map[item[0]][item[1]].changevalue(0)
            #             #map[mcur[0] + item[0] // 2][mcur[1] + item[1] // 2].changevalue(0)
            #             mpath.append(item)
            #             mway.append(item)
            #             continue
            #
            #
            # if len(mpath) == 0:
            #
            #     mpath.append(mway.pop())
            #
            #     mpath.append(mway.pop())
            #
            #
            #
            #
            #
            #
            #
            #
            #
            #
            # # for item in mpways:
            # #     if cnt==4:
            # #         cnt=0
            # #     else:cnt+=1
            # #     if item in mpath:
            # #         continue
            # #
            # #     elif map[item[0]][item[1]].getvalue()==0:
            # #         continue
            # #     elif item[0]<=78 and  item[0]>=3 and  item[1]<=78 and item[1]>=3:
            # #         if map[item[0] + 1][item[1]] in mpath or map[item[0]][item[1] + 1] in mpath or map[item[0]][item[1] - 1] in mpath or map[item[0] - 1][item[1]] in mpath:
            # #             continue
            # #         elif map[item[0]][item[1]].getvalue() == 1:
            # #             mpath.append(item)
            # #             if cnt==1:
            # #                 map[item[0]][item[1]].changevalue(0)
            # #             continue
            #
            #
            #
            #



        if keypressed[pygame.K_SPACE]:
            x, y = getapos()
            path.append((x,y))
            flag=True
        try:
            if flag:
                cur = path.pop()

            print(len(shortpath), len(path))
            pways = [(cur[0], cur[1] + 1), (cur[0], cur[1] - 1), (cur[0] + 1, cur[1]), (cur[0] - 1, cur[1])]


            for item in pways:
                try:
                    if item in shortpath:
                        get = shortpath.index(item)
                        for i in range(get + 1, len(shortpath)-1):
                            shortpath.pop(i)
                        shortpath.append(cur)
                except Exception:
                    pass

                if map[item[0]][item[1]].getvalue() in [1, 2, 'a']:
                    continue
                elif map[item[0]][item[1]].getcolor() == 'g':
                    continue
                elif item in path:
                    continue
                elif map[item[0]][item[1]].getvalue() == 'b':
                    path.append(item)
                    print('traced')
                    flag = False
                    for item in shortpath:
                        map[item[0]][item[1]].changevalue(3)
                    yd=yshort()
                    for item in yd:
                        map[item[0]][item[1]].changevalue(4)
                    ypathd=ypath()
                    #for item in ypathd:
                    #    map[item[0]][item[1]].changevalue(3)

                    #for item in yd:
                      #  map[item[0]][item[1]].changevalue(2)




                    #spath=short(shortpath)
                    # for item in spath:
                    #     map[item[0]][item[1]].changevalue(4)



                else:
                    if item not in path:
                        path.append(item)
                        shortpath.append(cur)
                        map[item[0]][item[1]].changevalue(2)
        except Exception as e:
            print('NO ROUTES FOUND')

###########################################################################################################
#display
        for i in map:
            for j in i:
                j.draw()
        pygame.display.update()
    pygame.quit()

if __name__=='__main__':
    main()




