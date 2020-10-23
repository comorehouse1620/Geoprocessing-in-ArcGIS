# Name: YOUR NAME HERE 
# Python Version: ENTER ASSIGNMENT TITLE HERE.
# Description: ENTER A DESCRIIPTION ABOUT WHAT YOUR CODE IS SUPPOSED TO DO HERE: DESCRIBE INPUTS / OUTPUTS.

Leave the lines of comment code, above, but add your personal details. Then replace these two lines of code with your new code! 
'''
Author: Claire Morehouse
Data: Lab 1 Geoprocessing, Using Python 3
Description: Writing a script for lab 1 that clips the shape file using basing
'''

import arcpy
#Set Workspace
arcpy.env.workspace = "C:\Users\CMorehouse\Desktop\compprog\Lab_1_Geoprocessing_ArcGIS"
#Clip, save in results folder
arcpy.Clip_analysis("Data_Lab_1_Geoprocessing_ArcGIS/lakes.shp","Data_Lab_1_Geoprocessing_ArcGIS/basin.shp","Results/lake_myClip.shp")
                    
