import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

data = pd.read_csv('~/Desktop/ATCS-2021/ml/data/chirping.csv')
x = data['Temp'].values
y = data['Chirps'].values

x = x.reshape(-1, 1)

model = LinearRegression().fit(x, y)

slope = round(float(model.coef_), 2)
intercept = round(float(model.intercept_), 2)
r_squared = model.score(x, y)

# testing the model
x_predict = 77
prediction = float(model.predict([[ x_predict ]]))
print('Linear equation: y =', slope, "x +", intercept)
print('R Squared =', r_squared)
print('Prediction when x is', x_predict, "=", prediction)

# visualize the model
plt.figure(figsize=(5,4))
plt.scatter(x, y, c='purple')
plt.scatter(x_predict, prediction, c='blue')
plt.plot(x, slope*x + intercept, c = 'red', label = "line of best fit")

plt.xlabel('Temperature')
plt.ylabel('Chirps/Min')
plt.title("Cricket Chirps by Temperature")

plt.legend()
plt.show()
