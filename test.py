import asyncio
import sys
from argparse import ArgumentParser
from os import getenv

from owmpy.current import CurrentWeather
from owmpy.utils import StandardUnits, Units, convert_temp

argparser = ArgumentParser()
argparser.add_argument("lat", type=float, default=0)
argparser.add_argument("lon", type=float, default=0)
argparser.add_argument("--token", type=str, default=None)
args = argparser.parse_args()


async def main():
    # Get a weather token from openweathermap.org
    appid = args.token or getenv("CURRENT_WEATHER_TOKEN")
    if not appid:
        raise RuntimeError("CURRENT_WEATHER_TOKEN is not set")

    async with CurrentWeather(appid=appid) as weather:
        degrees = (args.lat, args.lon)
        response = await weather.get(degrees, units=StandardUnits.METRIC)

        for name in ["metric", "standard", "imperial"]:
            units: Units = getattr(StandardUnits, name.upper())
            temp = convert_temp(response.main.temp, response.units, units)
            print(name.title() + ": \t", round(temp, 2), units.temp[0], sep="")
        print("Reached end of program Flow")


if __name__ == "__main__":
    resp = asyncio.run(main(), debug=True)
