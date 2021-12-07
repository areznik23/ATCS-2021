# author: Alex Reznik
# date: 6 December 2021
# course: Advanced Topics Computer Science
# instructor: Ms.Namasivayam
# file: ./clean.py
# operation: clean and merge the datasets to a composite dataset that is then output

# import packages
import pandas as pd


# import of the datframes and casting
econ = pd.read_csv('econdevelopment.csv')
polit = pd.read_csv('politicalstructure.csv')

# initial merge to get the composite table
comp = pd.merge(econ, polit, left_on="Country", right_on="Country")

# cast the country column in each table to be a string
def countryToString():
    polit['Country'] = polit['Country'].astype(str)
    econ['Country'] = econ['Country'].astype(str)

# condenses the time frame to compute the growth from first to last years
def computeGrowth(firstYear, lastYear):
    columns = []
    computed_data = []
    count = 0
    total_growth = 0
    for name, data in firstYear.iteritems():
        if "Data" in name:
            count += 1
            columns.append(name)
            if data == 0:
                pct_growth = 0
            else:
                pct_growth = ((lastYear[name] - data) / data) * 100
                total_growth += pct_growth
            computed_data.append(pct_growth)
    columns.insert(0, 'Average Growth')
    avg_growth = total_growth / count
    computed_data.insert(0, avg_growth)
    return [columns, computed_data]

# computes the growth for every country
def growthRows():
    result = []
    columns = []
    country = comp['Country'].loc[0]
    firstYear = comp.loc[0]
    for index, row in comp.iterrows():
        if row['Country'] != country:
            country = row['Country']
            lastYear = comp.loc[index - 1]
            columns, computed_data = computeGrowth(firstYear, lastYear)
            columns.insert(0, 'Country')
            computed_data.insert(0, row['Country'])
            result.append(computed_data)
    return result, columns

# merges the new economic growth table with the political table on the common countries
# replaces blank values with zeroes as well
def mergeDf():
    result, columns = growthRows()
    result = pd.DataFrame(result, columns=columns)
    final = pd.merge(result, polit, left_on="Country", right_on="Country")
    final['sq2'] = final['sq2'].round(decimals=0)
    final.replace(r'^\s*$', 0, regex=True)
    final.to_csv('composite.csv')


# run function 
def main():
    countryToString()
    growthRows()
    mergeDf()

main()