# Denna fil är endast till för att det ska gå att installera grejen.
from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='espresso',
    version='0.0.1a', # Uppdatera innan push
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
            "espresso = espresso.espresso:main",   # Pekar så att när vi installerat programmet via pip så körs main() i espresso.py om vi skriver espresso i terminalen "Vi har ett script espresso som kör main-metoden i espresso.py i espresso"
        ]
    },
    install_requires=[      # Uppdatera med nya libraries/moduler som krävs
         'pyodbc',  # För hantering av SQL
      ],
)