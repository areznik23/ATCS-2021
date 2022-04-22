import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

data = pd.read_csv('~/Desktop/ATCS-2021/ml/data/chirping.csv')
x = data['Temp'].values
y = data['Chirps'].values

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
x_train = x_train.reshape(-1, 1)

x = x.reshape(-1, 1)

model = LinearRegression().fit(x_train, y_train)

slope = round(float(model.coef_), 2)
intercept = round(float(model.intercept_), 2)
r_squared = model.score(x_train, y_train)

# testing the model
# x_predict = 77
# prediction = float(model.predict([[ x_predict ]]))
x_test = x_test.reshape(-1, 1)
predict = model.predict(x_test)

print('Testing linear model with test data')
for i in range(len(x_test)):
    actual = y_test[i]
    y_pred = round(predict[i], 2)
    x_val = x_test[i]
    print("x val:", float(x_val), " predict y val: ", y_pred, "actual y val:", actual)

print('Linear equation: y =', slope, "x +", intercept)
print('R Squared =', r_squared)

# visualize the model
plt.figure(figsize=(5,4))
plt.scatter(x_train, y_train, c='purple', label='training data')
plt.scatter(x_test, y_test, c='blue', label = 'test data')
plt.scatter(x_test, predict, c='orange', label = 'predictions')
plt.plot(x_train, slope*x_train + intercept, c = 'red', label = "line of best fit")

plt.xlabel('Temperature')
plt.ylabel('Chirps/Min')
plt.title("Cricket Chirps by Temperature")

plt.legend()
plt.show()
