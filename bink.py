import time
flashes = 50
flashDelay = 200
led = Pin("LED", Pin.OUT)

while flashes > 0:
    flashes-=1
    time.sleep_ms(flashDelay)
    led.toggle()
