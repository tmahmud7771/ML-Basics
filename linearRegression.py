import sklearn 
import matplotlib.pyplot as plt 
import numpy as np
import random as r

#celcius to farhenheit grap plot (basic)
# c  
# f
# c=>f equ is f=1.8*x + 32

x = list(range(0,10)) #C  #print with list method as see what happens 
y = [1.8*F +32 + r.randint(-5,5) for F in x] #F #list comprehension

plt.plot(x,y,'.-r') 
plt.show() #must use it other wise plot not gonna show 
