import math

def formula(x): # actual formula here
    y = (x**3-1)/(x**2-1)
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

if avg == "yes":
    y = (formula(input2) - formula(input1))/(input2-input1)
    print()
    print("Outputs:")
    print(round(formula(input1),6),round(formula(input2),6))
    print()
    print("Average Rate of Change:")
    print(round(y,6))
    exit()
    

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

    y = formula(x)
    y1 = formula(x1)

    finaly = (y - y1)/(x - x1)

    
    # the formula
    ylist[a] = round(finaly,6)

for a in range(4,8):
    x1 = xlist[a]

    y = formula(x)
    y1 = formula(x1)

    finaly = (y1 - y)/(x1 - x)

    
    # the formula
    ylist[a] = round(finaly,6)

print("Left Side:")
for a in range(0,4):
    print(str(xlist[a])+","+inpu,ylist[a])

print()
print("Right Side:")
for a in range(4,8):
    print(inpu+","+str(xlist[a]),ylist[a])




    