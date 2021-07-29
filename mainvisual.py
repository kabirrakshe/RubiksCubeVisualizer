import cv2 as cv
import numpy as np
class Cube():
    def __init__(self):
        self.white = ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W']
        self.yellow = ['Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y']
        self.red = ['R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R']
        self.orange = ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']
        self.green = ['G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G']
        self.blue = ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B']
    def reset(self):
        self.white = ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W']
        self.yellow = ['Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y']
        self.red = ['R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R']
        self.orange = ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']
        self.green = ['G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G']
        self.blue = ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B']
    def printcube(self):
        print(self.blue[:3])
        print(self.blue[3:6])
        print(self.blue[6:])
        for face in [self.white, self.red, self.yellow, self.orange]:
            if face == self.yellow:
                print(face[8:5:-1], end = '')
                continue
            print(face[:3], end = '')

        print()
        for face in [self.white, self.red, self.yellow, self.orange]:
            if face == self.yellow:
                print(face[5:2:-1], end = '')
                continue
            print(face[3:6], end = '')
        print()
        for face in [self.white, self.red, self.yellow, self.orange]:
            if face == self.yellow:
                print(face[2::-1], end = '')
                continue
            print(face[6:], end = '')
        print()
        print(self.green[:3])
        print(self.green[3:6])
        print(self.green[6:])

    def rotate(self, side, clckwise):
        if clckwise:
            side[0:2], side[2:6:3], side[:-3:-1], side[6:2:-3] = side[6:2:-3],side[0:2], side[2:6:3], side[:-3:-1]
        else:
            side[0:2], side[2:6:3], side[:-3:-1], side[6:2:-3] = side[2:6:3], side[:-3:-1], side[6:2:-3], side[0:2]
    def R(self):
        self.white[2::3], self.blue[2::3], self.yellow[2::3], self.green[2::3] = self.green[2::3],self.white[2::3], self.blue[2::3], self.yellow[2::3]
        self.rotate(self.red, True)
        return (self)

    def R_(self):
        self.white[2::3],self.blue[2::3], self.yellow[2::3], self.green[2::3] = self.blue[2::3], self.yellow[2::3], self.green[2::3],self.white[2::3]
        self.rotate(self.red, False)
        return (self)
    def M(self):
        self.white[1::3], self.blue[1::3], self.yellow[1::3], self.green[1::3] = self.green[1::3], self.white[1::3], self.blue[1::3], self.yellow[1::3]
        return (self)
    def M_(self):
        self.white[1::3], self.blue[1::3], self.yellow[1::3], self.green[1::3] = self.blue[1::3], self.yellow[1::3], self.green[1::3],self.white[1::3]
        return (self)
    def L(self):
        self.white[0::3], self.blue[0::3], self.yellow[0::3], self.green[0::3] = self.blue[0::3], self.yellow[0::3], self.green[0::3],self.white[0::3]
        self.rotate(self.orange, True)
        return (self)
    def L_(self):
        self.white[0::3], self.blue[0::3], self.yellow[0::3], self.green[0::3] = self.green[0::3], self.white[0::3], self.blue[0::3], self.yellow[0::3]
        self.rotate(self.orange, False)
        return (self)
    def U(self):
        self.white[:3], self.orange[:3], self.yellow[:5:-1], self.red[:3] = self.red[:3], self.white[:3], self.orange[:3], self.yellow[:5:-1]
        self.rotate(self.blue, True)
        return (self)
    def U_(self):
        self.white[:3], self.orange[:3], self.yellow[:5:-1], self.red[:3] = self.orange[:3], self.yellow[:5:-1], self.red[:3], self.white[:3]
        self.rotate(self.blue, False)
        return self
    def F(self):
        self.blue[6:], self.red[::3], self.green[2::-1], self.orange[::-3] = self.orange[::-3], self.blue[6:], self.red[::3], self.green[2::-1]
        self.rotate(self.white, True)
        return (self)
    def F_(self):
        self.blue[6:], self.red[::3], self.green[2::-1], self.orange[::-3] = self.red[::3], self.green[2::-1], self.orange[::-3], self.blue[6:]
        self.rotate(self.white, False)
        return(self)
    def D(self):
        self.white[6:], self.red[6:], self.yellow[2::-1], self.orange[6:] = self.orange[6:], self.white[6:], self.red[6:], self.yellow[2::-1]
        self.rotate(self.green, True)
        return self
    def D_(self):
        self.white[6:], self.red[6:], self.yellow[2::-1], self.orange[6:] = self.red[6:], self.yellow[2::-1], self.orange[6:], self.white[6:]
        self.rotate(self.green, False)
        return self
    def solve(self):
        all = {self.white : [self.blue, self.red, self.green, self.orange],
               self.blue : [self.yellow, self.red, self.white, self.orange],
              self.yellow : [self.green, self.red, self.blue, self.orange],
              self.red : [self.blue, self.yellow, self.green, self.white],
              self.orange : [self.blue, self.white, self.green, self.yellow]

               }
        missing = [9, None]
        for i in all:
            center = i[4]
            if len([x for x in i if x != center]) < missing[0]:
                missing = [len([x for x in i if x != center]), i]
        while True:
            side = missing[i]
            center = side[4]
            neighboring = all[side]
            for j in range(len(neighboring)):
                if neighboring[j] == center:
                    pass

