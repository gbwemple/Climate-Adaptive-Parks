"""

Task 1: Identify Current Climate Adaptive Parks in Syracuse, NY

"""

#%%

import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['figure.dpi'] = 300

#%%

#Read the input shapefiles

parcels = gpd.read_file("syracuse_city_parcels.zip")
parks = gpd.read_file("syracuse_city_parks.zip")
city = gpd.read_file("syracuse_city_boundary.zip")

#Transform coordinate reference system as parcels

city = city.to_crs(parcels.crs)

#%%

#Filter the parcels to select schools

is_school = (parcels['LUCODE'] == '612') & (parcels['MAIL_ADD1'] == '725 Harrison St')

print('Number of school parcels:',sum(is_school))

sel_parcels = parcels[is_school]

#%%

#Build the dataframe of merged parks and schools

df_parks = pd.concat({'parks':parks,'schools':sel_parcels})

df_parks.index.names = ['kind','id']

df_parks = df_parks.reset_index()

df_parks.fillna('',inplace=True)

df_parks = df_parks.copy()

df_parks['name'] = df_parks['NAME'] + df_parks['OWNERNAME1']

df_parks = df_parks[['kind','id','name','geometry']]

print('Number of parcels before filtering: ', len(df_parks))

#%%

#Plot park and school parcels

fig1,ax1 = plt.subplots()
city.boundary.plot(ax=ax1,color='gray')
df_parks.plot(ax=ax1,column='kind',legend=True)
ax1.set_title('Park and School Parcels')
ax1.axis(False)
fig1.tight_layout()
fig1.savefig('parks_and_schools.png')

#%%

#Filter the school and park parcels based on ratio

df_parks['area'] = df_parks.area

df_parks['radius'] = df_parks.area/df_parks.length

df_parks = df_parks.query('radius >= 15')

print('Number of parcels meeting radius criteria:', len(df_parks))

#%%

#Plot park and school parcels meeting radius criteria

fig2,ax2 = plt.subplots()
city.boundary.plot(ax=ax2,color='gray')
df_parks.plot(ax=ax2,column='kind',legend=True)
ax2.set_title('Park and School Parcels - Filtered')
ax2.axis(False)
fig2.tight_layout()
fig2.savefig('parks_and_schools_filtered.png')

#%%

#Make a buffer to combine parks within a 0.25mi distance

buffer_m = 0.25 * 1609 
#0.25 miles * 1609 m/mile
buffer = df_parks.buffer(buffer_m)

#%%

#Plot the buffer

fig3,ax3 = plt.subplots()
city.boundary.plot(ax=ax3,color='gray')
buffer.plot(ax=ax3,color='lightgreen')
df_parks.plot(ax=ax3,column='kind',legend=True)
ax3.set_title('Park and School Parcels Buffer')
ax3.axis(False)
fig3.tight_layout()
fig3.savefig('parks_and_schools_buffer.png')

#%%

#Filter the parks with the buffer

buffer = gpd.GeoDataFrame(geometry=buffer)

df_parks['acres'] = df_parks.area / 4046.86
buffer['source_area'] = df_parks.area
buffer['source_acres'] = df_parks['acres']

inter = df_parks.sjoin(buffer)
print('Number of records after join:',len(inter))

#Filter out self-matches
self_match_filter = inter[inter.index != inter['index_right']]
print('Number of records after filtering out self matches:',len(self_match_filter))

#Filter out combinations with less than two acres
combined_size_filter = self_match_filter.query("acres+source_acres >= 6")
print('Number of records after filtering out by combined size:',len(combined_size_filter))

#%%

#Map the current CAP inventory

fig4,ax4 = plt.subplots()
city.boundary.plot(ax=ax4,color='gray')
combined_size_filter.plot(ax=ax4,color='green')
ax4.set_title('Current CAP Inventory')
ax4.axis(False)
fig4.tight_layout()
fig4.savefig('current_CAP_parcels.png')

#%%

combined_size_filter.to_file('current_CAP_inventory.gpkg',layer='CAP_parcels')

