# cm-rgb
[![Version](https://img.shields.io/pypi/v/cm-rgb?style=for-the-badge)](https://pypi.org/project/cm-rgb/)
[![Licence](https://img.shields.io/github/license/gfduszynski/cm-rgb?color=blue&style=for-the-badge)](https://github.com/gfduszynski/cm-rgb/)
[![Downloads](https://img.shields.io/pypi/dm/cm-rgb?&style=for-the-badge)](https://github.com/gfduszynski/cm-rgb/)
[![PayPal](https://img.shields.io/badge/PayPal-3$-1abc9c.svg?style=for-the-badge)](https://www.paypal.me/gfduszynski/3USD)


### Control your Wraith Prism RGB on Linux, Mac OS and Windows

![Picutre](https://github.com/gfduszynski/cm-rgb/raw/master/cm-rgb-monitor.gif)

**cm-rgb-monitor** _showing realtime cpu utilization._


## Getting started
### Installation & Configuration

Follow [this simple guide on our wiki.](https://github.com/gfduszynski/cm-rgb/wiki/Installation-&-Configuration)

### Usage

Included there is a sample script that allows for displaying cpu utilization with ring LED's.
```
cm-rgb-monitor --cpu-color=#FFA500 --bg-color=#00FFFF
```
The monitoring script can also display sensor values (e.g. CPU temperature) using the fan color.
```
cm-rgb-monitor --cpu-color=#FFA500 --bg-color=#00FFFF --show-temp --low-color=#00FF00 --high-color=#FF0000
```
Requires _lm-sensor_ installed and configured and a python wrapper for it called _pysensors_.


Example of CLI usage
```
cm-rgb-cli set logo --mode=breathe --color=#00ff00 --speed=3 --brightness=5 fan --mode=breathe --color=#0000ff --speed=4 --brightness=1 ring --mode=swirl --color=#ff0000 --speed=1 --brightness=1
```

In order to make settings persistent append ``save``

```
cm-rgb-cli set logo --mode=breathe --color=#00ff00 --speed=3 --brightness=5 fan --mode=breathe --color=#0000ff --speed=4 --brightness=1 ring --mode=swirl --color=#ff0000 --speed=1 –brightness=1 save
```

You can also restore previously saved settings by running
```
cm-rgb-cli restore
```

If LED lights disgust you, use this to turn them off.
```
cm-rgb-cli set logo --mode=off save
```

Check help for details on each command
```
cm-rgb-cli set logo --help
```

Much more flexibility is achievable by using the library directly instead of CLI.
All of the 15 LED’s on the ring are available to mess with.

### Licence

**MIT** 

See LICENCE file for details


