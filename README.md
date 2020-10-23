# LAB 1: GEOPROCESSING IN ARCGIS
Author: Claire Morehouse

Due: 23 OCT 2020

## Lab Description
This repository contains two python scripts that geoprocess in ArcMap 10.7. ArcMap is an ArcGIS ESRI Geographic Information Systems software. The first script is called flooding.py. The flooding script was creating by converting a Model built in ArcMap to Python Script. You can build a Model in ArcMap by creating a Model The script takes the shapefiles of floodzones and basin, and clips the floodzones using basin as an empty toolbox in the ArcCatalog window in ArcMap and then creating a model. The flooding model executes a clip, a type of extraction geoprocessing tool, and Select. In the flooding script, the shapefile basin is a "cookie-cutter" of the shapefile floodzones, and when it is clipped a new shapefile of just the extracted parts of floodzones is created. Then from that clipped shapefile, the script then selects Special Flood Hazard Areas. The final output is a shapefile of the Special Flood Hazard Areas in the clipped floodzone areas. The my_clip script was written in Python, and the final output is also a clipped shapefile. The script starts by creating a workspace in the Lab 1 Geoprocessing folder, and then clips the lake shapefile using basins as the "cookie-cutter". The final output is lake_myclip, which is a clipped version of lakes. 

Below is an image of the clipped lake shapefile that is the final output of my_clip. 

![](images/lakes.png)
