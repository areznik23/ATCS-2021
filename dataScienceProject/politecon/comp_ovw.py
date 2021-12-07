# author: Alex Reznik
# date: 6 December 2021
# course: Advanced Topics Computer Science
# instructor: Ms.Namasivayam
# file: ./comp_ovw.py
# operation: make the comparison plots


# import packages
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy as sp
import numpy as np

# import the composite dataset
df = pd.read_csv('composite.csv')

# formats the plot title to include Pearson's coefficient
def formatTitle(words, r):
    return words + " - r=" + str(r)

# operation to switch lower to higher values to indicate difficulty
def computeCSE():
    series = df['sq19']
    return (-1 * series).add(6)

# drops outliers from the scatterplot dataframes
def dropOutliers(data, indxs):
    return data.drop(indxs[0])

# relationship: Civil Service Exam vs Urban Population
# plot: Scatter
def civServiceUrbanpopScatter():
    series = computeCSE()
    ax = sns.scatterplot(x=series, y=df['Data.Urban Development.Urban Population Percent'], palette='pastel')
    res = {'cse': series, 'up': df['Data.Urban Development.Urban Population Percent']}
    res = pd.DataFrame(res)
    res = dropOutliers(res, np.where((res['up'] < 100)))
    ax = sns.scatterplot(x=res['cse'], y=res['up'], palette='pastel')
    r, p = sp.stats.pearsonr(res['cse'], res['up'])
    ax.set(ylabel='% Increase Urban Development', xlabel='Difficulty of Civil Service Exam',
           title=formatTitle('Civil Service Exam vs Urban Development', r))
    plt.show()

# relationship: Civil Service Exam vs Telephone Lines/100 People
# plot: Scatter
def civServiceTelGrowthScatter():
    series = computeCSE()
    ax = sns.scatterplot(x=series, y=df["Data.Infrastructure.Telephone Lines per 100 People"], palette='pastel')
    res = {'cse': series, 'tg': df["Data.Infrastructure.Telephone Lines per 100 People"]}
    res = pd.DataFrame(res)
    res = dropOutliers(res, np.where((res['cse'] < 3.5) & (res['tg'] > 10000)))
    ax = sns.scatterplot(x=res['cse'], y=res['tg'], palette='pastel')
    r, p = sp.stats.pearsonr(res['cse'], res['tg'])
    ax.set(ylabel='% Increase Telephone Lines/100 People', xlabel='Difficulty of Civil Service Exam',
           title=formatTitle('Civil Service Exam vs Telephone Growth', r))
    plt.show()

# relationship: Policy Responsibility vs Average Growth
# plot: Box
def polResponseAvgGrowthBox():
    ax = sns.boxplot(x='sq2', y="Average Growth", data=df, palette='pastel')
    ax.set(ylabel='Average Growth', xlabel='Policy Responsibility', title='Policy Responsibility vs Average Growth')
    plt.show()

# relationship: Public Private Crossover vs Telephone Lines/100 People
# plot: Scatter
def publicPrivateTelGrowthScatter():
    res = {'pp': df['sq12'], 'tg': df["Data.Infrastructure.Telephone Lines per 100 People"]}
    res = pd.DataFrame(res)
    sns.scatterplot(x=df['sq12'], y=df["Data.Infrastructure.Telephone Lines per 100 People"], palette='pastel')
    res = dropOutliers(res, np.where((res['pp'] < 3.5) & (res['tg'] > 12500)))
    ax = sns.scatterplot(x=res['pp'], y=res['tg'], palette='pastel')
    r, p = sp.stats.pearsonr(res['pp'], res['tg'])
    ax.set(ylabel='% Increase Telephone Lines/100 People', xlabel='Public Private Crossover',
           title=formatTitle('Public-Private vs Telephone Growth', r))
    plt.show()

# run function
def main():
    civServiceUrbanpopScatter()
    civServiceTelGrowthScatter()
    polResponseAvgGrowthBox()
    publicPrivateTelGrowthScatter()

main()