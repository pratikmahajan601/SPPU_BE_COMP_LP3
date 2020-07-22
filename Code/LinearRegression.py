import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
data = [[10,95],[9,80],[2,10],[15,50],[10,45],[16,98],[11,38],[16,93]]
data=np.array(data)
X = data[:,0:1]
Y = data[:,1:2]
regressor=LinearRegression()
regressor.fit(X,Y)
B1 = regressor.coef_
print("Coefficient : ",B1)
B0 = regressor.intercept_
print("Intercept : ",B0)
print("Accuracy : ",regressor.score(X,Y)*100)
print("Equation of Line : ")
print(B1,"x + ",B0)
plt.plot(X,Y,'o')
plt.plot(X,regressor.predict(X))
plt.xlabel('Number of hours spent driving')
plt.ylabel('Risk Score')
plt.show()