cube = Cube()
print("Orient the white side of the cube towards yourself and\n the blue side of the cube towards the ceiling\n")
moves = input("Now Enter Moves Using Cube Notation. Separate moves with space: \n").split(' ')
seq = []
for move in moves:
    move = move.lower()
    if move == 'r':
        seq.append(cube.R)
    elif move == r"r'":
        seq.append(cube.R_)
    elif move == 'l':
        seq.append(cube.L)
    elif move == r"l'":
        seq.append(cube.L_)
    elif move == 'u':
        seq.append(cube.U)
    elif move == r"u'":
        seq.append(cube.U_)
    elif move == "f":
        seq.append(cube.F)
    elif move == r"f'":
        seq.append(cube.F_)
    elif move == "m":
        seq.append(cube.M)
    elif move == r"m'":
        seq.append(cube.M_)
    elif move == "d":
        seq.append(cube.D)
    elif move == r"d'":
        seq.append(cube.D_)


relation = {
    'R': (0,0,255),
    'W': (255,255,255),
    'B': (255,0,0),
    "G": (0,255,0),
    "Y" : (0,255,255),
    "O" : (0,165,255)
}
blank = np.zeros((800, 800, 3), dtype = 'uint8')
cv.imshow('screen', blank)
cv.waitKey(5000)
def draw():
    global blank
    count = -1
    for i in range(300, 411, 55):
        for j in range(300, 411, 55):
            count += 1
            cv.rectangle(blank, (j, i), (j+50, i+50), relation[cube.white[count]], -1)

    count = 255
    n = 11
    for i in range(295,224,-24): #Blue side
        count += 45
        n -= 6
        for j in range(count, count + 115,57):
            n += 1
            pts = np.array([[j,i],[j+50,i],[j+90,i-20],[j+40,i-20]], np.int32)
            cv.fillPoly(blank, [pts], relation[cube.blue[n]])


    #Red Side


    pts = np.array([[466, 300], [505,280],[505,330],[466,350]], np.int32)
    cv.fillPoly(blank, [pts], relation[cube.red[0]])
    pts = np.array([[466, 355], [505,335],[505,385],[466,405]], np.int32)
    cv.fillPoly(blank, [pts], relation[cube.red[3]])
    pts = np.array([[466, 410], [505,390],[505,440],[466,460]], np.int32)
    cv.fillPoly(blank, [pts], relation[cube.red[6]])

    pts = np.array([[510, 277], [549,257],[549,307],[510,327]], np.int32)
    cv.fillPoly(blank, [pts], relation[cube.red[1]])
    pts = np.array([[510, 332], [549,312],[549,362],[510,382]], np.int32)
    cv.fillPoly(blank, [pts], relation[cube.red[4]])
    pts = np.array([[510, 387], [549,367],[549,417],[510,437]], np.int32)
    cv.fillPoly(blank, [pts], relation[cube.red[7]])

    pts = np.array([[554, 254], [593,234],[593,284],[554,304]], np.int32)
    cv.fillPoly(blank, [pts], relation[cube.red[2]])
    pts = np.array([[554, 309], [593,289],[593,339],[554,359]], np.int32)
    cv.fillPoly(blank, [pts], relation[cube.red[5]])
    pts = np.array([[554, 364], [593,344],[593,394],[554,414]], np.int32)
    cv.fillPoly(blank, [pts], relation[cube.red[8]])


for i in seq:
    i()
    draw()
    cv.imshow('screen', blank)
    cv.waitKey(100)
cv.imshow('screen', blank)
cv.waitKey(0)
