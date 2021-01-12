import arcpy
from datetime import datetime
import os
import shutil
import Setup
import pandas as pd

arcpy.env.workspace = Setup.process_folder
arcpy.env.overwriteOutput = True


def filter_data():
    print 'Removing False cases based on LULC'

    in_boundary = os.path.join(os.getcwd(), 'backup\India_Subdistrict_06.shp')
    in_lulc = os.path.join(os.getcwd(), 'backup\HR_LULC_Multi.shp')

    print 'filtering data based on LULC'
    list = os.listdir(Setup.input_folder)
    for file in list:
        if file.endswith(".shp"):
            print("Processing ..." + file)
            in_fire = os.path.join(Setup.input_folder, file)
            try:
                arcpy.MakeFeatureLayer_management(in_fire, 'fire')
                arcpy.FeatureClassToFeatureClass_conversion('fire', Setup.process_folder, 'fire_location')

                arcpy.Clip_analysis('fire_location.shp', in_boundary, 'Haryana_fire_location.shp')

                arcpy.SpatialJoin_analysis('Haryana_fire_location.shp', in_lulc, 'Haryana_LULC_fire.shp')
                arcpy.MakeFeatureLayer_management('Haryana_LULC_fire.shp', 'Haryana_LULC')
                arcpy.SelectLayerByAttribute_management('Haryana_LULC', "NEW_SELECTION", "gridcode=2")
                points = "Haryana_Active_fire" + file
                arcpy.FeatureClassToFeatureClass_conversion('Haryana_LULC', Setup.output_folder, points)

                feature_class = os.path.join(Setup.output_folder, points)
                arr = arcpy.da.FeatureClassToNumPyArray(feature_class, ['latitude', 'longitude'])
                df = pd.DataFrame(arr, columns=['latitude', 'longitude'])

                csv_file = os.path.join(Setup.output_folder, 'fire.csv')
                df.to_csv(csv_file, index=False)

            except OSError as e:
                print e
