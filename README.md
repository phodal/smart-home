# smart-home

ESP8266 仿真 Wemo
---


安装 Arduino ESP8266 [https://github.com/esp8266/Arduino](https://github.com/esp8266/Arduino)

Arduino Esp8266 Alexa Wemo switch emulator https://github.com/witnessmenow/esp8266-alexa-wemo-emulator

Raspberry Pi Home Assistant
---

Images: [https://home-assistant.io/docs/hassbian/installation/](https://home-assistant.io/docs/hassbian/installation/)

Images Downloader: [https://etcher.io/](https://etcher.io/)


文档有问题。233 

https://home-assistant.io/docs/installation/virtualenv/

```
pip3 install --upgrade homeassistant
```

运行

```
sudo -u homeassistant -H /srv/homeassistant/bin/hass
```

并不没工作，233

```
curl -O https://raw.githubusercontent.com/home-assistant/fabric-home-assistant/master/hass_rpi_installer.sh && sudo chown pi:pi hass_rpi_installer.sh && bash hass_rpi_installer.sh
```

在我的 MBP 上安装尝试

```
pip3 install homeassistant
hass --open-ui
```

LICENSE
---

MIT
