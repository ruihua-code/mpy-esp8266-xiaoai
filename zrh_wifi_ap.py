import network
from zrh_web_server import do_socket_start


# 创建wifi热点，ssid=ESP-AP password=esp123456
def init_ap():
    ap = network.WLAN(network.AP_IF)
    ap.active(True)
    ap.config(essid='ESP-AP', authmode=network.AUTH_WPA_WPA2_PSK,
              password='esp123456')

    print('--- AP热点启动成功 ---')
    print(ap.ifconfig())
    print('--- AP web服务启动 ---')
    do_socket_start()
