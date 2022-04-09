import asyncio
import sys
from os import getenv

from owmpy.current import CurrentWeather
from owmpy.utils import StandardUnits, convert_temp


async def main():
    # Get a weather token from openweathermap.org
    async with CurrentWeather(appid=getenv("CURRENT_WEATHER_TOKEN")) as weather:
        dft = [0]
        lat = int((sys.argv[1:2] or dft)[0])
        lon = int((sys.argv[2:3] or dft)[0])

        response = await weather.get((lat, lon), units=StandardUnits.METRIC)

        print(response)

        print(
            f"Metric: {convert_temp(response.main.temp, response.units, StandardUnits.METRIC)}{StandardUnits.METRIC.temp[0]}"
        )
        print(
            f"Kelvin: {convert_temp(response.main.temp, response.units, StandardUnits.STANDARD)}{StandardUnits.STANDARD.temp[0]}"
        )
        print(
            f"Cringe: {convert_temp(response.main.temp, response.units, StandardUnits.IMPERIAL)}{StandardUnits.IMPERIAL.temp[0]}"
        )


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main())
