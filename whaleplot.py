import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import descartes
import geopandas as gpd
from shapely.geometry import Point, Polygon
import geopandas as gpd
from geopandas import GeoDataFrame


train = pd.read_csv('southernocean_microbial - Sheet1.csv')
test = pd.read_csv('southernocean_microbial - Sheet1.csv')

reg = linear_model.LinearRegression()
reg.fit(train[['cyanobacteria','temp_2017','temp_2018','temp_2020']],train.boom)

arr_result = reg.predict(test[['cyanobacteria','temp_2017','temp_2018','temp_2020']])

rounded_boom = np.around(arr_result)
rounded_boom.astype(int)
something = train['boom'].values[:156]

accuracy_val = 100 - mean_squared_error(something,rounded_boom)

df = pd.read_csv('southernocean_microbial - Sheet1.csv')
plt.scatter(x=df['Longitude'],y=df['Latitude'])

geometry = [Point(xy) for xy in zip(df['Longitude'], df['Latitude'])]
gdf = GeoDataFrame(df, geometry=geometry)   


world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
gdf.plot(ax=world.plot(figsize=(10, 6)), marker='^', color='orange', markersize=20)

plt.savefig('static/world.jpg')
