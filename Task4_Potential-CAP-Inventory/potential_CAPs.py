# -*- coding: utf-8 -*-
"""

Task 4: Combine and Filter the Vacant (vp) and Environmental Remediation (er) 
        Parcels in Syracuse, NY

"""

#%%

import geopandas as gpd
import matplotlib.pyplot as plt

city = gpd.read_file("syracuse_city_boundary.zip")

#%%

#Read the environmental remediation parcels. Create a marker to identify as er.

dir_er = '../Task3_Current-Remediation-Parcels'
geo_er = 'remediation_parcel_inventory.gpkg'

current_er = gpd.read_file(f'{dir_er}/{geo_er}')
current_er['is_er'] = True

print('Number of ER',len(current_er))

#%%

#Read the vacant parcels. Create a marker to identify as vp.

dir_vp = '../Task2_Current-Vacant-Parcels'
geo_vp = 'vacant_parcel_inventory.gpkg'

current_vp = gpd.read_file(f'{dir_vp}/{geo_vp}')
current_vp['is_vp'] = True

print('Number of VP',len(current_vp))

#%%

#Build the overlay

combined_er_vp = current_er.overlay(current_vp,
                      how='union',
                      keep_geom_type=True,
                      make_valid=True)

#Display origin of each part of parcel with marker

for col in ['is_er','is_vp']:
    combined_er_vp[col] = combined_er_vp[col].fillna(False)

#List the counts of each type of parcel part

print(combined_er_vp[['is_er','is_vp']].value_counts(dropna=False))

#Give each parcel part unique id

combined_er_vp['id'] = combined_er_vp.index

#%%

#Map the parcels combined

fig1,ax1 = plt.subplots()
combined_er_vp.plot(ax=ax1,color='darkorange')
ax1.set_title('Current ER and VP Inventory')
ax1.axis(False)
fig1.tight_layout()
fig1.savefig('combined_er_vp.png')

#%%

#Save layers

current_er.to_file('er-vp.gpkg',layer='ER')
current_vp.to_file('er-vp.gpkg',layer='VP')
combined_er_vp.to_file('er-vp.gpkg',layer='overlay')
#%%

#Filter the parcels

over_er_vp = gpd.read_file('er-vp.gpkg',layer ='overlay')

#%%

#Filter the er and vp parcels based on ratio

combined_er_vp['area'] = combined_er_vp.area
combined_er_vp['radius'] = combined_er_vp.area/combined_er_vp.length


combined_er_vp = combined_er_vp.query('radius >= 15')

print('Number of er and vp parcels meeting radius criteria:', len(combined_er_vp))

#%%

#Make a buffer to combine er_vp within a 0.25mi distance

buffer_m = 0.25 * 1609 
#0.25 miles * 1609 m/mile
buffer = combined_er_vp.buffer(buffer_m)

#%%

#Filter er_vp with the buffer

buffer_combo = gpd.GeoDataFrame(geometry=buffer)

combined_er_vp['acres'] = combined_er_vp.area / 4046.86
buffer_combo['source_area'] = combined_er_vp.area
buffer_combo['source_acres'] = combined_er_vp['acres']
buffer_combo['source_id'] = combined_er_vp['id']

#er_vp_id brings the id column from slice
er_vp_id = combined_er_vp.sjoin(buffer_combo)
print('Number of records after join:',len(er_vp_id))

#Filtering out self-matches
self_match_filter = er_vp_id[er_vp_id.index != er_vp_id['index_right']]
print('Number of records after filtering out self matches:',len(self_match_filter))


#Grouping by new column 'source_id' added to slice_er_vp

agg_acres = er_vp_id.groupby('source_id')['acres'].sum()
print('Number of records after groupby:',len(agg_acres))

#Add a column for aggregated acreage

combined_er_vp['agg_acres'] = agg_acres

#Filtering out combinations with less than six acres

combined_size_filter = combined_er_vp.query("acres + agg_acres >= 6")
print('Number of records after filtering out by combined size:',len(combined_size_filter))


#%%

#Transform to same coordinate reference system as neighbors
city = city.to_crs(combined_size_filter.crs)

#Map the potential CAP inventory

fig2,ax2 = plt.subplots()
city.boundary.plot(ax=ax2,color='gray')
combined_size_filter.plot(ax=ax2,color='darkorange')
ax2.set_title('Potential CAP Inventory')
ax2.axis(False)
fig2.tight_layout()
fig2.savefig('potential_CAP_inventory.png')


#%%

combined_size_filter.to_file('potential_CAP_inventory.gpkg',layer='potential_CAP_parcels')