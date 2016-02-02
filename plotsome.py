import matplotlib
matplotlib.use('Qt4Agg')
import matplotlib.pyplot as plt
import os, sys
from sys import argv
import csv
import numpy as np
import pandas as pd
from pandas import DataFrame as df

# add argument statement for csv file
#filename = sys.argv[1]

# read csv file
df = pd.read_csv('/users/paulchung/Desktop/python_projects/data_projects/test_plot_2.csv', index_col=False)
#print df

#sub-setting data by team and saving into own variables
# try using
#if "FRS" in df["Team"]:
FRS_complete = df.iloc[0:9]
CS_complete = df.iloc[10:]

#sub-setting by CS team by columns
CS_backlogsize_composite = CS_complete.loc[10:, "Backlog Size"]
CS_storiescompleted_composite = CS_complete.loc[10:,"Stories Completed"]
CS_sprints_composite = CS_complete.loc[10:,"Team"]


# empty sets for each team data
CS_backlogsize = []
CS_storiescompleted = []
CS_sprints = []

FRS_backlogsize = []
FRS_storiescompleted = []
FRS_sprints = []


#CS Dataset
for i in CS_backlogsize_composite:
    CS_backlogsize.append(i)

for i in CS_storiescompleted_composite:
    CS_storiescompleted.append(i)

for i in CS_sprints_composite:
    CS_sprints.append(i)



#FRS Dataset

# structure data frame


# create matplotlib graph model(s) example code below


# 10 sprints
n_groups = 10

fig, ax = plt.subplots()

index = np.arange(n_groups)
bar_width = 0.35

opacity = 0.4

backlog_size = plt.bar(index, CS_backlogsize, bar_width,
                 alpha=opacity,
                 color='r',
                 label='Backlog Size')

stories_completed = plt.bar(index + bar_width, CS_storiescompleted, bar_width,
                 alpha=opacity,
                 color='g',
                 label='Stories Completed')

plt.xlabel('Sprints')
plt.ylabel('Story Points')
plt.title('Customer Success Team: Q4 2015')
plt.xticks(index + bar_width, (CS_sprints))
plt.legend()

plt.tight_layout()
plt.show()






# need trendline

# output into ipython?
