import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
eu_fat = pd.read_csv("eu_terrorism_fatalities_by_country.csv") 

eu_fat.head()

#print(eu_fat.loc[:, 'France'])
#print(eu_fat[['France', 'Belgium']])
print(eu_fat[['iyear','France', 'Belgium']])

fr_bel = eu_fat[['iyear','France', 'Belgium']]

fr_bel.plot(x = 'iyear', y = 'France')
plt.show()
