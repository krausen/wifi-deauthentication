# Deauthenticate attack on a nearby WIFI

Perform a [Wifi deauthentication attack](https://en.wikipedia.org/wiki/Wi-Fi_deauthentication_attack). Use with caution and only for educatiuonal purposes ;)

## Requirements
* Wifi network card with support for monitor mode

## Setup virtual environment
```code
virtualenv venv
sudo -s
source venv/bin/activate
pip install -r requirements.txt
```

## Run
`network_interface.py` is a file that perform operations on your network card. As it is the file is dependent on my OS (Ubuntu 20.04.3) at the time of writing.
You might need to edit this file so that it runs the equivalent commands on your OS. Then all you need to do is:

```code
python main.py
```