from enum import Enum
from typing import NamedTuple, Optional, TypedDict

from pydantic import BaseModel
from typing_extensions import NotRequired

from ..utils._types import Number


class _Units(NamedTuple):
    temp: tuple[str, str] = ("K", "Kelvin")
    speed: tuple[str, str] = ("m/s", "meter/sec")

    time = ("unix", "UTC")
    pressure = "hPa"
    cloudiness = "%"
    precipitation = ("mm", "millimeters")
    degrees = ("°", "degrees (meteorological)")


class Units(Enum):
    STANDARD = _Units()
    METRIC   = _Units(temp=("°C", "Celsius"))
    IMPERIAL = _Units(temp=("°F", "Fahrenheit"), speed=("mph", "miles/hour"))


class Coord(BaseModel):
    lat: Number
    """City geo location, latitude"""
    lon: Number
    """City geo location, longitude"""


class Weather(BaseModel):
    id: int
    """Weather condition id. See [here](https://openweathermap.org/weather-conditions#Weather-Condition-Codes-2) for a full list of possibilities."""
    main: str
    """Group of weather parameters (Rain, Snow, Extreme etc.)"""
    description: str
    """Weather condition within the group"""
    icon: str
    """Weather icon id. Icon can be fetched with `http://openweathermap.org/img/wn/{icon}@2x.png`"""


class Main(BaseModel):
    """Do not confuse `temp_min` or `temp_max` with daily lows/highs; see [here](https://openweathermap.org/current#min)"""

    temp: float
    """Temperature"""
    humidity: Number
    """Humidity"""
    feels_like: Number
    temp_min: Number
    """Minimum temperature at the moment. This is deviation from current temp that is possible for large cities and megalopolises geographically expanded (use these parameters optionally)"""
    temp_max: float
    """Maximum temperature at the moment. This is deviation from current temp that is possible for large cities and megalopolises geographically expanded (use these parameters optionally)"""
    pressure: int
    """Atmospheric pressure (on the sea level, if there is no sea_level or grnd_level data)"""
    sea_level: int
    """Atmospheric pressure on the sea level"""
    grnd_level: int
    """Atmospheric pressure on the ground level"""


class Wind(BaseModel):
    deg: int
    """Wind direction"""
    speed: float
    """Wind speed. Differs from wind gust in that it measures instantaneous velocity."""
    gust: float
    """Wind gust. Differs from wind speed in that it measures short bursts in wind."""


class Clouds(BaseModel):
    all: int
    """Cloudiness as a percentage"""


class Sys(BaseModel):
    message: str | None = None
    """System parameter, do not use it"""
    country: Optional[str] = None
    """Country code (GB, JP etc.)"""
    sunrise: int
    """Sunrise time"""
    sunset: int
    """Sunset time"""
    type: Optional[str] = None
    id: Optional[str] = None


class Rain(BaseModel):
    _1h: Number
    _3h: Number


class CurrentWeatherStatus(BaseModel):
    """The weather data served by https://openweathermap.org/current. Most docstrings stolen from there too."""

    id: int
    """City identification"""
    units: Units = Units.STANDARD
    """Units to use. Served by internal API."""
    dt: int
    """Data receiving time"""
    name: str
    """City name"""
    coord: Coord
    """Geographical coordinates"""
    sys: Sys
    """Location data"""
    wind: Wind
    clouds: Clouds
    weather: list[Weather]
    """A list of weather responses. Usually one item."""
    rain: Optional[Rain] = None
    """Rain data. May not exist."""
    base: str
    main: Main
    visibility: int
    timezone: int
    cod: int