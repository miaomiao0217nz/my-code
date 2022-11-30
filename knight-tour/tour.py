import numpy as np
moves=[[-1,2],[-2,1],[1,2],[2,1],[-1,-2],[-2,-1],[1,-2],[2,-1]]
ar=np.zeros([8,8])
def walk(x,y,move,steps):
    nx= x + move[0]
    ny= y + move[1]
    if x >=0 and x<=7 and y>=0 and y<=7 and nx >=0 and nx<=7 and ny>=0 and ny<=7 and ar[nx][ny]==0:
        ar[nx][ny]=1
        steps.append(move)
        if len(steps)<=63:
            print(steps)
            return 1
        r = 0
        for move in moves:
            a = walk(x,y,move,steps)
            r = r + a


print(ar)


          
