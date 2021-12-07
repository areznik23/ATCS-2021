import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy as sp

# have to really structure the code and create the presentation
# create a handout for the presentation element, be very clear with the different visuals
# be clear and have a cohesive color scheme throughout the project
df = pd.read_csv('composite.csv')
counts = df['sq2'].value_counts()
data = {'counts': counts}
labels = ['policy creation', 'policy approval']
colors = sns.color_palette('pastel')[0:2]
plt.pie(data=pd.DataFrame(data = data),  x='counts', labels=labels, colors=colors, autopct="%.1f%%", explode=[0.04]*2)
plt.title("Administrative Policy Responsibility", fontsize=12)
plt.show()

df['corruption_level'] = df['sq15'].subtract(df['sq14'])
for i, v in df['corruption_level'].iteritems():
    if v < 0:
        df['corruption_level'][i] = 0

sns.scatterplot(data=df, x="corruption_level", y="Data.Health.Life Expectancy at Birth, Total", hue='sq2', style='sq2', palette="deep")
sns.regplot(data=df, x="corruption_level", y="Data.Health.Life Expectancy at Birth, Total")
r, p =r= sp.stats.pearsonr(df["corruption_level"], df["Data.Health.Life Expectancy at Birth, Total"])
print(r)
plt.show()

# need a way to exclude telephone development from the average growth metric
# test out civil service metrics
df['sq18'] = df['sq18'].fillna(0)
sns.scatterplot(data=df, x="sq18", y="Data.Health.Life Expectancy at Birth, Total")
sns.regplot(data=df, x="sq18", y="Data.Health.Life Expectancy at Birth, Total")
r, p = sp.stats.pearsonr(df["sq18"], df["Data.Health.Life Expectancy at Birth, Total"])
print(r)
plt.show()

# how much US aid is flowing to the country
# notes and sources - world population sheet, assumptions made
