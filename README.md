# LAB 1: GEOPROCESSING IN ARCGIS
Author: Claire Morehouse
Due: 23 OCT 2020

## Lab Description
This repository contains two scripts that each execute different geoprocesssing mechanisms in ArcMap using Python 3. The flooding script was creating by converting a Model built in ArcMap to Python Script. The script takes the shapefiles of floodzones and basin, and clips the floodzones using basin as a "cookie-cutter", and then from that clipped shaped, selects Special Flood Hazard Areas. The final output is a shapefile of the Special Flood Hazard Areas in the clipped floodzone areas. The my_clip script as written in Python, and creates a workspace in the Lab 1 Geoprocessing folder, and then clips the lake shapefile using basins as the "cookie-cutter". The final output is lake_myclip, which is a clipped version of lakes. 

Below is an image of the clipped lake shapefile that is the final output of my_clip. 

You will submit two scripts, one screenshot, and a short (150 – 250 word) write up as your README file. Be sure to read the lab sheet carefully since it explains which scripts you need to save! Specifically, your repo should include: 
- `file.flooding.py` from part 2
- `my_clip.py` from part 3, and 
- an image of the lakes_myClip layer from part 3. If you don't know how to add an image to your Github readme you can [view this video](https://www.youtube.com/watch?reload=9&v=hHbWF1Bvgf4) or [see the instructions at the bottom of this readme](https://github.com/Shadrock/code-snippets).

Your read me should explain briefly what you did in the lab and clearly list the contents of the repo and explain what it is so that someone who is not in the class can look at your repo and understand both the lab and the outputs. In example, “file.flooding.py is a Python script for use in ArcMap. The script takes some inputs and then outputs something else…” For guidance on things you should include in your readme, or how to structure it nicely using markdown, [see this web page](https://www.makeareadme.com/). 
