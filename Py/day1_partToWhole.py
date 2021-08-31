# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 11:47:33 2021

Day 1: Part to Whole
2016 Olympics, share of women in team Chile
dataset: modern Olympic Games from Athens 1896 to Rio 2016
data source: https://www.kaggle.com/heesoo37/120-years-of-olympic-history-athletes-and-results

@author: Karla
"""

import pandas as pd
# read data
df = pd.read_csv("../input/athlete_events.csv")
print(df.shape)
for col in df:
    print(col)
print(df.describe())
print(df.Medal.unique())
print(df.Games.unique())
# Team Chile historical participation in Summer Olympics
chdf = df.loc[(df.Team == 'Chile') & (df.Games.astype(str).str.contains('Summer'))]
# Total Medals won by Chile in all Summer Olympics History
print(chdf.Medal.value_counts())
# Not that many medals, lets see share of females in Team Chile in 2016 Summer Olympics
# ch_fem = chdf.groupby(['Year']).Sex.value_counts(normalize=True)
ch_fem = chdf.loc[(chdf['Year'] == 2016)].Sex.value_counts(normalize=True)
print(ch_fem)
# plot

import matplotlib.pyplot as plt
from pywaffle import Waffle

mylabels = [str(i) + ' (' + str(int(round(ch_fem.loc[i] * 100,0))) + '%)' for i in ch_fem.index]

fig = plt.figure(
    FigureClass=Waffle,
    rows=10,
    values=[int(round(i*100,0)) for i in ch_fem.values],
    title={
        'label': '2016 Olympics, Share of Women in Team Chile',
        'loc': 'center',
        'fontdict': {
            'fontsize': 15
        }
    },
    colors = ['#a1896e', '#dd5317'],
    font_size=15,
    icon_legend=True,
    legend={
        #'labels': ch_fem.index.tolist(), 
        'labels': mylabels, 
        'loc': 'upper left', 
        'bbox_to_anchor': (1, 1)
    }
)
plt.savefig('../output/day1_partTowhole.jpg')