import RPI GPIO as gpio
import time

gpio.setnode(gpio.BOARD)
gpio.setnode(32, gpio.OUT)
while True:
    gpio.output(32,0)
    time sleep(1)
    gpio.output (32, 0)
    time sleep (1)





import ADEfruit_DHT as DHT
import time as t

while True:
    umid, temp = dht.read.retry(dht.DHT11, 4)
    print("Temp [0,0 ?]    Umid: [1,1 ?] ".format(temp, umid))
    t.sleep(15*60)
