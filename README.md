## Control your Wraith Prism RGB without bloatware on Linux
![Picutre](https://github.com/gfduszynski/cm-rgb/raw/master/cm-rgb-demo.jpg)
![Picutre](https://github.com/gfduszynski/cm-rgb/raw/master/cm-rgb-monitor.gif)

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

NOTE: I’m running this as root.

### Usage

Included there is a sample script that allows for displaying cpu utilization with ring LED's.
```
cm-rgb-monitor --cpu-color=#FFA500 --bg-color=#00FFFF
```


```
cm-rgb-cli logo --mode=breathe --color=#00ff00 --speed=3 --brightness=5 fan --mode=breathe --color=#0000ff --speed=4 --brightness=1 ring --mode=swirl --color=#ff0000 --speed=1 --brightness=1
```

In order to make settings persistent append ``save``

```
cm-rgb-cli logo --mode=breathe --color=#00ff00 --speed=3 --brightness=5 fan --mode=breathe --color=#0000ff --speed=4 --brightness=1 ring --mode=swirl --color=#ff0000 --speed=1 –brightness=1 save
```

You can also restore previously saved settings by running
```
cm-rgb-cli restore
```

If LED lights disgust you, use this to turn them off.
```
cm-rgb-cli logo --mode=off save
```

Check help for details on each command
```
cm-rgb-cli logo --help
```

Much more flexibility is achievable by using the library directly instead of CLI.
All of the 15 LED’s on the ring are available to mess with.

### Licence

**MIT** 

See LICENCE file for details

### Donations
If this works for you and you like it feel free to buy me a beer :)

[![Support via PayPal](https://cdn.rawgit.com/twolfson/paypal-github-button/1.0.0/dist/button.svg)](https://www.paypal.me/gfduszynski/)

