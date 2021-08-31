# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 11:11:20 2021
day 2: Pictogram

Data: wine consumption by country per person in litres. Historical data from 1963 to 2014
datasource: https://ourworldindata.org/alcohol-consumption
Pictogram chart plotting historical data of Chile with custom markers on top of a barh

@author: Karla
"""

# import libraries
import matplotlib as mpl
from svgpathtools import svg2paths
from svgpath2mpl import parse_path
import pandas as pd
import matplotlib.pyplot as plt

### make custom markers
# you can download data from: https://ourworldindata.org/alcohol-consumption
wine_path, attributes = svg2paths('../input/winebottle.svg')

# d stores vertices and path codes 
# parse_path returns a matplotlib path object
wine_marker = parse_path(attributes[0]['d'])

# shift vertices so that marker left corner is at center of data point 
wine_marker.vertices -= wine_marker.vertices.mean(axis=0)
wine_marker = wine_marker.transformed(mpl.transforms.Affine2D().scale(-1,1))

# read file
df = pd.read_csv('../input/wine-consumption-per-person.csv')
print(df.shape)
print(df.head())

# Select 2014 data
df2014 = df[(df.Year == 2014)]
# rename columns
df2014.columns = ['country','code','year','litres']
# Compare Chile to France, Portugal, Italy, Argentina and USA
p2014 = df2014[(df2014.country == "Chile") | (df2014.country == "Argentina")| (df2014.country == "France")| (df2014.country == "Portugal")| (df2014.country == "Italy")| (df2014.country == "United States")]

# add column with consumption as bottles of wine. Each bottle represents 1 litre of wine
p2014b = p2014.assign(wineBottles = p2014['litres'].transform(lambda x: int(x)))
print(p2014b.head())

# Start plotting
plt.figure(figsize=(10,5))
plt.title('2014 Wine Consumption per Person', fontsize=20)
plt.xlabel('Litres (1bottle = 1Litre of wine)')

### Plot with custom markers
for i in p2014b.index:
    nb = p2014b.loc[i,'wineBottles'] # 1 bottle of wine = 1 litre of wine
    plt.plot([i for i in range(1,nb+1)],[p2014b.loc[i,'country']]*nb,'o',marker=wine_marker,markersize=30, color='#9c1727')

# Plot barh
x = p2014b['litres']
y = p2014b['country']
plt.barh(y,x, color='#E6E8E6')
# remove top and right frame sides
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['top'].set_visible(False)
# save fig
plt.savefig('../output/day2_pictogram.jpg')
plt.show()
