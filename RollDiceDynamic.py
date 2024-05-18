#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 18 20:10:26 2024

@author: lenovom
"""

from matplotlib import animation
import matplotlib.pyplot as plt
import sys
import random
import seaborn as sns

def newFrame(frameNr, rolls_per_frame, eyeNr, eyeStatistics, limit = 10000):
    for i in range(rolls_per_frame):
        eyeStatistics[random.randrange(1,7)-1] += 1
    
    plt.cla()
    series = sum(eyeStatistics)
    if series > limit-rolls_per_frame:
        mPlotAnimation.pause()
    plot_name = f'Frequency of rolling distinct number of eyes in {series} rolls'
    axis = sns.barplot(x=eyeNr, y=eyeStatistics, palette='mako', hue=eyeNr, legend=False)
    axis.set_title(plot_name)

    axis.set(xlabel='Number of eyes:', ylabel='Frequency:')
    axis.set_ylim(top=max(eyeStatistics) * 1.15)

    for bar, roll_count_label in zip(axis.patches, eyeStatistics):
        xText = bar.get_x() + bar.get_width() / 2.0
        yText = bar.get_height()
        text = f'{roll_count_label}\n{~roll_count_label/series:.3%}'
        axis.text(xText, yText, text, fontsize=10, ha='center', va='bottom')

if len(sys.argv) < 3:
    print("Error: The number of arguments is to small!\nYou should try: " \
          "python", f'{sys.argv[0]}', "6000 20\n * 6000 - number of frames\n * 20 - number of rolls per frame\nThe max number of rolls is 10,000!")
    sys.exit();

frameNr = int(sys.argv[1])
rolls_per_frame = int(sys.argv[2])

sns.set_style('whitegrid')
window_object = plt.figure('Simulating a series of rolls with a Dice')
xLabel = list(range(1,7))
eye_counter = [0]*6

mPlotAnimation = animation.FuncAnimation(window_object, newFrame, frames=frameNr, interval = 33, fargs=(rolls_per_frame, xLabel, eye_counter))

plt.show()