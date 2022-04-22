import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

data = pd.read_csv('data5/diamonds.csv')
data['cut'].replace(['Fair', 'Premium'], [0, 1], inplace=True)

x = data[['carat', 'depth', 'table']].values
y = data['cut'].values

scaler = StandardScaler().fit(x)
x = scaler.transform(x)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

model = LogisticRegression().fit(x_train, y_train)

coef = model.coef_[0]

print('weight for model')
print(coef)

y_pred = model.predict(x_test)
print('confusion matrix')
print(confusion_matrix(y_test, y_pred))
print('accuracy:', model.score(x_test, y_test))

carat = 0.5
depth = 60
table = 60

x_pred = [[carat, depth, table]]
x_pred = scaler.transform(x_pred)

if model.predict(x_pred)[0] == 1:
    print('Diamond is likely a premium cut')
else:
    print('Diamond is likely a fair cut')
