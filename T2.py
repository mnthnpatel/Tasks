
import clrprint as clr
import random

list = ["red","yellow","blue"]
m = random.randint(1000,9999)
n = random.randint(1000,9999)
v = (chr(m))
s = (chr(n))



for i in range(1,999):        
    x = random.choice(list)
    # clr.clrprint("\u2764  \u2133" ,clr=x ,end=" ")
    clr.clrprint(f"{v}  {s}",clr=x,end = " ")