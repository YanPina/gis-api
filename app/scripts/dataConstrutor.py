import os
import json

import pandas as pd
import geopandas as gpd

from scripts.gisOperations import *


class PointToGeoDataFrame:
    def __init__(self, lat:list, long:list) -> None:
        self.lat = lat
        self.long = long


    def _make_geodataframe(self) -> gpd.GeoDataFrame:
        df = pd.DataFrame(
            {
                'lat': self.lat,
                'long': self.long
            }
        )

        return gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df["long"], df["lat"]))


class GeoDataFrameToJson:
    def __init__(self, geodataframe:gpd.GeoDataFrame) -> None:
        self.geodataframe = geodataframe

    def _json(self):
        return json.loads(self.geodataframe.to_json())
    

class RasterData:
    def __init__(self) -> None:
        self.folder_project = os.getcwd()
        self.folder_raster = f"{self.folder_project}/app/data/raster"

    
    def _data(self) -> gpd.GeoDataFrame:
        data = gpd.GeoDataFrame(gpd.read_file(f"{self.folder_raster}/raster_polygon.shp"))
        data = data.rename(columns={"DN": "elevation"})

        return ReprojectGeometries(geodataframe=data, to="4326")._reproject()
    

class JsonToGeoDataFrame:
    def __init__(self, points:dict) -> None:
        self.points = points

    def _data(self) -> gpd.GeoDataFrame:
        return gpd.GeoDataFrame.from_features(self.points['features'])
    