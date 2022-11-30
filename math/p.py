def mf(n):
    s=1
    while n > 1 :
       s= s*n
       n= n-1
    return s
      
print(mf(100))

def ss(n):
    result=0
    for number in range(1,n+1):
        result+=number*number
    return result
print(ss(5))

# line 1-8 is factorial of n
# line 10- 15 is sum of squares
    