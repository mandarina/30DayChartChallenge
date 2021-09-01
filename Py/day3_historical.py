# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 11:52:14 2021

day 3: historical 
How much of our primary energy comes from renewables?
data: Share of primary energy consumption that came from renewable technologies* from 1980 to 2019
* the combination of hydropower, solar, wind, geothermal, wave, tidal and modern biofuels
[traditional biomass – which can be an important energy source in lower-income settings is not included].
datasource: https://ourworldindata.org/renewable-energy

@author: Karla
"""
# import libraries
import pandas as pd
import matplotlib.pyplot as plt

# data found here: https://ourworldindata.org/renewable-energy
df = pd.read_csv('../input/renewable-share-energy.csv')
print(df.head(3))
# drop code columns
df = df.drop(columns=['Code'])
# rename columns
df.columns = ['country', 'year', 'share_renewables']
print(df.describe())
# order by 2019 share in descending order to see which countries are best at it
df2019 = df[df.year == 2019].sort_values(by=['share_renewables'], ascending=False)
print(df2019.head())
# compare Chile to other countries from 1980 to 2019
dfpartial = df[(df.country == 'Chile') | (df.country == 'China') | (df.country == 'United States') | (df.country == 'Iceland') | (df.country == 'Brazil')].loc[(df.year >= 1980)]
print(dfpartial.describe())

# plot
fig, ax = plt.subplots()
fig.set_size_inches(10,5) # crear figura, especificando tamaño
# quitar el marco de la figura
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)
# Plot some data
# and keep plotting more data on the axes as many countries are selected...
for c in dfpartial.country.unique():
    ax.plot(dfpartial.year.unique(), dfpartial['share_renewables'].loc[dfpartial.country == c], label=c, marker='o')
ax.set_xlabel('Year', fontsize=10) # add x-label
ax.set_ylabel('Share of renewables (%)', fontsize=10) # add y-label
ax.set_title('How much of our primary energy comes from renewables?', fontsize=20) # add title
ax.minorticks_on() # turn on minor ticks on both axes
# rotate xlabels
for tick in ax.get_xticklabels():
    tick.set_rotation(90)
ax.grid(which='both', linestyle='--') # add minor and major grid lines
ax.legend()  # Add a legend.
plt.savefig('../output/day3_historical.jpg') # save figure
plt.show()
