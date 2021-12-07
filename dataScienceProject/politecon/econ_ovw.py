# author: Alex Reznik
# date: 6 December 2021
# course: Advanced Topics Computer Science
# instructor: Ms.Namasivayam
# file: ./econ_ovw.py
# operation: make the economic dataset plots


# import packages
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy as sp

# import the composite dataset
df = pd.read_csv('composite.csv')

# relationship: Continent vs Telephone Lines/100 People
# plot: Box
def continentTelephoneGrowthBox():
    ax = sns.boxplot(x='Continent', y="Data.Infrastructure.Telephone Lines per 100 People", data=df, palette='pastel')
    ax.set(ylabel='% Increase Telephone Lines/100 People', xlabel='Continent', title='Continent vs Telephone Growth')
    plt.show()


# relationship: Urban Population vs Life Expectancy
# plot: Scatter
def urbanPopulationLifeExpectancyScatter():
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

# relationship: Continent
# plot: Pie
def continentPie():
    counts = df['Continent'].value_counts()
    counts = counts.sort_values(ascending=False)
    data = {'counts': counts}
    labels = ['Asia', 'South America', 'Africa', 'North America', 'Europe']
    colors = sns.color_palette('pastel')[0:5]
    plt.pie(data=pd.DataFrame(data=data), x='counts', labels=labels, colors=colors, autopct="%.1f%%",
            explode=[0.04] * 5)
    plt.title("Continent Breakdown", fontsize=12)
    plt.show()


# relationship: Average Growth
# plot: Histogram
def averageGrowthHist():
    ax = sns.histplot(data=df['Average Growth'], binwidth=300, palette='pastel')
    ax.set(title='Average Economic Growth')
    plt.show()

# run function
def main():
    continentTelephoneGrowthBox()
    urbanPopulationLifeExpectancyScatter()
    continentPie()
    averageGrowthHist()

main()