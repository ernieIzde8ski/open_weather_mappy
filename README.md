# Open Weather Mappy

A wrapper for the [Open Weather Map API](https://openweathermap.org/api).

## Installation

`pip install owmpy`

## Usage

Import the class and make requests.

```py
import asyncio
from os import getenv

from owmpy.current import CurrentWeather


async def main():
    # Get a weather token from openweathermap.org
    async with CurrentWeather(appid="YOUR_TOKEN") as weather:
        response = await weather.get((0, 0))
    print(response)


if __name__ == "__main__":
    asyncio.run(main())
```

Optionally, you can supply your own ClientSession:

```py
import aiohttp
weather = CurrentWeather(appid="token", client=aiohttp.ClientSession())
```

## Building

<!-- for when I inevitably forget again -->

```sh
rm -r dist
python -m build
twine upload 'dist/*'
```
