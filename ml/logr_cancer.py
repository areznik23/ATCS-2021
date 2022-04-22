import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

data = pd.read_csv('data/breast_cancer.csv')

x = data[['Age', 'Nodes']].values
y = data['Survived_5_Years'].values

scaler = StandardScaler().fit(x)
x = scaler.transform(x)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

model = LogisticRegression().fit(x_train, y_train)

coef = model.coef_[0]

print('weights for model')
print(coef)

y_pred = model.predict(x_test)
print('confusion matrix')
print(confusion_matrix(y_test, y_pred))
print('accuracy:', model.score(x_test, y_test))

age = int(input('how old is patient? '))
nodes = int(input('is many nodes does the patient have? '))

x_pred = [[age, nodes]]
x_pred = scaler.transform(x_pred)

if model.predict(x_pred)[0] == 1:
    print('patient will likely survive 5 years')
else:
    print('patient likely will not survive 5 years')

