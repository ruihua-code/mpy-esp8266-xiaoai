from time import sleep
import network
from zrh_storage import read_config
from zrh_wifi_ap import init_ap


def do_connect():
    # 使用域名方式访问（esp.local）
    # wlan.config(dhcp_hostname=hostname)

    # network.hostname("zrh-8266")
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)

    if not wlan.isconnected():
        print('--- 开始连接网格 ---')
        try:
            wifiConfig = read_config()
            if wifiConfig != None:
                print("wifiConfig:", wifiConfig)
                wlan.connect(wifiConfig[0], wifiConfig[1])
            else:
                init_ap()

        except OSError as e:
            print("读取wifi配置信息失败")

        connTimeOut = 0
        while not wlan.isconnected():
            print("连接失败，正在重新连接...")
            sleep(1)
            connTimeOut += 1
            # 连接网络10秒超时
            if (connTimeOut >= 10):
                print("--- 连接超时 ---")
                break
        if wlan.isconnected():
            print('连网成功:', wlan.ifconfig())
        else:
            print("连接失败了,开启ap模式")
            init_ap()
