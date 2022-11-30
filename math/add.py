# add two integer by bit opretion
def add(a,b):
    while b != 0:
        x = (a^b)
        y =(a&b) << 1
        a = x
        b = y
    return x
print(add(9,10))




