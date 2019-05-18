import pandas as pd 
import matplotlib.pyplot as plt
# Read data from file 'filename.csv' 
# (in the same directory that your python process is based)
# Control delimiters, rows, column names with read_csv (see later) 
data = pd.read_csv("eu_terrorism_fatalities_by_country.csv") 

data = data[['iyear', 'France']]
#print(data.head())
data.plot(x='iyear', y='France')
plt.show()