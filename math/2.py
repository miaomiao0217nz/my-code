t=63320
s= t%60
h=t//3600
m=(t-s)%3600/60
print(h,(":"),int(m),(":"),s)


def time(n):
    i=n%3600
    h=n//3600
    m=i//60
    s=i%60
    print(h,m,s)

time(66653)
# two ways of figuring out the digital time from seconds