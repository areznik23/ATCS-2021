"""
A Machine Learning algorithm to predict car prices

@author: Ms. Namasivayam (replace with your name)
@version: 02/23/2022
@source: CodeHS
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

''' Load Data '''
data = pd.read_csv("~/Desktop/ATCS-2021/ml/data/car.csv")
x_1 = data["miles"]
x_2 = data["age"]
y = data["Price"]

''' Visualize Data '''
fig, graph = plt.subplots(2)
graph[0].scatter(x_1, y)
graph[0].set_xlabel("Total Miles")
graph[0].set_ylabel("Price")

graph[1].scatter(x_2, y)
graph[1].set_ylabel("Price")
graph[1].set_xlabel("Car Age")

print("Correlation between Total Miles and Car Price:", x_1.corr(y))
print("Correlation between Age and Car Price:", x_2.corr(y))

plt.tight_layout()
plt.show()

''' TODO: Create Linear Regression '''
# Reload and/or reformat the data to get the values from x and y
x = data[['miles', 'age']].values
y = data['Price'].values

# Separate data into training and test sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

# Create multivariable linear regression model
model = LinearRegression().fit(x_train, y_train)

# Find and print the coefficients, intercept, and r squared values.
# Each rounded to two decimal places.
print("Model Information")
print("Annual Precipitation Coefficient:", round(model.coef_[0], 2))
print("Winter Severity Coefficient:", round(model.coef_[1], 2))
print("Intercept:", round(model.intercept_, 2))
print("R Squared Value: ", round(model.score(x_train, y_train), 2))

# Test the model
predict = model.predict(x_test)
# Print out the actual vs the predicted values
print('Testing linear model with test data')
for i in range(len(x_test)):
    actual = y_test[i]
    y_pred = round(predict[i], 2)
    x_miles = x_test[i][0]
    x_age = x_test[i][1]
    print("Miles val:", float(x_miles), "Age val: ", float(x_age), "predict y val: ", y_pred, "actual y val:", actual)

new_test = [[89000, 10], [150000, 20]]
pred = model.predict(new_test)
for i in range(len(new_test)):
    actual = y_test[i]
    y_pred = round(pred[i], 2)
    x_miles = new_test[i][0]
    x_age = new_test[i][1]
    print("Miles val:", float(x_miles), "Age val: ", float(x_age), "predict y val: ", y_pred, "actual y val:", actual)


