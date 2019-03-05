import os
import re
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


SHOW_PLOT = False

# printing pandas version
print(f'Pandas version: {pd.__version__}\n')


print('Creating Series')
print(
    pd.Series(['San Francisco', 'San Jose', 'Sacramento'])
)
print()

print('Creating DataFrame')
city_names = pd.Series(['San Francisco', 'San Jose', 'Sacramento'])
population = pd.Series([852469, 1015785, 485199])
print(
    pd.DataFrame({'City name': city_names, 'Population': population})
)
print()

print('Load CSV DataFrame')
# path_csv = 'https://download.mlcc.google.com/mledu-datasets'
path_csv = os.path.dirname(os.path.realpath(__file__)) + '/../data'
csv_name = 'california_housing_train.csv'
csv_url = f'{path_csv}/{csv_name}'
print(csv_url)
california_housing_dataframe = pd.read_csv(csv_url, sep=',')
print(
    california_housing_dataframe.describe()
)
print()

print('Displaying first few records')
print(
    california_housing_dataframe.head()
)
print()

print(
    california_housing_dataframe.hist('housing_median_age')
)
if SHOW_PLOT:
    plt.show()

print('Accessing Data')
cities = pd.DataFrame({'City name': city_names, 'Population': population})
print(type(cities['City name']))
print(cities['City name'])
print(type(cities['City name'][1]))
print(cities['City name'][1])
print(type(cities[0:2]))
print(cities[0:2])
print()

print('Manipulating Data')
print(population / 1000)
print(np.log(population))
print(population.apply(lambda val: val > 1000000))
cities['Area square miles'] = pd.Series([46.87, 176.53, 97.92])
cities['Population density'] = cities['Population'] / \
    cities['Area square miles']
# cities['new column'] = cities.apply(
#     lambda val:
#         val['Area square miles'] > 50.0 and val['City name'].startswith(
#             'San '),
#     axis=1)
cities['Is wide and has saint name'] = (
    cities['Area square miles'] > 50) & cities['City name'].apply(
        lambda name: name.startswith('San'))
print(cities)
print()

print('Indexes')
print(city_names.index)
print(cities.index)
print(cities.reindex([2, 0, 1]))
print(cities.reindex(np.random.permutation(cities.index)))
print(cities.reindex([2, 0, 1, 14]))
print()
