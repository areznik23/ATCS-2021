import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split

data = pd.read_csv('data/suv.csv')
data['Gender'].replace(['Male', 'Female'], [0, 1], inplace=True)
x = data[['Age', 'EstimatedSalary', 'Gender']].values
y = data['Purchased'].values

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

age = int(input('how old is customer?'))
gender = int(input('is the customer male(0) or female(1)'))
salary = int(input('how much does the customer make in a year'))

x_pred = [[age, salary, gender]]
x_pred = scaler.transform(x_pred)

if model.predict(x_pred)[0] == 1:
    print('customer will likely buy an suv')
else:
    print('customer likely will not buy an suv')