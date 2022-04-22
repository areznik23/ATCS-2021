import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

''' Load Data '''
data = pd.read_csv("~/Desktop/ATCS-2021/ml/data/antelope.csv")
x_1 = data["Annual Precipitation"]
x_2 = data["Winter Severity"]
y = data["Fawn"]

fig, graph = plt.subplots(2)
graph[0].scatter(x_1, y)
graph[0].set_xlabel("Annual Precipitation")
graph[0].set_ylabel("Fawn")

graph[1].scatter(x_2, y)
graph[1].set_xlabel("Winter Severity")
graph[1].set_ylabel("Fawn")

print("Corr between Annual Precipitation and Fawn: ", x_1.corr(y))
print("Corr between Winter Severity and Fawn: ", x_2.corr(y))

plt.tight_layout()
plt.show()

''' Create Multiple Linear Regression Model '''
x = data[['Annual Precipitation', 'Winter Severity']].values
y = data['Fawn'].values

# Split into train and test data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

model = LinearRegression().fit(x_train, y_train)

# Print out the information
print("Model Information")
print("Annual Precipitation Coefficient:", model.coef_[0])
print("Winter Severity Coefficient:", model.coef_[1])
print("Intercept:", model.intercept_)

''' Model Testing '''

# get the predicted y-values for x_test - returns an array
predict = model.predict(x_test)

# compare the actual and predicted values
print('Testing linear model with test data')
for i in range(len(x_test)):
    actual = y_test[i]
    y_pred = round(predict[i], 2)
    x_precip = x_test[i][0]
    x_winter = x_test[i][1]
    print("Precip val:", float(x_precip), "Winter val: ", float(x_winter), "predict y val: ", y_pred, "actual y val:", actual)


