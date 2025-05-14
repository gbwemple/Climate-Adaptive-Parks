# Climate Adaptive Parks: Closing the Green Space Service Gap in Syracuse, NY

# Abstract
As major metropolitan areas increase in population and climate change brings severe weather changes and extreme heat, the public will require more green space to mitigate the impacts. Large, green spaces can act as climate mitigating spaces for people to recreate in. Access to climate large park space varies throughout Syracuse, NY and has led to neighborhoods that are underserved. This tool has identified the neighborhoods in Syracuse that have the least access to Climate Adaptive Parks (CAP) and has identified areas of land that could potentially serve as a new CAP to bridge the existing service gap. 

# Methods
This analysis used Syracuse city parcel and neighborhood boundary data from Open Data Syracuse and environmental remediation boundary data from NYS GIS Clearinghouse. 

Current CAP space were selected by filtering park and school parcels in Syracuse, NY to meet the following criteria: 
1. An area to length ratio greater than 15 to avoid awkwardly long parcels
2. An area greater than six acres, including in combination with other parcels within 0.25 miles

Potential CAP parcels were selected by spatially joining environmental remediation and vacant parcels through a union and then filtered to the same CAP criteria.

The existing service gap was identified by overlaying the neighborhood boundary and current CAP space identified, then finding the percentage of neighborhood covered by CAP space. Potential CAP spaces were then listed in a CSV file with their respective neighborhood. 

# Scripts
1. current_CAPs.py 
   Identified current CAPs in Syracuse, NY.

2. vacant_parcels.py
   Identified vacant parcels in Syracuse, NY.
   
3. remediation_parcels.py
   Identified environmental remediation parcels in Syracuse, NY.
   
4. potential_CAPs.py
   Identified potential CAPs in Syracuse, NY 
   
5. neighborhoods.py
   Calculated the percentage of land that met CAP criteria per neighborhood to identify the most under-served neighborhoods in Syracuse. Produced a map of current and potential CAPS in each neighborhood.

# Inputs
  - Parcel Data (Open Data Syracuse)
     - Land use codes designating public park or school space
     - Land use codes to identify vacancy type
     - Owner
     - Area
 - Neighborhood Data (Open Data Syracuse)
     - Boundaries
 -Environmental Remediation Data (NYS GIS Clearinghouse)
     - Owner
     - Clean-Up Type
     - Area
     
# Outputs
The main scripts should produce the following outputs in this order:

 1. current_CAP_parcels.png
 2. current_CAP_inventory.gpkg
##
 3. vacant_parcel_inventory.gpkg
##
 4. remediation_parcel_inventory.gpkg
##
 7. potential_CAP_parcels.png
 8. potential_CAP_inventory.gpkg
##
  9. neighborhood_all_CAPs.png
 10. percentages.csv
 11. current_CAPs_neighborhoods.csv
 12. potential_CAPs_neighborhoods.csv


# Results

The following CAP spaces were identified in Syracuse, NY:

![Current CAPs in Syracuse, NY](https://github.com/gbwemple/Climate-Adaptive-Parks/blob/main/Task1_Current-CAP-Inventory/current_CAP_parcels.png?raw=true)

The following potential CAP spaces were identified in Syracuse, NY:

![Potential CAPs in Syracuse, NY](https://github.com/gbwemple/Climate-Adaptive-Parks/blob/main/Task4_Potential-CAP-Inventory/potential_CAP_parcels.png?raw=true)

The following neighborhoods were identified as the most underserviced for large park space; 

![Current and Potential CAPs by Neighborhood in Syracuse, NY](https://github.com/gbwemple/Climate-Adaptive-Parks/blob/main/Task5_Neighborhoods/neighborhoods_all_CAPs.png?raw=true)


# Future Applications
This tool can be applied to another city with parcel data to identify current CAP spaces using current_CAPs.py, and changing field names used for filtering. It can also be applied using neighborhoods.py, and removing the potential CAP section, to identify underserved neighborhoods.


# Conclusion
Identifying areas of cities that lack access to sufficient climate adaptive green spaces can promote accessibility to the outdoors, mitigate climate change and the urban heat island effect, and promote equity. Investments in increasing the amount of green spaces in communities must be carried out thoughtfully to ensure all can experience the mental, physical, and monetary benefits from living close to a park. It is of the best interest for local, state, and federal governments to invest resources into urban green spaces because they have the opportunity to convert current land use designations that are less costly and the damage withstood from the lack of current climate change risk mitigation will continue to increase and affect communities in need of climate adaptive spaces. 


