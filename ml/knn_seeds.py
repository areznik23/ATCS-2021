import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, accuracy_score

# Area (A) - area of the seed
# Perimeter (P) - perimeter of the seed
# Compactness = 4*pi*A/P^2
# Kernel_length - Length of the seed
# Kernel_width - Width of the seed
# Asymmetry_coef - The coefficient of asymmetry for the seed
# Groove_length - the length of the groove down the middle of the seed
# Seed - the class of seed (Kama, Rosa, or Canadian)

data = pd.read_csv('data/seeds.csv')

feature_area = data['area'].values
feature_perimeter = data['perimeter'].values
feature_compactness = data['compactness'].values
feature_kernel_length = data['kernel_length'].values
feature_kernel_width = data['kernel_width'].values
feature_asymmetry_coef = data['asymmetry_coef'].values
feature_groove_length = data['groove_length'].values

classes = data['seed'].values

features = np.array([
    feature_area, feature_perimeter, feature_compactness, feature_kernel_length, feature_kernel_width, feature_asymmetry_coef, feature_groove_length
]).transpose()

class_labels = np.unique(data['seed'])

scaler = StandardScaler().fit(features)
features = scaler.transform(features)

features_train, features_test, classes_train, classes_test = train_test_split(features, classes, test_size=0.2)

# model = KNeighborsClassifier(n_neighbors=5).fit(features_train, classes_train)
#
# classes_pred = model.predict(features_test)
#
# print('accuracy', accuracy_score(classes_test, classes_pred))
#
# cm = confusion_matrix(classes_test, classes_pred, labels=class_labels)
#
# cmd = ConfusionMatrixDisplay(cm, display_labels=class_labels)

n_neighbors = []
accuracy = []
for k in range(2, len(features_train)):
    model = KNeighborsClassifier(n_neighbors=k).fit(features_train, classes_train)
    classes_pred = model.predict(features_test)
    n_neighbors.append(k)
    accuracy.append(accuracy_score(classes_test, classes_pred))

plot = sns.lineplot(x=n_neighbors, y=accuracy)
plt.xlabel('k')
plt.ylabel('accuracy')
plt.show()

