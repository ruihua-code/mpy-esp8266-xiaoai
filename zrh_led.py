from machine import Pin


led_pin = Pin(14, Pin.OUT, Pin.PULL_UP)


def on_led():
    led_pin.value(1)


def off_led():
    led_pin.value(0)
