# csssprite
A simple Python utility for merging images into a sprite with accompanying CSS

- [Kailash Nadh](http://nadh.in), June 2013
- License: GPL v2
- [PyPi](https://pypi.python.org/pypi/csssprite)

## Installation
With pip or easy_install

```pip install csssprite``` or ```easy_install csssprite```

or from source

```python setup.py install```

## Usage
Once the package is installed, the commandline utility ```csssprite``` should become available system wide

```csssprite --in "./images" --out "./"" --name "buttons"```

Arguments
```
--in		path to directory containing images
--out		path to the directory where image+css should be generated
--name		name of the output image and layer id in the css (default=sprite)
--orientation	orientation of sprites. horizontal or vertical (default)
--spacing		distance between individual tiles (default=30)
--filetype		image filetype (default=png)
```