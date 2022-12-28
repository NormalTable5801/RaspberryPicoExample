from machine import Pin,PWM
import utime
led =machine.PWM(machine.Pin(25))
led.freq(1000)
while True:
    for i in range(0,65535,2):
        led.duty_u16(i)
        utime.sleep(0.0005)
    for i in range(0,65535,2):
        led.duty_u16(65535-i)
        utime.sleep(0.0005)
