import pandas as pd 
import matplotlib.pyplot as plt
# Read data from file 'filename.csv' 
# (in the same directory that your python process is based)
# Control delimiters, rows, column names with read_csv (see later) 
deaths_by_year = pd.read_csv("eu_terrorism_fatalities_by_country.csv") 
deaths_by_year_france = deaths_by_year[['iyear', 'France']]

pop_global= pd.read_csv("population.csv")
#pop_global.set_index('Country Name',inplace=True)
pop_fr = pop_global.loc[pop_global['Country Name'] == 'France']
pop_fr_clean = pop_fr.loc[:, '1970':'2018']

pop_fr_clean_t = pop_fr_clean.transpose()
pop_fr_clean_t.columns = ['Population']

deaths_pop = pd.concat([pop_fr_clean_t, deaths_by_year_france], sort=True)
print(deaths_pop.head())

fig = plt.figure()

# Divide the figure into a 2x1 grid, and give me the first section
ax1 = fig.add_subplot(211)

# Divide the figure into a 2x1 grid, and give me the second section
ax2 = fig.add_subplot(212)

deaths_by_year_france.plot(x='iyear', ax=ax1)
pop_fr_clean_t.plot(ax=ax2)

#deaths_by_year_france.plot(x = 'iyear')
plt.show()