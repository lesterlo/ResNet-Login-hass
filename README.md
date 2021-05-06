# CUHK ResNet Login Service in Home assistant

## Introduction
This home assistant script keeps the CUHK ResNet or WiFi connection persistently. By default, the CUHK ResNet/WiFi has 8 hours timeout on each session. This login service can check the network connection status and re-login the CUHK ResNet/WiFi automatically after the 8 hours timeout.

No network service interruption in your hostel room anymore. :)


## Prerequisites

Please install the [Home Assistant](https://www.home-assistant.io) and [pyscript](https://github.com/custom-components/pyscript) before installing this script.

If you don't have Home Assistant, please use the [CUHK ResNet Login Bot](https://github.com/lesterlo/ResNet-Login-Bot)

## Installation

1. Move the `cuhk_resnet_login.py` into the `<config>/pyscript/apps/`

2. Insert the following setting into `<config>/configuration.yaml`

```
pyscript:
  allow_all_imports: true
  apps:
    cuhk_resnet_login:
      - interval: 50min
        url: "http://securelogin.net.cuhk.edu.hk/cgi-bin/login"
        uid: !secret cuhk_id
        upw: !secret cuhk_pw
```

## Usage

### 1. Polling interval
In the `<config>/configuration.yaml`, you can adjust the polling interval of your connection status on `interval` parameter.

```
# Example
interval: 50min   # For 50 minute
# interval: 1h    # For 1 Hour 
```

### 2. Login URL
In the `<config>/configuration.yaml`, you can modify the login URL for different network connection medium.
```
#For CUHK ResNet
url: "http://securelogin.net.cuhk.edu.hk/cgi-bin/login"

#For CUHK WiFi
url: "http://securelogin.wlan.cuhk.edu.hk/cgi-bin/login"
```

### 3. Login Account& Password

In the `<config>/secrets.yaml`, you need to provides your `CUHK Computer ID` and `CUHK OnePass (CWEM) Password ` for login purpose.

```
cuhk_id: YOUR_COMPUTER_ID
cuhk_pw: YOUR_PASSWORD
```

  
## Reference
https://github.com/lesterlo/ResNet-Login-Bot
