import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import matplotlib.pyplot as plt

iris = pd.read_csv('iris.csv') 

X = iris.iloc[:, :3].values  # First three columns as features (sepal length, sepal width, petal width)
y = iris.iloc[:, 2].values   # Third column (petal length) as target


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)


model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print("Mean Absolute Error:", metrics.mean_absolute_error(y_test, y_pred))
print("Mean Squared Error:", metrics.mean_squared_error(y_test, y_pred))
print("Root Mean Squared Error:", np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

print("\nEnter The Sample Data:")
a = float(input("Enter Sepal Length In CM: "))
b = float(input("Enter Sepal Width In CM: "))
c = float(input("Enter Petal Width In CM: "))

sample = [[a, b, c]]
pred = model.predict(sample)
print('Predicted Petal Length =', pred[0])


# Visualization
plt.scatter(y_test, y_pred, color='blue', alpha=0.6)
plt.plot([y.min(), y.max()], [y.min(), y.max()],color="red")
plt.xlabel("Actual Petal Length")
plt.ylabel("Predicted Petal Length")
plt.title("Actual vs Predicted Petal Length")
plt.show()
