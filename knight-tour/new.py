import numpy as np

#moves = [[-2,1],[-2,-1],[-1,-2],[2,1],[2,-1],[1,2],[1,-2],[-1,2]]
moves =[[2,1],[1,2],[1,-2],[-1,2],[-1,-2],[2,-1],[-2,1],[-2,-1]]
ar = np.zeros([8,8])


def walk(x,y, mv, steps):
    nx = x + mv[0]
    ny = y+ mv[1]
    if nx>=0 and nx <=7 and ny>=0 and ny<=7 and ar[nx][ny]==0:
        ar[nx][ny] = 1
        steps.append(mv)
        if len(steps)==63:
            print(steps)
            return 1

        r=0
        for move in moves :
            a = walk(nx,ny,move,steps)
            r = r + a
        
        if r == 0 :
            ar[nx][ny] = 0
            steps.pop()
            return 0
        else :
            return 1
    else:
        return 0

x,y=1,0

ar[x][y]=1
steps = []
for move in [[-1,2],[2,1],[1,2]] :
    walk(x,y,move, steps)

print(ar)


