import math

def frange(x_start,x_end,increment=1.):
    if x_end is None:
        x_end,x_start=x_start,0
    else:
        x_start=float(x_start)
    count=int(math.ceil(x_end-x_start)/increment)
    return(x_start+n*increment for n in range(count))

for x in frange(1, 5, 0.1):
    print(x)
