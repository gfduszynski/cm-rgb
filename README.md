# cm-rgb-gui
[![Version](https://img.shields.io/pypi/v/cm-rgb?style=for-the-badge)](https://pypi.org/project/cm-rgb/)
[![Licence](https://img.shields.io/github/license/gfduszynski/cm-rgb?color=blue&style=for-the-badge)](https://github.com/gfduszynski/cm-rgb/)
[![Downloads](https://img.shields.io/pypi/dm/cm-rgb?&style=for-the-badge)](https://github.com/gfduszynski/cm-rgb/)
[![PayPal](https://img.shields.io/badge/PayPal-3$-1abc9c.svg?style=for-the-badge)](https://www.paypal.me/gfduszynski/3USD)


### Control your Wraith Prism RGB on Linux, Mac OS and Windows

## Screenshots
![Picture](https://github.com/groovykiwi/cm-rgb-gui/raw/master/screenshot.png)

## cm-rgb-gui
GUI interfaces that serve the purpose of simplifying the usage of [cm-rgb](https://github.com/gfduszynski/cm-rgb) by gfduszynski.

### Prerequisites
* [Python](https://www.python.org/) 3.x (most likely it is already installed)
* [PyGObject](https://wiki.gnome.org/action/show/Projects/PyGObject)

### How to use
1. Install cm-rgb following the guide listed below

2. Download the [cm-rgb-gui](https://raw.githubusercontent.com/groovykiwi/cm-rgb-gui/master/scripts/cm-rgb-gui) and [cm-rgb-monitor-gui](https://raw.githubusercontent.com/groovykiwi/cm-rgb-gui/master/scripts/cm-rgb-monitor-gui) scripts

3. Run ```./cm-rgb-gui``` or ```./cm-rgb-monitor-gui```  in the scripts directory or whererver you saved it (running it with sudo is not neccessary if you added the udev rule). Optionally put the scripts in /usr/bin for easy access.

#### cm-rgb-gui
All applied changes are automatically persistent.  
To disable a specific component just leave the color field blank or set it to pure black (#000000).

#### cm-rgb-monitor-gui
I'm pretty sure this script works exclusively on Linux as it makes use of basic linux commands (sed, cut) and bashism.  
If the **show temperature on fan option** is disabled, the previous color and mode of the fan will remain. Be sure to set it before using cm-rgb-monitor-gui

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
