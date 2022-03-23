import asyncio
from os import getenv

from owmpy.current import CurrentWeather


async def main():
    # Get a weather token from openweathermap.org
    async with CurrentWeather(appid=getenv("WEATHER_TOKEN")) as weather:
        response = await weather.get((0, 0))
        print(response)


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main())
