import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

data = pd.read_csv('data5/houses.csv')

x = data[['bathrooms', 'lot_size_1000_sqft', 'living_space_1000_sqft', 'garages', 'bedrooms', 'age', 'num_fire_places']].values
y = data['selling_price'].values

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
    x_bathrooms = x_test[i][0]
    x_lot_size_1000_sqft = x_test[i][1]
    x_living_space_1000_sqft = x_test[i][2]
    x_garages = x_test[i][3]
    x_bedrooms = x_test[i][4]
    x_age = x_test[i][5]
    x_num_fire_places = x_test[i][6]
    print(
        "Bathrooms:", float(x_bathrooms),
        "Lot Size sqft: ", float(x_lot_size_1000_sqft * 1000),
        "Living Space sqft:", float(x_living_space_1000_sqft * 1000),
        "Garages: ", float(x_garages),
        "Bedrooms:", float(x_bedrooms),
        "Age: ", float(x_age),
        "Number of Bedrooms: ", float(x_num_fire_places),
        "predict y val: ", y_pred,
        "actual y val:", actual
    )

print('New Test Data')
new_test = [[3, 8, 3, 2, 4, 20, 2]]
pred = model.predict(new_test)
    for i in range(len(new_test)):
    y_pred = round(float(pred), 2)
    x_bathrooms = new_test[i][0]
    x_lot_size_1000_sqft = new_test[i][1]
    x_living_space_1000_sqft = new_test[i][2]
    x_garages = new_test[i][3]
    x_bedrooms = new_test[i][4]
    x_age = new_test[i][5]
    x_num_fire_places = new_test[i][6]
    print(
        "Bathrooms:", float(x_bathrooms),
        "Lot Size sqft: ", float(x_lot_size_1000_sqft * 1000),
        "Living Space sqft:", float(x_living_space_1000_sqft * 1000),
        "Garages: ", float(x_garages),
        "Bedrooms:", float(x_bedrooms),
        "Age: ", float(x_age),
        "Number of Fireplaces: ", float(x_num_fire_places),
        "predict y val: ", y_pred,
    )







