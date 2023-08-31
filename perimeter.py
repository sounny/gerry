# -*- coding: utf-8 -*-

import arcpy

def Model41():  # Perimeter Model

    # To allow overwriting outputs change overwriteOutput option to True.
    arcpy.env.overwriteOutput = False

    arcpy.ImportToolbox(r"c:\program files\arcgis\pro\Resources\ArcToolbox\toolboxes\Data Management Tools.tbx.tbx")
    districts001_2_ = "districts001"

    # Process: Add Geometry Attributes (Add Geometry Attributes) (management)
    districts001 = arcpy.management.AddGeometryAttributes(Input_Features=districts001_2_, Geometry_Properties=["PERIMETER_LENGTH_GEODESIC"], Length_Unit="METERS", Area_Unit="", Coordinate_System="")[0]

if __name__ == '__main__':
    # Global Environment settings
    with arcpy.EnvManager(scratchWorkspace=r"c:\research.gdb"):
        Model41()

