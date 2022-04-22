"""
@author: Alex Reznik
@version: 02/23/2022
@source: CodeHS
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

''' Load Data '''
data = pd.read_csv("data/blood_pressure.csv")
x = data["Age"]
y = data["Blood Pressure"]

''' TODO: Create Linear Regression '''
# Get the values from x and y
# Use reshape to turn the x values into 2D arrays:
x = x.values
y = y.values
x = x.reshape(-1, 1)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
x_train = x_train.reshape(-1, 1)

# Create the model
model = LinearRegression().fit(x_train, y_train)

# Find the slope and intercept
# Each should be a float and rounded to two decimal places.
slope = round(float(model.coef_), 2)
intercept = round(float(model.intercept_), 2)

# Print out the linear equation
print('Linear equation: y =', slope, "x +", intercept)

# Predict the the blood pressure of someone who is 43 years old.
# x_predict = 43
# prediction = round(float(model.predict([[ x_predict ]])), 2)

x_test = x_test.reshape(-1, 1)
predict = model.predict(x_test)

# Print out the prediction
# print('Predicted blood pressure when person is', x_predict, "years old =", prediction)

print('Testing linear model with test data')
for i in range(len(x_test)):
    actual = y_test[i]
    y_pred = round(predict[i], 2)
    x_val = x_test[i]
    print("x val:", float(x_val), " predict y val: ", y_pred, "actual y val:", actual)


''' Visualize Data '''
# set the size of the graph
plt.figure(figsize=(5, 4))

# label axes and create a scatterplot
plt.scatter(x_train, y_train, c='purple', label='training data')
plt.scatter(x_test, y_test, c='blue', label = 'test data')
plt.scatter(x_test, predict, c='orange', label = 'predictions')
plt.plot(x_train, slope*x_train + intercept, c = 'red', label = "line of best fit")

plt.xlabel("Age")
plt.ylabel("Systolic Blood Pressure")
plt.title("Systolic Blood Pressure by Age")
plt.scatter(x, y)
plt.show()

# print("Pearson's Correlation: r = :", x.corr(y))
