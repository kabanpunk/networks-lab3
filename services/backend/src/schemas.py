from dataclasses import dataclass
from datetime import datetime

from dataclasses_json import dataclass_json

from pydantic import BaseModel, Json, Field
from typing import Optional, List, Dict, Union

"""
Data schemas for https://graphhopper.com/ API
"""


@dataclass_json
@dataclass
class Point:
    lng: float
    lat: float


@dataclass_json
@dataclass
class Hit:
    point: Point
    osm_id: str
    osm_type: str
    osm_key: str
    name: str
    country: str
    city: Union[str, None] = None
    state: Union[str, None] = None
    street: Union[str, None] = None
    housenumber: Union[str, None] = None
    postcode: Union[str, None] = None


@dataclass_json
@dataclass
class GeoCodeOut:
    hits: List[Hit]
    took: Union[int, None] = None


@dataclass_json
@dataclass
class GeoCodeQuery:
    q: str
    locale: Union[str, None] = None
    limit: Union[int, None] = None
    reverse: Union[bool, None] = None
    debug: Union[bool, None] = None
    point: Union[str, None] = None
    provider: Union[str, None] = None


"""
Data schemas for https://openweathermap.org/ API
"""


@dataclass_json
@dataclass
class WeatherQuery:
    lat: float
    lon: float
    mode: Union[str, None] = None
    units: Union[str, None] = None
    lang: Union[str, None] = None


@dataclass_json
@dataclass
class Coord:
    lat: float
    lon: float


@dataclass_json
@dataclass
class Weather:
    id: int
    main: str
    description: str
    icon: str


@dataclass_json
@dataclass
class Main:
    temp: float
    feels_like: float
    temp_min: float
    temp_max: float
    pressure: Union[int, None] = None
    humidity: Union[int, None] = None
    sea_level: Union[int, None] = None
    grnd_level: Union[int, None] = None


@dataclass_json
@dataclass
class Wind:
    speed: float
    deg: int
    pressure: Union[float, None] = None


@dataclass_json
@dataclass
class Clouds:
    all: int


@dataclass_json
@dataclass
class Sys:
    country: str
    sunrise: int
    sunset: int
    type:  Union[int, None] = None
    id:  Union[int, None] = None
    message: Union[str, None] = None


@dataclass_json
@dataclass
class WeatherOut:
    coord: Coord
    weather: List[Weather]
    base: str
    main: Main
    visibility: int
    wind: Wind
    clouds: Clouds
    dt: int
    sys: Sys
    timezone: int
    id: int
    name: str
    cod: str
    rain: Union[dict, None] = None
    snow: Union[dict, None] = None
