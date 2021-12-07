import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy as sp
import numpy as np

df = pd.read_csv('composite.csv')

def pie():
    counts = df['sq2'].value_counts()
    data = {'counts': counts}
    labels = ['policy approval', 'policy creation', 'policy implementation']
    colors = sns.color_palette('pastel')[0:3]
    plt.pie(data=pd.DataFrame(data = data),  x='counts', labels=labels, colors=colors, autopct="%.1f%%", explode=[0.04]*3)
    plt.title("Administrative Policy Responsibility", fontsize=12)
    plt.show()


def scatter():
    series = compute_cse()
    ax = sns.boxplot(x=df['Continent'], y=series, palette='pastel')
    ax.set(ylabel='Difficulty of Civil Service Exam', xlabel='Continent', title='Continent vs Civil Service Exam')
    plt.show()

def compute_cse():
    series = df['sq19']
    series *= -1
    series = series.add(6)
    return series


