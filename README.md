# cm-rgb
[![Version](https://img.shields.io/pypi/v/cm-rgb?style=for-the-badge)](https://pypi.org/project/cm-rgb/)
[![Licence](https://img.shields.io/github/license/gfduszynski/cm-rgb?color=blue&style=for-the-badge)](https://github.com/gfduszynski/cm-rgb/)
[![Downloads](https://img.shields.io/pypi/dm/cm-rgb?&style=for-the-badge)](https://github.com/gfduszynski/cm-rgb/)
[![PayPal](https://img.shields.io/badge/PayPal-3$-1abc9c.svg?style=for-the-badge)](https://www.paypal.me/gfduszynski/3USD)


### Control your Wraith Prism RGB on Linux, Mac OS and Windows

## Screenshots
![Picture](https://github.com/groovykiwi/cm-rgb-gui/raw/master/gui-ss.png)

## cm-rgb-gui
A GUI interface that serves the purpose of simplifying the usage of [cm-rgb](https://github.com/gfduszynski/cm-rgb) by gfduszynski.

### How to use
1. Install cm-rgb following the guide listed below

2. Download the cm-rgb-gui script [here](https://github.com/groovykiwi/cm-rgb-gui/raw/master/cm-rgb-gui)

3. Run ```sudo cm-rgb-gui``` in whichever directory the script is located (if it is not run with sudo the changes will not be applied). Optionally put in in one of your PATH folders for easy access.

All applied changes are automatically persistent.
To disable a specific component just leave the color field blank or set it to pure black (#000000).

## Getting started
### Installation & Configuration

Follow [this simple guide on our wiki.](https://github.com/gfduszynski/cm-rgb/wiki/1.-Installation-&-Configuration)

### Usage

Package comes with two scripts ``cm-rgb-cli`` and ``cm-rgb-monitor``.  

``cm-rgb-cli`` allows for fine grained control of each individual zone including [turning off the LED's](https://github.com/gfduszynski/cm-rgb/wiki/2.-CLI-usage#3-turning-all-zones-off) completely.

Check out the [examples in our wiki](https://github.com/gfduszynski/cm-rgb/wiki/2.-CLI-usage).

``cm-rgb-monitor`` allows for displaying cpu utilization with ring LED's, along with temperature (thanks to [mpsdskd](https://github.com/mpsdskd)).

Combining the cli + monitor can create neat transition from powering your system right to booting your OS.

Check out the [examples in our wiki](https://github.com/gfduszynski/cm-rgb/wiki/3.-Monitor-usage).

## Licence

**MIT** 

See LICENCE file for details
