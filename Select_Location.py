import arcpy
import os

gdb_path = r"D:\Programming for GIS-3\P4_Working_With_Selection\ProProject_Selections\ProProject_Selections.gdb"
restaurant_fc_name = "Wilson_Restaurants"
hist_fc_name = "Wilson_Histdist"

restaurant_fc_path = os.path.join(gdb_path, restaurant_fc_name)
hist_fc_path = os.path.join(gdb_path, hist_fc_name)

# Converting a feature class into a feature layer
arcpy.management.MakeFeatureLayer(restaurant_fc_path, "restaurant_lyr")
arcpy.management.MakeFeatureLayer(hist_fc_path, "hist_dist_lyr")


# Getting count of all the feature before applying selection
pre_count = arcpy.GetCount_management("restaurant_lyr")
print("The Count of restaurant before applying selection is {}".format(pre_count[0]))

arcpy.management.SelectLayerByLocation("restaurant_lyr", "WITHIN_A_DISTANCE", "hist_dist_lyr", "500 feet")

post_count = arcpy.GetCount_management("restaurant_lyr")
print("The Count of restaurant within 500 feet of histdist is {}".format(post_count[0]))

output_restaurants_histdist = "Restaurant_within_500feet"
output_restaurants_histdist_path = os.path.join(gdb_path, output_restaurants_histdist)

arcpy.management.CopyFeatures("restaurant_lyr", output_restaurants_histdist_path)
print("Process Completed")
