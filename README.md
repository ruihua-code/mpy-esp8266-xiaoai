### esp8266 连接小米小爱同学

使用mpy官方固件：https://www.micropython.org/download/?port=esp8266


### 固件烧入
```
# 擦除固件
esptool.py --port /dev/cu.usbserial-1140 erase_flash

# 刷入固件
esptool.py --port /dev/cu.usbserial-1140 --baud 115200  write_flash -fm qio -fs detect 0 ESP8266_GENERIC-20240105-v1.22.1.bin
```

### 程序代码上传
```
ampy -b 115200 -p com7 -d 1 put .\main.py
ampy -b 115200 -p com7 -d 1 put .\zrh_storage.py
ampy -b 115200 -p com7 -d 1 put .\zrh_web_server.py
ampy -b 115200 -p com7 -d 1 put .\zrh_wifi_ap.py
ampy -b 115200 -p com7 -d 1 put .\zrh_wifi.py
```