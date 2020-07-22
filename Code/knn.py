
X = [[2,4],[4,2],[4,4],[4,6],[6,2],[6,4]]
y = ['Orange','Orange','Blue','Orange','Blue','Orange']
from sklearn.neighbors import KNeighborsClassifier
model = KNeighborsClassifier(n_neighbors=3)
# Train the model using the training sets
model.fit(X,y)
x1 = int(input('Enter X Co-ordinate :' ))
y1 = int(input('Enter Y Co-ordinate : '))
predicted1= model.predict([[x1,y1]])
print("class for [",x1,",",y1,"] is (GENERAL KNN):",predicted1)
model1 = KNeighborsClassifier(n_neighbors=3, weights='distance')
model1.fit(X,y)
predicted2 = model1.predict([[x1,y1]])
print("class for [",x1,",",y1,"] is ( Distance Weighted KNN):",predicted2)
col=[]
for a in y:
    if a=='Orange':
        col.append('orange')
    elif a=='Blue':
        col.append('blue')
if(predicted1=='Orange'):
    col.append('orange')
else:
    col.append('blue')
#print(col)
X.append([x1,y1])
#print(df)
import numpy as np
import matplotlib.pyplot as plt
data = np.array(X)
x1=data[:,0:1]
#print(x)
y1=data[:,1:2]
#print(len(df))
for i in range(len(X)):    
    plt.scatter(x1[i],y1[i],c=col[i])
plt.show()