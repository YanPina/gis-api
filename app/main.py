import uvicorn
from fastapi import FastAPI, Request

from scripts.gisOperations import *
from scripts.dataConstrutor import *

app = FastAPI()

raster = RasterData()._data()


@app.post("/point-intersection")
async def point_intersection(data:Request):
    json_data = await data.json()
    json_data = JsonToGeoDataFrame(points=json_data)._data()

    intersection = Intersection(geodataframe1=json_data, geodataframe2=raster)._intersection()

    return GeoDataFrameToJson(geodataframe=intersection)._json()


@app.post("/buffer")
async def buffer(data:Request):

    json_data = await data.json()
    json_data = JsonToGeoDataFrame(points=json_data)._data()

    buffer_geometry = Buffer(geodataframe=json_data, area_buffer=0.0005)._buffer_area()
    
    return GeoDataFrameToJson(geodataframe=buffer_geometry)._json()


if __name__ == "__main__":
    uvicorn.run(app, port=8000, host="0.0.0.0")
    