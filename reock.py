# -*- coding: utf-8 -*-

import arcpy
from sys import argv

def Model6(districts001="districts001"):  # Reock

    # To allow overwriting outputs change overwriteOutput option to True.
    arcpy.env.overwriteOutput = False

    arcpy.ImportToolbox(r"c:\program files\arcgis\pro\Resources\ArcToolbox\toolboxes\Data Management Tools.tbx.tbx")

    # Process: Add Geometry Attributes (Add Geometry Attributes) (management)
    districts001_4_ = arcpy.management.AddGeometryAttributes(Input_Features=districts001, Geometry_Properties=["AREA_GEODESIC"], Length_Unit="METERS", Area_Unit="", Coordinate_System="")[0]

    # Process: Minimum Bounding Geometry (Minimum Bounding Geometry) (management)
    districts001_MinimumBounding = fr"{arcpy.env.scratchGDB}\districts001_MinimumBounding1"
    arcpy.management.MinimumBoundingGeometry(in_features=districts001_4_, out_feature_class=districts001_MinimumBounding, geometry_type="CIRCLE", group_option="NONE", group_field=[], mbg_fields_option="NO_MBG_FIELDS")

    # Process: Calculate Geometry Attributes (Calculate Geometry Attributes) (management)
    districts001_MinimumBounding1_2_ = arcpy.management.CalculateGeometryAttributes(in_features=districts001_MinimumBounding, geometry_property=[["AREA_Circle", "AREA_GEODESIC"]], length_unit="", area_unit="SQUARE_METERS", coordinate_system="", coordinate_format="SAME_AS_INPUT")[0]

if __name__ == '__main__':
    # Global Environment settings
    with arcpy.EnvManager(scratchWorkspace=r"\\ict-mc1-fs01.ad.ufl.edu\wvt-ufapps-temp-storage$\UserData\msounnyslitine\Documents\ArcGIS\Packages\Summer Research_1d1a56\p20\summer_research.gdb", workspace=r"\\ict-mc1-fs01.ad.ufl.edu\wvt-ufapps-temp-storage$\UserData\msounnyslitine\Documents\ArcGIS\Packages\Summer Research_1d1a56\p20\summer_research.gdb"):
        Model6(*argv[1:])

