"""

Task 3: Identify Current Environmental Remediation Parcels in Syracuse, NY

"""

#%%
import geopandas as gpd
import matplotlib.pyplot as plt

plt.rcParams['figure.dpi'] = 300

#%%

#Read the input shapefiles

remediation_parcels = gpd.read_file('NY_remediation_site_borders.zip')
city = gpd.read_file("syracuse_city_boundary.zip")

#Transform coordinate reference system as remediation parcels

city = city.to_crs(remediation_parcels.crs)

remediation_parcels['geometry'] = remediation_parcels.buffer(0)

#Clip remediation parcels to Syracuse boundary

syr_remediation_parcels = gpd.clip(remediation_parcels, city)

#%%

#Create a list of columns to keep

keepers = ["SITECODE", "SITENAME", "PROGRAM", "SHAPE_AREA", "geometry"]

#Trim the database

trimmed_remediation = syr_remediation_parcels[keepers].copy()

#%%

#Summarize number of parcels in each category

attrs = {'brownfield': 'Brownfield Cleanup Program',
         'superfund':'State Superfund Program',
         'restoration':'Environmental Restoration Program',
         'conserve':'Resource Conservation and Recovery',
         'voluntary':'Voluntary Cleanup Program'}

for col,program in attrs.items():
    trimmed_remediation[col] = trimmed_remediation['PROGRAM'] == program
    print(f'\n Number of {program}:', trimmed_remediation[col].sum())
      
#%%

#Map the remediation parcels with legend

fig1,ax1 = plt.subplots()
city.boundary.plot(ax=ax1,color='black')
trimmed_remediation.plot(ax=ax1,column='PROGRAM',legend=True)
#
ax1.set_title('Current Environmental Remediation Sites')
ax1.axis(False)
fig1.tight_layout()
fig1.savefig('current_remediation_parcels.png')

#%%

trimmed_remediation.to_file('remediation_parcel_inventory.gpkg',layer='remediation_parcels')