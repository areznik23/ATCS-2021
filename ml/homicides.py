import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

data = pd.read_csv('data5/homicides.csv')

x = data[['Inhabitants', 'Percent_with_income_below_5000', 'Percent_unemployed']].values
y = data['Murders_per_year_per_million'].values

scaler = StandardScaler().fit(x)
x = scaler.transform(x)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

model = LinearRegression().fit(x_train, y_train)

predict = model.predict(x_test)

print("R Squared Value: ", round(model.score(x_train, y_train), 2), '\n')

print('Testing linear model with test data')
for i in range(len(x_test)):
    actual = y_test[i]
    y_pred = round(predict[i], 2)
    x_inhabitants = x_test[i][0]
    x_percent_with_income_below_5000 = x_test[i][1]
    x_percent_unemployed = x_test[i][2]
    print(
        "Inhabitants:", float(x_inhabitants),
        "Percent with income below 5000: ", float(x_percent_with_income_below_5000),
        "Percent Unemployed:", float(x_percent_unemployed),
        "predict y val: ", y_pred,
        "actual y val:", actual
    )

print('New Predictions \n')
new_test = [[600000, 5, 5]]
pred = model.predict(new_test)
for i in range(len(new_test)):
    x_inhabitants = new_test[i][0]
    x_percent_with_income_below_5000 = new_test[i][1]
    x_percent_unemployed = new_test[i][2]
    print(
        "Inhabitants:", float(x_inhabitants),
        "Percent with income below 5000: ", float(x_percent_with_income_below_5000),
        "Percent Unemployed:", float(x_percent_unemployed),
        "predict y val: ", float(pred),
    )
