# Denna fil är endast till för att det ska gå att installera grejen.
from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='espresso',
    version='0.0.1',
    author=[
        'Ludvig Liftig',
        'Tom Andersson',
        'Fabian Sondh',
        'Johannes Larsson',
        'Jonathan Benitez',
        'Emil Jonathan Eriksson',
    ],
    author_email='macapar@esek.se',     # Well isch
    description='The best damn coffee-counter there ever was',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/esek/espresso",
    packages=find_packages(),
    entry_points={  # Detta avgör vad som kör programmet när det installerats av pip. typ.
        "console_scripts": [
            "espresso=espresso.__main__:main"   # Ändra om strukturen ändras så att __main__ inte är huvudfil.
        ]
    },
    install_requires=[      # Uppdatera med nya libraries/moduler som krävs
         'pyodbc',  # För hantering av SQL
      ],
)