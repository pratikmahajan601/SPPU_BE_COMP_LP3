#install graphviz for tree visualization
import pandas as pd
import numpy as np
dataset=pd.read_csv(r"data.csv")
#print(dataset)
# reading dataset
X=dataset.iloc[:,:-1]
y=dataset.iloc[:,5].values
#Perform Label Encoding
from sklearn.preprocessing import LabelEncoder
labelencoder_X=LabelEncoder()
X = X.apply(LabelEncoder().fit_transform)
#print(X)

from sklearn.tree import DecisionTreeClassifier
regressor=DecisionTreeClassifier(random_state=0)
regressor.fit(X.iloc[:,1:5],y)
#Predict value
X_in=np.array([1,1,0,0])
y_pred=regressor.predict([X_in])
print("Prediction :",y_pred)

from sklearn.externals.six import StringIO
from IPython.display import Image
from sklearn import tree
import pydotplus
dot_data = tree.export_graphviz(regressor, out_file=None, filled=True, rounded=True, special_characters=True)
graph = pydotplus.graph_from_dot_data(dot_data)
Image(graph.create_png())