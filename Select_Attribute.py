# Commonly used terms when working with selection

# Feature class: A table contating an attribute field that store geometry that defines shape of a feature
# Feature layer: An in-memory representation of the data in the feature class

# Table: A storage container for rows that contain fields to store Data
# TableView: An in-memory representation of the data in a table

import arcpy
import os
gdb_path = r"D:\Programming for GIS-3\P4_Working_With_Selection\ProProject_Selections\ProProject_Selections.gdb"
restaurant_fc_name = "Wilson_Restaurants"

restaurant_fc_path = os.path.join(gdb_path, restaurant_fc_name)

# Converting a feature class into a feature layer
arcpy.management.MakeFeatureLayer(restaurant_fc_path, "restaurant_lyr")

# Getting count of all the feature before applying selection
pre_count = arcpy.GetCount_management("restaurant_lyr")
print("The Count of restaurant before applying selection is {}".format(pre_count[0]))

# Applying Select by Attribute to get the restaurant serving alcohol
arcpy.management.SelectLayerByAttribute("restaurant_lyr", "NEW_SELECTION", "ALCOHOL = 1")

# Getting count of selection
post_count = arcpy.GetCount_management("restaurant_lyr")
print("The Count of restaurant before applying selection is {}".format(post_count[0]))

output_alcohol_restaurants = "Wilson_Restaurant_Alcohol"
output_alcohol_restaurants_path = os.path.join(gdb_path, output_alcohol_restaurants)

# Converting the feature layer to feature Class (only selected features will be saved
arcpy.management.CopyFeatures("restaurant_lyr",output_alcohol_restaurants_path)

print("Process Completed")
