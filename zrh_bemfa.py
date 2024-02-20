from time import sleep
from micropython import const
import machine
from machine import Timer
from umqtt.simple import MQTTClient


clientID = const('11dd1fbc5cbe353fafdc955210933b87')
leddeng_002_topic = const('leddeng002')
woshideng_002_topic = const('woshideng002')
serverIP = const('bemfa.com')
port = const(9501)
client = None


# 接收消息，并处理
def MsgOK(topic, msg):          # 回调函数，用于收到消息
    print((topic, msg))             # 打印主题值和消息值
    if topic == leddeng_002_topic.encode():
        if msg == b"on":
            print("开灯")
        elif msg == b"off":
            print("关灯")
    if topic == woshideng_002_topic.encode():
        if msg == b"on":
            print("开灯2222")
        elif msg == b"off":
            print("关灯222")


# 初始化mqtt连接配置
def connect_and_subscribe():
    client = MQTTClient(clientID, serverIP, port, keepalive=30)
    client.set_callback(MsgOK)
    client.connect()
    client.subscribe(woshideng_002_topic)
    client.subscribe(leddeng_002_topic)
    print("Connected to %s" % serverIP)
    return client


def restart_and_reconnect():
    print('Failed to connect to MQTT broker. Reconnecting...')
    sleep(10)
    machine.reset()


def ping(self):
    print("ping...")
    client.ping()


def do_mqtt():
    # 开始连接MQTT
    try:
        global client
        client = connect_and_subscribe()
    except OSError as e:
        restart_and_reconnect()

    # 开启定时器，定时发送心跳,如果不发送心跳，设备会掉线
    tim = Timer(-1)
    tim.init(period=30000, mode=Timer.PERIODIC, callback=ping)

    while True:
        try:
            client.check_msg()
        except OSError as e:  # 如果出错就重新启动
            print('Failed to connect to MQTT broker. Reconnecting...')
            restart_and_reconnect()
