"""

Task 2: Identify Current Vacant Parcels in Syracuse, NY

"""

#%%
import geopandas as gpd
import matplotlib.pyplot as plt

plt.rcParams['figure.dpi'] = 300

#%%

#Read the input shapefiles

parcels = gpd.read_file("syracuse_city_parcels.zip")
city = gpd.read_file("syracuse_city_boundary.zip")

#Transform to same coordinate reference system as parcels

city = city.to_crs(parcels.crs)

#%%

#Create a list of columns to keep

keepers = ["LAND_USE", "LU_GROUP", "OWNERNAME1", "ADDRESSNUM", "ADDRESSNAM", "Shape__Are", "geometry"]

#Trim the database

trimmed_vacant = parcels[keepers].copy()

is_vacant = (trimmed_vacant['LU_GROUP'] == 'Vacant')
        
print('Number of vacant parcels:',sum(is_vacant))

sel_vacant = trimmed_vacant[is_vacant]

#%%

#Summarize number of parcels in each category

attrs = {'Com Vacant W/Minor Imprv': 'Com Vacant W/Minor Imprv',
         'Vacant Commercial Land':'Vacant Commercial Land',
         'Ind Vacant W/Minor Imprv':'Ind Vacant W/Minor Imprv',
         'Vacant Industrial Land':'Vacant Industrial Land',
         'Res Vacant Land W/Imprv':'Res Vacant Land W/Imprv',
         'Residential Vacant Land':'Residential Vacant Land',
         'Rural Lot 10 Ac Or Less':'Rural Lot 10 Ac Or Less'}

sel_vacant = sel_vacant.copy()

for col,vacancy in attrs.items():
    sel_vacant[col] = sel_vacant['LAND_USE'] == vacancy
    print(f'\n Number of {vacancy} parcels:',sel_vacant[col].sum())

#%%

#Map the vacant parcels with legend

#fig1,ax1 = plt.subplots()
#city.boundary.plot(ax=ax1,color='black')
#sel_vacant.plot(ax=ax1,column='LAND_USE',legend=True)
#fixed = ax1.get_legend()
#fixed.set_bbox_to_anchor((2,1))
#ax1.legend(loc='lower right', title='Vacancy Type')
#ax1.set_title('Vacant Parcels')
#ax1.axis(False)
#fig1.tight_layout()
#fig1.savefig('current_vacant_parcels.png')

#%%

sel_vacant.to_file('vacant_parcel_inventory.gpkg',layer='vacant_parcels')