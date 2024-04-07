import asyncio
from argparse import ArgumentParser
from os import getenv

from dotenv import load_dotenv

from owmpy import current
from owmpy.utils import StandardUnits, Units, convert_temp


argparser = ArgumentParser()
argparser.add_argument("lat", type=float)
argparser.add_argument("lon", type=float)
argparser.add_argument("--token", type=str, default=None)
args = argparser.parse_args()


async def main() -> None:
    load_dotenv()
    # Get a weather token from openweathermap.org
    appid = args.token or getenv("CURRENT_WEATHER_TOKEN")
    if not appid:
        raise RuntimeError("CURRENT_WEATHER_TOKEN is not set")

    async with current.Client(appid) as weather:
        degrees = (args.lat, args.lon)
        response = await weather.get(degrees, units=StandardUnits.METRIC)

        for name in ["METRIC", "STANDARD", "IMPERIAL"]:
            units: Units = getattr(StandardUnits, name)
            temp = convert_temp(response.main.temp, response.units, units)
            print(name.title() + ": \t", round(temp, 2), units.temp[0], sep="")
        print("Reached end of program Flow")


if __name__ == "__main__":
    resp = asyncio.run(main(), debug=True)
