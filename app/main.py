import uvicorn
from fastapi import FastAPI

from gisOperations import *
from dataConstrutor import PointToGeoDataFrame, GeoDataFrameToJson

from pydantic import BaseModel


class PointBuffer(BaseModel):
    lat: float
    long: float
    area_buffer:float


app = FastAPI()

@app.get("/")
async def main():
    return {"message": "Hello World"}


@app.post("/buffer")
async def buffer(point_buffer:PointBuffer):

    point_geodataframe = PointToGeoDataFrame(lat=point_buffer.lat, long=point_buffer.long)._make_geodataframe()

    buffer_geometry = Buffer(geodataframe=point_geodataframe, area_buffer=point_buffer.area_buffer)._buffer_area()
    
    return GeoDataFrameToJson(geodataframe=buffer_geometry)._json()


if __name__ == "__main__":
    uvicorn.run(app, port=8000, host="0.0.0.0")
    