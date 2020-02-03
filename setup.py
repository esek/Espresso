# Denna fil är endast till för att det ska gå att installera grejen.
from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_descritiption = fh.read()

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
    author_email='macapar@esek.se',
    description='The best damn coffee-counter there ever was',
    long_description=long_descritiption,
    long_description_content_type="text/markdown",
    url="https://github.com/esek/espresso",
    packages=find_packages(),
    entry_points={  # Tells pipx what to do
        "console_scripts": [
            "espresso=espresso.__main__:main"   # Must be underscore
        ]
    },
    install_requires=[      # Uppdatera med nya libraries/moduler som krävs
         
      ],
)