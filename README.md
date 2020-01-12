## Control your Wraith Prism RGB on Linux, Mac OS and Windows
![Picutre](https://github.com/gfduszynski/cm-rgb/raw/master/cm-rgb-monitor.gif)

**cm-rgb-monitor** _showing realtime cpu utilization._

### Installation

Make sure you have dev libraries for hidapi.

##### Ubuntu
```
sudo apt-get install python-dev libusb-1.0-0-dev libudev-dev
```

##### Other distros
It's possible you already have what it takes to install pip package so try that.
If you have any problems regarding hidapi installation see: `` https://github.com/trezor/cython-hidapi ``
Your issue may already have a solution there.

If you still have a problem please create an issue :)

##### Finally
Now you can install pip package.
```
pip install cm-rgb
```

### Configuration

Script must have access to USB device to function properly.
It would be wise not to run this as root.

It's now possible to add udev rule by running:
``` 
cm-rgb-cli add-udev-rule
```

It may be required to reload udev for changes to take effect.
Now you should be able to run ``cm-rgb-cli`` without sudo.


### Usage

Included there is a sample script that allows for displaying cpu utilization with ring LED's.
```
cm-rgb-monitor --cpu-color=#FFA500 --bg-color=#00FFFF
```

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

### Donations
If this works for you and you like it feel free to buy me a beer :)

[![Support via PayPal](https://cdn.rawgit.com/twolfson/paypal-github-button/1.0.0/dist/button.svg)](https://www.paypal.me/gfduszynski/)

