import max7219.led as led

device = led.matrix()

device.orientation(180)
device.show_message('Hello World!')
