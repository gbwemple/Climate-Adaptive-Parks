"""

Task 5: Identify the Current Neighborhood Park Service Gap in Syracuse, NY and 
        Overlay with Potential CAPs

"""

#%%

import geopandas as gpd
import matplotlib.pyplot as plt

plt.rcParams['figure.dpi'] = 300

#%%

#Read the input shapefiles

dir_parks = '../Task1_Current-CAP-Inventory'
geo_parks = 'current_CAP_inventory.gpkg'

current_CAPs = gpd.read_file(f'{dir_parks}/{geo_parks}')
neighbors = gpd.read_file('syracuse_neighborhood_boundaries.zip')

#%%

#Make a map with neighborhoods and parks

#fig1,ax1 = plt.subplots()
#neighbors.boundary.plot(ax=ax1,color='black')
#current_CAPs.plot(ax=ax1)
#ax1.set_title('Neighborhoods & Current CAPs')
#ax1.axis(False)
#fig1.tight_layout()
#fig1.savefig('neighborhood_current_CAPs.png')

#%%

#Perform a spatial overlay for percentage neighborhood that is a park

parks_only = current_CAPs[['name','acres','geometry']].drop_duplicates()

CAP_clip = parks_only.clip(neighbors, keep_geom_type=True)

CAP_neighborhoods = gpd.overlay(CAP_clip,neighbors, how='union')

is_park = CAP_neighborhoods['name'].notna()

CAP_neighborhoods['area_joined'] = CAP_neighborhoods.area

CAP_neighborhoods = CAP_neighborhoods.query('area_joined > 1')

CAP_neighborhoods ['area_joined'] = is_park * CAP_neighborhoods ['area_joined']

CAP_neighborhoods['tab_share'] = (CAP_neighborhoods['area_joined'] / CAP_neighborhoods['Shape_Are'])

percentage = (CAP_neighborhoods.groupby(['NAME']).agg({'tab_share':'sum'}))
              
#%%

#Read ervp input shapefile

dir_ervp = '../Task4_Potential-CAP-Inventory'
geo_ervp = 'potential_CAP_inventory.gpkg'

potential_CAPs = gpd.read_file(f'{dir_ervp}/{geo_ervp}')

#%%

#Make a map with neighborhoods and potential CAPs

#fig2,ax2 = plt.subplots()
#neighbors.boundary.plot(ax=ax2,color='black')
#potential_CAPs.plot(ax=ax2,color='darkorange')
#ax2.set_title('Neighborhoods & Potential CAPs')
#ax2.axis(False)
#fig2.tight_layout()
#fig2.savefig('neighborhood_potential_CAPs.png')

#%%

#Make a map with neighborhoods, current CAPs, potential CAPs

fig3,ax3 = plt.subplots()
neighbors.boundary.plot(ax=ax3,color='black')
current_CAPs.plot(ax=ax3)
potential_CAPs.plot(ax=ax3,color='darkorange')
ax3.set_title('Current & Potential CAPs in Syracuse, NY')
ax3.axis(False)
fig3.tight_layout()
fig3.savefig('neighborhoods_all_CAPs.png')


#%%

#Join neighborhoods and potential CAPs

potential_CAPs_neighborhoods = potential_CAPs.sjoin(neighbors)

#%%

#Export CSVs

percentage.to_csv('percentages.csv')

CAP_neighborhoods.to_csv('current_CAPs_neighborhoods.csv')

potential_CAPs_neighborhoods.to_csv('potential_CAPs.neighborhoods.csv')











