'''
Author: Claire Morehouse
Lab: Geogrocessing with ArcGIS, Python 3
Description: This script creates a model in ArcMap that clips the floodzones based
on the basin shapefile i.e. the basin is the "cookie-cutter of the floodzones.
The model then from the clipped layer selects Special Flood Zone areas for
the final output of the shapefile called flooding. 
'''

# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# flooding2.py
# Created on: 2020-10-22 20:17:08.00000
#   (generated by ArcGIS/ModelBuilder)
# Description: 
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy


# Local variables:
floodzones = "floodzones"
basin = "basin"
flood_clip_shp = "C:\\Users\\CMorehouse\\Desktop\\compprog\\Lab_1_Geoprocessing_ArcGIS\\Results\\flood_clip.shp"
flooding_shp = "C:\\Users\\CMorehouse\\Desktop\\compprog\\Lab_1_Geoprocessing_ArcGIS\\Results\\flooding.shp"

# Process: Clip
arcpy.Clip_analysis(floodzones, basin, flood_clip_shp, "")

# Process: Select
arcpy.Select_analysis(flood_clip_shp, flooding_shp, "\"SFHA\" = 'IN'")

