## Control your Wraith Prism RGB without bloatware on Linux
![Picutre](https://github.com/gfduszynski/cm-rgb/raw/master/IMG_2521.JPG)

### Installation
```
pip install cm-rgb
```

### Configuration

Script must have access to USB device to function properly.
It would be wise not to run this as root.
NOTE: I’m running this as root.

### Usage


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

