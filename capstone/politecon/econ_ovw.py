import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy as sp

# have to really structure the code and create the presentation
# create a handout for the presentation element, be very clear with the different visuals
# be clear and have a cohesive color scheme throughout the project
df = pd.read_csv('composite.csv')


# sns.histplot(data=df['Average Growth'], binwidth=300, kde=True)
def box():
    ax = sns.boxplot(x='Continent', y="Data.Infrastructure.Telephone Lines per 100 People", data=df, palette='pastel')
    ax.set(ylabel='% Increase Telephone Lines/100 People', xlabel='Continent', title='Continent vs Telephone Growth')
    plt.show()


def scatter():
    r, p = sp.stats.pearsonr(df['Data.Urban Development.Urban Population Percent'],
                             df["Data.Health.Life Expectancy at Birth, Total"])
    ax = sns.scatterplot(x='Data.Urban Development.Urban Population Percent',
                    y='Data.Health.Life Expectancy at Birth, Total',
                    hue='Continent',
                    palette='pastel',
                    data=df)
    title = 'Urban Population vs Life Expectancy - ' + "r=" + str(r)
    ax.set(ylabel="Life Expectancy % Increase", xlabel='Urban Population % Increase', title=title)
    plt.show()

def pie():
    counts = df['Continent'].value_counts()
    counts = counts.sort_values(ascending=False)
    data = {'counts': counts}
    labels = ['Asia', 'South America', 'Africa', 'North America', 'Europe']
    colors = sns.color_palette('pastel')[0:5]
    plt.pie(data=pd.DataFrame(data=data), x='counts', labels=labels, colors=colors, autopct="%.1f%%",
            explode=[0.04] * 5)
    plt.title("Continent Breakdown", fontsize=12)
    plt.show()


def hist():
    ax = sns.histplot(data=df['Average Growth'], binwidth=300, palette='pastel')
    ax.set(title = 'Average Economic Growth')
    plt.show()

box()
scatter()
pie()
hist()