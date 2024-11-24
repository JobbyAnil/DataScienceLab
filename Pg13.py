from sklearn.datasets import load_iris

from sklearn.model_selection import train_test_split

from sklearn.tree import DecisionTreeClassifier

from sklearn import metrics

iris=load_iris()

x=iris.data

y=iris.target

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=1)

dt = DecisionTreeClassifier()

dt.fit(x_train,y_train)

y_pred=dt.predict(x_test)

print("Accuracy : ",metrics.accuracy_score(y_test,y_pred))

from sklearn import tree

import matplotlib.pyplot as plt

plt.figure(figsize=(12,12))

tree.plot_tree(dt, filled=True, feature_names=iris.feature_names, 

class_names=iris.target_names)

plt.title("Decision Tree Visualization")

plt.show()
