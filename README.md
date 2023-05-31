# Climate Adaptive Parks: Closing the Recreational Space Service Gap

# Abstract
Access to park space varies throughout Syracuse, NY and has led to underserved neighborhoods. This tool has identified the neighborhoods in Syracuse that have the least access to Climate Adaptive Parks (CAP). The tool will then identify areas of land that could potentially serve as a new CAP to bridge the existing service gap. The tool can be personalized to the user's preferences by being able to rank characteristics of potential areas of land as more favorable than another. 

# Method
This analysis used Syracuse City parcel and neighborhood boundary data from Open Data Syracuse and environmental remediation data from NYS GIS Clearinghouse. Parcels are selected to meet CAP criteria to see current and potential CAPs. The existing service gap is identified by overlaying the neighborhood boundary and current CAPs.

# Scripts
1. ParkIdentification.py 
   The Syracuse parcel dataset was first filtered to identify parks and schools that met the CAP criteria. A parcel was counted if it's area to length ratio was      greater than 15 to avoid awkwardly long parcels, and if its area was greater than six acres, including in combination with other park or school parcels within    0.25 miles. These criteria align with the size of a neighborhood park suggested by the American Planning Association. 

2. VacantParcels.py
   Identified vacant parcels in Syracuse.
   
3. EnvironmentalRemediationParcels.py
   Identified environmental remediation parcels.
   
4. slice_er_vp.py
   Environmental remediation and vacant parcel data were spatially joined through a union, so that they could be evaluated together in the next script.
   
5. filter_er_vp.py
   Environmental remediation and vacant parcel data was filtered with the same criteria as the Syracuse City parcel dataset to identify potential areas for CAPs.
   The identified potential CAPs are then presented as a list in each neighborhood for the user to explore. 
   
6. Neighborhoods.py
   Lastly, the percentage of land that met CAP criteria was calculated per neighborhood to identify the most under-served neighborhoods in Syracuse. The              filtered environmental remediation and vacant parcel data were then overlayed with the neighborhood boundary to display a map of potential sites. A list of        parcels and their associated neighborhoods to explore as options for a new CAP are provided.

# Inputs
  - Parcel Data
     - Land use codes designating public park space
     - Land use codes to identify vacancy type
     - Assessed value
     - Owner
     - Area
 - Neighborhood Data
     - Boundaries
 -Environmental Remediation Data
     - Owner
     - Clean-Up Type
     - Area
     
# Outputs
The main scripts should produce the following outputs in this order:
 1. aug_park_inventory.png
 2. aug_park_inventory.gpkg
 3. VacantParcels.png
 4. RemediationSites.png
 5. rem_parcel_inventory.gpkg
 6. er_vp_sliced.png
 7. slice_er_vp.gpkg
 8. er_vp_filtered.png
 9. filter_er_vp.gpkg
 10. Potential_CAPs.csv

# Results




