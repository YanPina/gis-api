import pandas as pd
import geopandas as gpd

class PointToGeoDataFrame:
    def __init__(self, lat:float, long:float) -> None:
        self.lat = lat
        self.long = long


    def _make_geodataframe(self) -> gpd.GeoDataFrame:
        df = pd.DataFrame(
            {
                'lat': [self.lat],
                'long': [self.long]
            }
        )

        return gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df["long"], df["lat"]))


class GeoDataFrameToJson:
    def __init__(self, geodataframe:gpd.GeoDataFrame) -> None:
        self.geodataframe = geodataframe

    def _json(self):
        return self.geodataframe.to_json()