import pandas as pd 
import matplotlib.pyplot as plt
# Read data from file 'filename.csv' 
# (in the same directory that your python process is based)
# Control delimiters, rows, column names with read_csv (see later) 
data = pd.read_csv("country_stats_1993_appendix2.csv") 
#print(data.head())
data.plot()
plt.show()