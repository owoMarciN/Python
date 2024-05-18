#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 18 17:08:09 2024

@author: lenovom
"""

import matplotlib.pyplot as plt
import numpy as np
import random
import seaborn as sns

series = 600000

rolls = [random.randrange(1, 7) for i in range(series)]
eyes, roll_count = np.unique(rolls, return_counts=True)

#for eyes , roll_count in zip(eyes, roll_count):
    #print(f'{eyes:>2}{roll_count:>10}')

series_str = f'{series}'
plot_name = f'Frequency of rolling distinct number of eyes in {series_str} rolls'

sns.set_style('whitegrid')

axis = sns.barplot(x=eyes, y=roll_count, palette='mako', hue=roll_count, legend=False)
axis.set_title(plot_name)
axis.set(xlabel='Number of eyes:', ylabel='Frequency:')
axis.set_ylim(top=max(roll_count) * 1.15)

for bar, roll_count_label in zip(axis.patches, roll_count):
    xText = bar.get_x() + bar.get_width() / 2.0
    yText = bar.get_height()
    roll_count_label_str = f'{roll_count_label}'
    text = f'{roll_count_label_str}\n{~roll_count_label/series:.3%}'
    axis.text(xText, yText, text, fontsize=10, ha='center', va='bottom')
