import math

def formula(x): # actual formula here
    y = x**2/(x**2-9)
    return y

for a in range(0,20):
    print()

avg = ""

''' Form input lists '''

det = [0,0]

inpu = input()
if inpu == "a":
    avg = "yes"
    input1 = float(input())
    input2 = float(input())
    inpu = "0"
x = float(inpu)
   
lx = [0,0,0,0]  
rx = [0,0,0,0]

lx[0] = x - .01
lx[1] = x - .001
lx[2] = x - .0001
lx[3] = x - .00001

rx[0] = x + .01
rx[1] = x + .001
rx[2] = x + .0001
rx[3] = x + .00001

''' Create output lists '''

xlist = lx + rx
ylist = [0,0,0,0,0,0,0,0]

for a in range(0,4):
    x1 = xlist[a]

    finaly = formula(x1)

    
    # the formula
    ylist[a] = round(finaly,6)

for a in range(4,8):
    x1 = xlist[a]

    finaly=formula(x1)

    
    # the formula
    ylist[a] = round(finaly,6)

print("Left Side:")
for a in range(0,4):
    print(str(round(xlist[a],5)),ylist[a])

print()
print("Right Side:")
for a in range(4,8):
    print(str(round(xlist[a],5)),ylist[a])




    