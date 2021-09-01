# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 18:52:12 2021

day 4: Magical
data: Harry Potter and the Prisoner of Azkaban Movie Script
datasource https://www.kaggle.com/gulsahdemiryurek/harry-potter-dataset?select=Harry+Potter+3.csv
font source: https://www.fontget.com/font/magic-school-family/
icons source: https://picclick.com/Scrapbooking-Stickers-PH-Slim-Harry-Potter-Chibi-Characters-233144813787.html
@author: Karla
"""
# import libraries
import pandas as pd
import matplotlib.pyplot as plt
# you can download data from: https://www.kaggle.com/gulsahdemiryurek/harry-potter-dataset?select=Harry+Potter+3.csv
df = pd.read_csv('../input/HarryPotter3.csv', sep=';')
print(df.head(3))
# summarize script lines per character
summary = df['CHARACTER'].value_counts().reset_index()
summary.columns = ['Character', 'script_lines']
# show top 8 characters with most script lines
print(summary.head(8))
# add new custom font
# you can download the font from: https://www.fontget.com/font/magic-school-family/
import matplotlib.font_manager as fm
fe = fm.FontEntry(
    fname='../input/font/MagicSchoolTwo.ttf',
    name='magicSchool')
fm.fontManager.ttflist.append(fe) # append new font
# set new font for titles and labels
csfont = {'fontname':'magicSchool'}
### Start plotting
fig, ax = plt.subplots()
fig.set_size_inches(10,5)
ax.set_title('Characters with most script lines in Harry Potter and the Prisoner of Azkaban', fontsize=25, **csfont)
ax.set_xlabel('Characters', fontsize=15, **csfont)
ax.set_ylabel('Script Lines', fontsize=15, **csfont)
plt.xticks(fontsize=14, **csfont)
# Custom y limit to fit custom markers
ax.set_ylim(0, 400)
# remove top and right frame sides
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
# set gryffindor palette colours for all except Snape who has slytherin colour
mycolors = ['#740001', '#ae0001', '#eeba30', '#d3a625', '#000000', '#740001', '#ae0001','#5d5d5d']
# top 8 characters with most script lines
x = summary.loc[:7,'Character']
y = summary.loc[:7,'script_lines']
# plot bars
ax.bar(x, y, color=mycolors)
## add custom markers
import matplotlib.transforms as mpl
from svgpathtools import svg2paths
from svgpath2mpl import parse_path
# dict for custom markers
# harry potter icons from: https://picclick.com/Scrapbooking-Stickers-PH-Slim-Harry-Potter-Chibi-Characters-233144813787.html 
hpmarkers = {}
import os
directory = '../input/icons'
for filename in os.listdir(directory):
    if filename.endswith('.svg'):
        fn = filename[:-4]
        marker_path, attributes = svg2paths(os.path.join(directory, filename)) # get path
        hp_marker = parse_path(attributes[0]['d']) # retrieve attributes
        hp_marker.vertices -= hp_marker.vertices.mean(axis=0) # move vertices
        if fn in ['harry', 'sirius', 'snape']: # these markers need to rotate
            hp_marker = hp_marker.transformed(mpl.Affine2D().rotate_deg(180)) 
        hp_marker = hp_marker.transformed(mpl.Affine2D().scale(-1,1))
        hpmarkers[fn] = hp_marker
        idx = summary.index[summary['Character'] == fn.upper()]
        ax.plot(fn.upper(),summary.iloc[idx]['script_lines']+30,'o',marker=hpmarkers[fn],markersize=50, color='black')
# save figure
plt.savefig('../output/day4_magical.jpg')
plt.show()
