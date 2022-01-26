# author: Alex Reznik
# date: 6 December 2021
# course: Advanced Topics Computer Science
# instructor: Ms.Namasivayam
# file: ./polit_ovw.py
# operation: make the economic dataset plots


# import packages
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy as sp
import numpy as np

df = pd.read_csv('composite.csv')

# relationship: Policy Responsibility
# plot: Pie
def policyResponsibilityPie():
    counts = df['sq2'].value_counts()
    data = {'counts': counts}
    labels = ['policy approval', 'policy creation', 'policy implementation']
    colors = sns.color_palette('pastel')[0:3]
    plt.pie(data=pd.DataFrame(data = data),  x='counts', labels=labels, colors=colors, autopct="%.1f%%", explode=[0.04]*3)
    plt.title("Administrative Policy Responsibility", fontsize=12)
    plt.show()


# relationship: Continent vs Civil Service
# plot: Box
def continentCivilServiceBox():
    def compSeries():
        series = df['sq19']
        series *= -1
        return series.add(6)
    series = compSeries()
    ax = sns.boxplot(x=df['Continent'], y=series, palette='pastel')
    ax.set(ylabel='Difficulty of Civil Service Exam', xlabel='Continent', title='Continent vs Civil Service Exam')
    plt.show()

# run function
def main():
    policyResponsibilityPie()
    continentCivilServiceBox()

main()
