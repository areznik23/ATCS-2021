import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

# Urban_population_percentage: Percentage of the city’s total population that is urban
# Wine_consumption_per_capita: Litres per person per year
# Liquor_consumption_per_capita: Litres per person per year
# Cirrhosis_death_rate: Number of people per 1000 that died of Cirrhosis
# Number of people with Cirrhosis

# Urban_population_percentage,Wine_consumption_per_capita,Liquor_consumption_per_capita,Cirrhosis_death_rate

data = pd.read_csv('data5/drinking.csv')

x = data[['Urban_population_percentage', 'Wine_consumption_per_capita', 'Liquor_consumption_per_capita']].values
y = data['Cirrhosis_death_rate'].values

scaler = StandardScaler().fit(x)
x = scaler.transform(x)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

model = LinearRegression().fit(x_train, y_train)

print("R Squared Value: ", round(model.score(x_train, y_train), 2))

predict = model.predict(x_test)

print('Testing linear model with test data')
for i in range(len(x_test)):
    actual = y_test[i]
    y_pred = round(predict[i], 2)
    x_urbanpop = x_test[i][0]
    x_wineconsump = x_test[i][1]
    x_liquorconsump = x_test[i][2]
    print("Urban Population Percentage:", float(x_urbanpop), "Wine Consumption per Capita: ", float(x_wineconsump), "Liquor Consumption per Capita: ", float(x_liquorconsump), "Predicted Y Val:", y_pred, "Actual Y Val: ", actual)

print('New Test Data')
new_test = [[50, 10, 30]]
pred = model.predict(new_test)
print('Testing linear model with test data')
for i in range(len(new_test)):
    y_pred = round(float(pred), 2)
    x_urbanpop = new_test[i][0]
    x_wineconsump = new_test[i][1]
    x_liquorconsump = new_test[i][2]
    print("Urban Population Percentage:", float(x_urbanpop), "Wine Consumption per Capita: ", float(x_wineconsump), "Liquor Consumption per Capita: ", float(x_liquorconsump), "Predicted Y Val:", y_pred)

