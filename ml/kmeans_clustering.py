import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

data = pd.read_csv('data/customer.csv')

x = data[['Annual Income', 'Spending Score']]

scaler = StandardScaler().fit(x)
x = scaler.transform(x)

# plt.scatter(x[:, 0], x[:, 1])
# plt.xlabel('Annual Income')
# plt.ylabel('Spending Score')
# plt.show()

# inertias = []
# for k in range(1, 11):
#     kmeanModel = KMeans(n_clusters=k).fit(x)
#     inertias.append(kmeanModel.inertia_)
#
# plt.plot(range(1, 11), inertias, 'bx-')
# plt.xlabel('Values of K')
# plt.ylabel('Inertia')
# plt.show()

# best value => k = 5
k = 5

km = KMeans(n_clusters=k).fit(x)
centroids = km.cluster_centers_
labels = km.labels_

# sets the graph size
plt.figure(figsize=(5,4))

# graphing each of the clusters one by one
for i in range(k):
    cluster = x[labels == i]
    cluster_income = cluster[:, 0]
    cluster_spending = cluster[:, 1]
    plt.scatter(cluster_income, cluster_spending)

centroids_income = centroids[:, 0]
centroids_spending = centroids[:, 1]
plt.scatter(centroids_income, centroids_spending, marker='X', s=100, c='r')

plt.xlabel('Annual Income')
plt.ylabel('Spending Score')
plt.show()

