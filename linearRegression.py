import sklearn 
import matplotlib.pyplot as plt 
import numpy as np
import random as r
from sklearn import linear_model
from sklearn import model_selection

#celcius to farhenheit grap plot (basic)
# c  
# f
# c=>f equ is f=1.8*x + 32

x = list(range(0,10)) #C  #print without list method as see what happens 
y = [1.8*F +32 for F in x] #F #list comprehension add it for make graph the different r.randint(-5,5) 

plt.plot(x,y,'.-r') 
plt.show() #must use it other wise plot not gonna show 

x = np.array(x).reshape(-1,1)
y = np.array(y).reshape(-1,1)
print(x)

xTrain, xTest , yTrain , yTest = model_selection.train_test_split(x,y,test_size=0.2)

model = linear_model.LinearRegression()

model.fit(xTrain,yTrain)

print(f'Coeficient:{model.coef_}')
print(f'Intercept:{model.intercept_}')

accurcy = model.score(xTest,yTest)

print(f'Accuracy : {round(accurcy*100,2)}')

