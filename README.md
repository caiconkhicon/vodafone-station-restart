# vodafone-station-restart

## Introduction

This is a simple Python script which uses Selenium to access the Vodafone Station web UI and restart the station.

I write this script because my Vodafone cable Internet is SO BAD. It drops the Internet connection everyday, and the solution is to restart it. I do not know how good it work for different versions of the Vodafone Station. My hardware (in Germany) ID is `TG3442DE`.

## Requirements

* Python3
* Selenium
* Pythonping

```bash
sudo pip3 install selenium pythonping
```

* Google Chrome or Chromium
* Chromedriver

* Go to <https://chromedriver.chromium.org/downloads> and download the version corresponding to your Chrome/Chromium version

## Usage

* Create file `config.cfg` from `config.cfg.example`

```bash
cp config.cfg.example config.cfg
```

* Fill in `config.cfg`
* The script pings Google DNS at `8.8.8.8` 5 times, and if it gets timeouts more than 2 times, it will restart the station using Selenium.

* It should be ran as a Cron Job every minute.

## Limitations

* Since the script uses `ping`, it requires to be ran as `root`.
* The script does not handle the situations such as `No route to host`; or `Cannot resolve address` - if you ping something other than Google DNS.
